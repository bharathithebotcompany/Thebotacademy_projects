import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 06 — Transformer Architecture

## Terms & Definitions
- **Transformer block (decoder block)**: the repeating unit of a GPT-style model — multi-head causal attention followed by a feedforward MLP, each wrapped with LayerNorm and a residual connection.
- **Pre-norm**: applying LayerNorm *before* attention/MLP (as GPT-2 onward does), rather than after (the original 2017 paper's choice) — empirically trains more stably at scale.
- **Decoder-only architecture**: a Transformer built entirely from causally-masked blocks like this, used for autoregressive generation (GPT family). Contrasts with **encoder-only** (BERT — bidirectional attention, no causal mask, good for understanding/classifying text but not generating it) and **encoder-decoder** (T5, original Transformer — used for tasks like translation with a distinct source/target).
- **Depth (`n_layer`)**: how many Transformer blocks are stacked.
- **Width (`n_embd`)**: the embedding dimension flowing through the whole network.

## Assembling the Pieces
Every ingredient for a full Transformer block was covered in earlier notebooks:
- **Embeddings** (03): turn token IDs into vectors, add positional information.
- **LayerNorm, residual connections** (04): stabilize and ease training of deep stacks.
- **Multi-head causal attention** (05): let tokens gather information from earlier tokens.
- **MLP / feedforward layer** (04's linear + activation): after attention mixes information *across* positions, the MLP processes *each* position's vector independently, expanding then compressing it (typically 4x wider in the middle) to let the model do more complex per-token computation.

A single decoder block, in the pre-norm style GPT-2/3 and our `GPTMicro` use:

```
x = x + Attention(LayerNorm(x))
x = x + MLP(LayerNorm(x))
```

Both lines are residual connections wrapping a normalized sub-layer — exactly the pattern from notebook 04, just with attention and MLP as the two "layers" being wrapped.

## History
The 2017 Transformer paper used **post-norm** (LayerNorm *after* the residual add) and an **encoder-decoder** structure for machine translation. GPT (2018) adapted it to **decoder-only** (dropping the encoder, keeping only causally-masked self-attention) since generation is the goal. GPT-2 (2019) switched to **pre-norm**, which turned out to make training much more stable as models got deeper — a change nearly every subsequent LLM has kept.

## Why Decoder-Only for a Language Model?
Our goal (next-token prediction, autoregressive generation) requires that token $i$ never see tokens $> i$ — otherwise the model could "cheat" during training by looking at the very answer it's supposed to predict. That's exactly what the causal mask from notebook 05 enforces, and it's why GPT-style models are called decoder-only: every block uses *masked* self-attention. BERT-style encoder-only models remove the mask (full bidirectional attention) because their goal is understanding/classifying already-complete text, not generating new text left-to-right — bidirectional context helps there but would leak future answers here.
"""),
    code("""
import sys
sys.path.insert(0, "..")

import torch
import torch.nn as nn
import torch.nn.functional as F
import math

torch.manual_seed(0)
"""),
    md("""
## A Single Decoder Block, Built From Notebook 04/05 Pieces
"""),
    code("""
class CausalSelfAttention(nn.Module):
    def __init__(self, n_embd, n_head, block_size):
        super().__init__()
        self.n_head = n_head
        self.head_dim = n_embd // n_head
        self.qkv = nn.Linear(n_embd, 3 * n_embd)
        self.out_proj = nn.Linear(n_embd, n_embd)
        mask = torch.tril(torch.ones(block_size, block_size))
        self.register_buffer("mask", mask.view(1, 1, block_size, block_size))

    def forward(self, x):
        B, T, C = x.shape
        qkv = self.qkv(x)
        q, k, v = qkv.split(C, dim=2)
        q = q.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        att = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        att = att.masked_fill(self.mask[:, :, :T, :T] == 0, float("-inf"))
        att = F.softmax(att, dim=-1)
        out = (att @ v).transpose(1, 2).contiguous().view(B, T, C)
        return self.out_proj(out)


class MLP(nn.Module):
    def __init__(self, n_embd):
        super().__init__()
        self.fc = nn.Linear(n_embd, 4 * n_embd)
        self.proj = nn.Linear(4 * n_embd, n_embd)
        self.act = nn.GELU()

    def forward(self, x):
        return self.proj(self.act(self.fc(x)))


class DecoderBlock(nn.Module):
    \"\"\"One Transformer decoder block: pre-norm attention + pre-norm MLP,
    each wrapped in a residual connection.\"\"\"

    def __init__(self, n_embd, n_head, block_size):
        super().__init__()
        self.ln1 = nn.LayerNorm(n_embd)
        self.attn = CausalSelfAttention(n_embd, n_head, block_size)
        self.ln2 = nn.LayerNorm(n_embd)
        self.mlp = MLP(n_embd)

    def forward(self, x):
        x = x + self.attn(self.ln1(x))   # residual around attention
        x = x + self.mlp(self.ln2(x))    # residual around MLP
        return x

block = DecoderBlock(n_embd=32, n_head=4, block_size=16)
x = torch.randn(2, 10, 32)  # 2 sequences, 10 tokens, 32-dim embeddings
out = block(x)
print("input shape: ", x.shape)
print("output shape:", out.shape, "-- same shape in and out, so blocks can be stacked freely")
"""),
    md("""
## Stacking Blocks

The whole point of the residual + pre-norm design: because each block's output shape matches its input shape, and the residual path preserves a clean gradient signal, we can stack as many blocks as we want (6 in our `GPTMicro`, 96 in GPT-3) without the architecture needing to change.
"""),
    code("""
class MiniGPT(nn.Module):
    \"\"\"A minimal illustration of stacking decoder blocks + a language-model head.
    This is NOT the real GPTMicro (see src/model.py for that) -- just a compact
    version to show the full architecture end-to-end in one place.\"\"\"

    def __init__(self, vocab_size, n_embd, n_head, n_layer, block_size):
        super().__init__()
        self.block_size = block_size
        self.token_emb = nn.Embedding(vocab_size, n_embd)
        self.pos_emb = nn.Embedding(block_size, n_embd)
        self.blocks = nn.ModuleList([DecoderBlock(n_embd, n_head, block_size) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size, bias=False)

    def forward(self, idx):
        B, T = idx.shape
        pos = torch.arange(T, device=idx.device)
        x = self.token_emb(idx) + self.pos_emb(pos)
        for block in self.blocks:
            x = block(x)
        x = self.ln_f(x)
        return self.lm_head(x)

mini_gpt = MiniGPT(vocab_size=100, n_embd=32, n_head=4, n_layer=3, block_size=16)
idx = torch.randint(0, 100, (2, 10))
logits = mini_gpt(idx)
print("input token ids shape:", idx.shape)
print("output logits shape:  ", logits.shape, "-- (batch, seq_len, vocab_size): a distribution over next-token for every position")

n_params = sum(p.numel() for p in mini_gpt.parameters())
print(f"total parameters in this tiny 3-layer demo model: {n_params:,}")
"""),
    md("""
## Data Flow Summary

```
token ids  ->  [token_emb + pos_emb]  ->  [DecoderBlock] x n_layer  ->  [LayerNorm]  ->  [lm_head]  ->  logits
   (03)              (03)                   (04 + 05)                     (04)          (04)
```

Every arrow above was covered in a previous notebook — the Transformer's only genuinely new ingredient versus a plain deep MLP is attention (05); everything else (embeddings, LayerNorm, residuals, linear+activation, softmax+cross-entropy) is standard deep learning machinery from notebook 04.

## Exercise
Compare `MiniGPT` above to the real `GPTMicro` in `src/model.py`. The real version adds: dropout (regularization — randomly zeroing some activations during training to reduce overfitting), weight tying (sharing the token embedding matrix with the output `lm_head`, halving that parameter count), and a `generate()` method for autoregressive sampling (covered in notebook 09).

## Summary
- A decoder block is: `x = x + Attn(LN(x))` then `x = x + MLP(LN(x))` — pre-norm, residual-wrapped attention and MLP.
- Stacking many identical blocks (depth = `n_layer`) is what makes a "big" model big; the architecture doesn't otherwise change.
- Decoder-only + causal masking is specifically what makes a Transformer suitable for autoregressive generation, as opposed to encoder-only (BERT, bidirectional, for understanding) or encoder-decoder (translation-style) variants.

Next: **07 — Building the Model** (assemble the *real* `GPTMicro`, tuned to land at ~20M parameters, and verify its exact size).
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "06_transformer_architecture.ipynb", cells)
