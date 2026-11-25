"""
LLM From Scratch — chapter notebook generator.

Each chapter is defined ONCE as a list of (kind, payload) sections:
  ("md",   markdown_string)
  ("code", code_string)                       # appears identically in both versions
  ("todo", answer_code, blanked_code)         # answer notebook gets answer_code,
                                              # todo notebook gets blanked_code

Emits two notebooks per chapter:
  notebooks/answer/Chapter{NN}_{slug}_answer.ipynb
  notebooks/todo/Chapter{NN}_{slug}_todo.ipynb
"""
import json, pathlib

USER, REPO, BRANCH = "kader-xai", "llm-from-scratch", "main"
ROOT = pathlib.Path("/Users/kader/Downloads/llm-from-scratch")

def _cell_md(t):   return {"cell_type":"markdown","metadata":{},"source":t.splitlines(keepends=True)}
def _cell_code(t): return {"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":t.splitlines(keepends=True)}

def badge(nn, slug, kind):
    path = f"notebooks/{kind}/Chapter{nn:02d}_{slug}_{kind}.ipynb"
    return (f'<a href="https://colab.research.google.com/github/{USER}/{REPO}/blob/{BRANCH}/{path}" '
            f'target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" '
            f'alt="Open In Colab"/></a>')

def emit(nn, slug, title, sections):
    for kind in ("answer", "todo"):
        cells = [_cell_md(f"{badge(nn, slug, kind)}\n\n"
                          f"> 🧱 **LLM From Scratch · Chapter {nn:02d} — {title}**\n\n"
                          f"> {'✅ Answer notebook — full working code.' if kind=='answer' else '✍️ TODO notebook — fill in the `# YOUR CODE HERE` blanks, then check against the answer.'}")]
        for sec in sections:
            if sec[0] == "md":
                cells.append(_cell_md(sec[1]))
            elif sec[0] == "code":
                cells.append(_cell_code(sec[1]))
            elif sec[0] == "todo":
                _, answer_code, todo_code = sec
                cells.append(_cell_code(answer_code if kind == "answer" else todo_code))
        nb = {"cells": cells,
              "metadata": {"kernelspec": {"display_name":"Python 3","language":"python","name":"python3"},
                           "language_info": {"name":"python"}},
              "nbformat": 4, "nbformat_minor": 5}
        out = ROOT / "notebooks" / kind / f"Chapter{nn:02d}_{slug}_{kind}.ipynb"
        out.write_text(json.dumps(nb, indent=1))
    print(f"Chapter {nn:02d} — {title}: wrote answer + todo")


# ════════════════════════════════════════════════════════════════════════════
# SHARED SETUP CELL  (every chapter starts here)
# ════════════════════════════════════════════════════════════════════════════
SETUP = """# ── Setup (run first) ─────────────────────────────────────────────────
# Pure PyTorch — no extra installs needed beyond torch (preinstalled on Colab).
import torch, torch.nn as nn, torch.nn.functional as F
torch.manual_seed(1337)
device = "cuda" if torch.cuda.is_available() else "cpu"
print("torch", torch.__version__, "| device:", device)"""

DATA = """# Download the training corpus (Tiny Shakespeare, ~1 MB) if not present.
import os, urllib.request
if not os.path.exists("input.txt"):
    url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    urllib.request.urlretrieve(url, "input.txt")
text = open("input.txt").read()
print(f"corpus: {len(text):,} characters")
print(text[:200])"""


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 00 — Start / Tutorial
# ════════════════════════════════════════════════════════════════════════════
emit(0, "start", "Start Here — How This Series Works", [
("md", """## What you're going to build

By the end of this series you will have built a working **GPT language model from scratch** in
pure PyTorch — every line, no `transformers` library — and trained it to generate Shakespeare-like
text. We build it *one component at a time*, the way you'd assemble an engine from parts:

```
Chapter 01  Dataloader        →  turn text into training batches
Chapter 02  Token Embedding   →  map token ids to vectors
Chapter 03  Position Embedding→  tell the model where each token is
Chapter 04  Embedding Module  →  combine token + position
Chapter 05  LayerNorm         →  stabilise activations
Chapter 06  Attention Head    →  the core "look at other tokens" op
Chapter 07  Multi-Head Attn   →  several heads in parallel
Chapter 08  FeedForward       →  per-token MLP
Chapter 09  Transformer Block →  attention + FFN + residuals
Chapter 10  LM Head           →  hidden state → vocabulary logits
Chapter 11  nanoGPT           →  assemble the full model
Chapter 12  Trainer           →  the training loop
Chapter 13  Generate          →  sample text from your model
```

Each chapter ships in **two versions**:
- **`todo`** — has `# YOUR CODE HERE` blanks for you to fill in.
- **`answer`** — the complete working code, to check yourself against.

### How to use it
1. Open the **todo** notebook for a chapter in Colab.
2. Read the explanation, fill in the blanks, run the cell.
3. If stuck, peek at the **answer** notebook.
4. Move to the next chapter — each one imports the pieces you built conceptually before.

Let's make sure your environment works."""),
("code", SETUP),
("code", DATA),
("md", """## The mental model — a "tensor map"

Everything in a transformer is a tensor reshaping pipeline. Keep this shape map in your head; we
fill it in chapter by chapter:

```
ids        (B, T)            integer token ids
embed      (B, T, C)         each token → C-dim vector            ← Ch 02-04
block ×N   (B, T, C)         attention + FFN, shape preserved     ← Ch 05-09
logits     (B, T, vocab)     next-token scores                    ← Ch 10
```

`B` = batch size, `T` = sequence length (context), `C` = embedding dim, `vocab` = number of tokens.
Knowing the shape at every step is 80% of understanding a transformer."""),
("code", """# Quick sanity check that you can make and reshape tensors.
x = torch.randint(0, 65, (4, 8))      # (B=4, T=8) fake token ids
print("ids:", x.shape)
emb = torch.randn(4, 8, 32)           # (B, T, C=32) pretend embeddings
print("embeddings:", emb.shape)
print("✅ environment ready — go to Chapter 01")"""),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 01 — Dataloader
# ════════════════════════════════════════════════════════════════════════════
emit(1, "dataloader", "Dataloader — Text → Batches", [
("md", """## Goal

A language model trains on `(context, next-token)` pairs. We need to:
1. Build a **character-level tokenizer** (map each unique char ↔ an integer).
2. Encode the whole corpus into one long tensor of ids.
3. Sample random **batches** of `(x, y)` where `y` is `x` shifted one position right.

Character-level keeps things simple — vocab is just the unique characters (~65 for Shakespeare)."""),
("code", SETUP),
("code", DATA),
("md", """## 1 · Character tokenizer

`stoi` maps string→int, `itos` maps int→string. `encode` and `decode` use them."""),
("todo",
"""chars = sorted(set(text))
vocab_size = len(chars)
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s]
decode = lambda ids: "".join(itos[i] for i in ids)

print("vocab_size:", vocab_size)
print("encode('hi there'):", encode("hi there"))
print("decode back:", decode(encode("hi there")))""",
"""chars = sorted(set(text))
vocab_size = len(chars)
# YOUR CODE HERE: build stoi (char->int) and itos (int->char) dicts
stoi = ...
itos = ...
encode = lambda s: [stoi[c] for c in s]
decode = lambda ids: "".join(itos[i] for i in ids)

print("vocab_size:", vocab_size)
print("encode('hi there'):", encode("hi there"))
print("decode back:", decode(encode("hi there")))"""),
("md", """## 2 · Encode the corpus + train/val split"""),
("code", """data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))
train_data, val_data = data[:n], data[n:]
print("train tokens:", len(train_data), "| val tokens:", len(val_data))"""),
("md", """## 3 · Batch sampler

For a context length `block_size`, pick `batch_size` random start positions. `x` is the context,
`y` is `x` shifted by one — the target the model must predict at each position."""),
("todo",
"""block_size = 8
batch_size = 4

def get_batch(split):
    d = train_data if split == "train" else val_data
    ix = torch.randint(len(d) - block_size, (batch_size,))
    x = torch.stack([d[i:i+block_size] for i in ix])
    y = torch.stack([d[i+1:i+block_size+1] for i in ix])
    return x.to(device), y.to(device)

xb, yb = get_batch("train")
print("x:", xb.shape, "y:", yb.shape)
print("first context:", decode(xb[0].tolist()))
print("first target :", decode(yb[0].tolist()))""",
"""block_size = 8
batch_size = 4

def get_batch(split):
    d = train_data if split == "train" else val_data
    ix = torch.randint(len(d) - block_size, (batch_size,))
    # YOUR CODE HERE: x = contexts of length block_size; y = same shifted right by 1
    x = ...
    y = ...
    return x.to(device), y.to(device)

xb, yb = get_batch("train")
print("x:", xb.shape, "y:", yb.shape)
print("first context:", decode(xb[0].tolist()))
print("first target :", decode(yb[0].tolist()))"""),
("md", "✅ You can now turn text into training batches. Next: turn ids into vectors."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 02 — Token Embedding
# ════════════════════════════════════════════════════════════════════════════
emit(2, "token_embedding", "Token Embedding — ids → vectors", [
("md", """## Goal

A token id (e.g. `42`) carries no meaning on its own. A **token embedding** is a learnable lookup
table of shape `(vocab_size, C)` — row `i` is the C-dim vector for token `i`. The model learns these
vectors during training so that similar tokens get similar vectors.

`nn.Embedding(vocab_size, C)` *is* that table; calling it with ids does the row lookup."""),
("code", SETUP),
("todo",
"""vocab_size = 65       # Shakespeare char vocab
C = 32                # embedding dimension

token_embedding = nn.Embedding(vocab_size, C)

ids = torch.randint(0, vocab_size, (4, 8))      # (B, T)
tok_emb = token_embedding(ids)                  # (B, T, C)
print("ids:    ", ids.shape)
print("tok_emb:", tok_emb.shape)               # (4, 8, 32)
print("table:  ", token_embedding.weight.shape) # (65, 32) learnable rows""",
"""vocab_size = 65
C = 32

# YOUR CODE HERE: create an embedding table mapping vocab_size ids to C-dim vectors
token_embedding = ...

ids = torch.randint(0, vocab_size, (4, 8))
tok_emb = token_embedding(ids)
print("ids:    ", ids.shape)
print("tok_emb:", tok_emb.shape)
print("table:  ", token_embedding.weight.shape)"""),
("md", """## Why a lookup table and not one-hot × matrix?

`nn.Embedding(ids)` is mathematically identical to one-hot-encoding `ids` and multiplying by the
table — but it skips building the huge one-hot tensor. It's just an indexed row-gather. That's the
whole trick."""),
("code", """# Prove the lookup == one-hot @ table
onehot = F.one_hot(ids, vocab_size).float()       # (B, T, vocab)
manual = onehot @ token_embedding.weight          # (B, T, C)
print("max diff:", (manual - tok_emb).abs().max().item())   # ~0"""),
("md", "✅ Tokens are now vectors. But the model still doesn't know *order*. Next: position."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 03 — Position Embedding
# ════════════════════════════════════════════════════════════════════════════
emit(3, "position_embedding", "Position Embedding — where is each token?", [
("md", """## Goal

Attention (Chapter 06) is **permutation-invariant** — by itself it can't tell "the cat sat" from
"sat cat the". We fix this by adding a **position embedding**: a second learnable table of shape
`(block_size, C)`, where row `t` is the vector for position `t`. We add it to the token embedding."""),
("code", SETUP),
("todo",
"""block_size = 8
C = 32

position_embedding = nn.Embedding(block_size, C)   # one row per position

T = 8
pos = torch.arange(T)                # [0,1,2,...,T-1]
pos_emb = position_embedding(pos)    # (T, C)
print("pos:    ", pos)
print("pos_emb:", pos_emb.shape)     # (8, 32)""",
"""block_size = 8
C = 32

# YOUR CODE HERE: a learnable table with one C-dim vector per position (0..block_size-1)
position_embedding = ...

T = 8
pos = torch.arange(T)
pos_emb = position_embedding(pos)
print("pos:    ", pos)
print("pos_emb:", pos_emb.shape)"""),
("md", """## Adding token + position

Broadcasting handles the batch dimension: `(B, T, C) + (T, C)` → `(B, T, C)`. Every token now
carries *what it is* (token emb) plus *where it is* (position emb)."""),
("code", """tok_emb = torch.randn(4, 8, C)      # pretend token embeddings (B, T, C)
x = tok_emb + pos_emb               # (4, 8, 32) + (8, 32) -> (4, 8, 32)
print("combined:", x.shape)"""),
("md", "✅ Order information is in. Next we package token + position into one reusable module."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 04 — Embedding Module
# ════════════════════════════════════════════════════════════════════════════
emit(4, "embedding_module", "Embedding Module — package it up", [
("md", """## Goal

Wrap token + position embedding into a single `nn.Module` so the rest of the model just calls
`embed(ids)` and gets back `(B, T, C)`. This is the first real building block of our GPT."""),
("code", SETUP),
("todo",
"""class Embedding(nn.Module):
    def __init__(self, vocab_size, block_size, C):
        super().__init__()
        self.tok = nn.Embedding(vocab_size, C)
        self.pos = nn.Embedding(block_size, C)
    def forward(self, ids):                 # ids: (B, T)
        B, T = ids.shape
        tok_emb = self.tok(ids)             # (B, T, C)
        pos_emb = self.pos(torch.arange(T, device=ids.device))   # (T, C)
        return tok_emb + pos_emb            # (B, T, C)

embed = Embedding(vocab_size=65, block_size=8, C=32)
out = embed(torch.randint(0, 65, (4, 8)))
print("embedding output:", out.shape)       # (4, 8, 32)""",
"""class Embedding(nn.Module):
    def __init__(self, vocab_size, block_size, C):
        super().__init__()
        # YOUR CODE HERE: create token + position embedding tables
        self.tok = ...
        self.pos = ...
    def forward(self, ids):                 # ids: (B, T)
        B, T = ids.shape
        # YOUR CODE HERE: look up token + position embeddings and add them
        tok_emb = ...
        pos_emb = ...
        return tok_emb + pos_emb

embed = Embedding(vocab_size=65, block_size=8, C=32)
out = embed(torch.randint(0, 65, (4, 8)))
print("embedding output:", out.shape)"""),
("md", "✅ One clean module turns ids into vectors. Next: LayerNorm to keep activations stable."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 05 — LayerNorm
# ════════════════════════════════════════════════════════════════════════════
emit(5, "layernorm", "LayerNorm — stabilise activations", [
("md", """## Goal

Deep networks train badly when activation magnitudes drift. **LayerNorm** normalises each token's
vector to zero mean / unit variance across its `C` features, then rescales with learnable `gamma`
(scale) and `beta` (shift). We implement it from scratch to demystify it."""),
("code", SETUP),
("todo",
"""class LayerNorm(nn.Module):
    def __init__(self, C, eps=1e-5):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(C))
        self.beta  = nn.Parameter(torch.zeros(C))
        self.eps = eps
    def forward(self, x):                      # x: (B, T, C)
        mean = x.mean(-1, keepdim=True)
        var  = x.var(-1, keepdim=True, unbiased=False)
        xhat = (x - mean) / torch.sqrt(var + self.eps)
        return self.gamma * xhat + self.beta

ln = LayerNorm(32)
x = torch.randn(4, 8, 32) * 5 + 2              # off-centre, high variance
y = ln(x)
print("before: mean=%.2f std=%.2f" % (x.mean(), x.std()))
print("after:  mean=%.2f std=%.2f" % (y.mean(), y.std()))   # ~0 mean, ~1 std""",
"""class LayerNorm(nn.Module):
    def __init__(self, C, eps=1e-5):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(C))
        self.beta  = nn.Parameter(torch.zeros(C))
        self.eps = eps
    def forward(self, x):                      # x: (B, T, C)
        # YOUR CODE HERE: normalise x over its LAST dim, then scale+shift
        mean = ...
        var  = ...
        xhat = ...
        return self.gamma * xhat + self.beta

ln = LayerNorm(32)
x = torch.randn(4, 8, 32) * 5 + 2
y = ln(x)
print("before: mean=%.2f std=%.2f" % (x.mean(), x.std()))
print("after:  mean=%.2f std=%.2f" % (y.mean(), y.std()))"""),
("md", "✅ Activations stay tame. Now the heart of the transformer: attention."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 06 — Attention Head
# ════════════════════════════════════════════════════════════════════════════
emit(6, "attention_head", "Attention Head — the core operation", [
("md", """## Goal — the most important chapter

A single **causal self-attention head**. Each token produces a **query** (what am I looking for?),
a **key** (what do I offer?) and a **value** (what I'll pass on). A token attends to earlier tokens
by comparing its query to their keys, then takes a weighted sum of their values.

Shapes: from `x: (B, T, C)` we make `q, k, v: (B, T, head_size)`. The attention matrix is
`(B, T, T)`. **Causal masking** sets future positions to `-inf` so a token can only see the past."""),
("code", SETUP),
("md", """## Step 1 · Q, K, V projections and the score matrix"""),
("todo",
"""C, head_size, block_size = 32, 16, 8

key   = nn.Linear(C, head_size, bias=False)
query = nn.Linear(C, head_size, bias=False)
value = nn.Linear(C, head_size, bias=False)

x = torch.randn(4, block_size, C)              # (B, T, C)
k = key(x)                                     # (B, T, head_size)
q = query(x)
v = value(x)

scores = q @ k.transpose(-2, -1) * head_size ** -0.5   # (B, T, T), scaled
print("scores:", scores.shape)""",
"""C, head_size, block_size = 32, 16, 8

key   = nn.Linear(C, head_size, bias=False)
query = nn.Linear(C, head_size, bias=False)
value = nn.Linear(C, head_size, bias=False)

x = torch.randn(4, block_size, C)
k = key(x); q = query(x); v = value(x)

# YOUR CODE HERE: scaled dot-product scores  q·kᵀ / sqrt(head_size)  -> (B, T, T)
scores = ...
print("scores:", scores.shape)"""),
("md", """## Step 2 · Causal mask + softmax + weighted sum

We mask the upper triangle (future) to `-inf`, softmax over the last dim to get weights that sum to
1, then multiply by `v`."""),
("todo",
"""tril = torch.tril(torch.ones(block_size, block_size))
scores = scores.masked_fill(tril == 0, float("-inf"))   # block future
weights = F.softmax(scores, dim=-1)                     # (B, T, T)
out = weights @ v                                       # (B, T, head_size)
print("attention weights row 0 (token 0 sees only itself):")
print(weights[0, 0].round(decimals=2))
print("out:", out.shape)""",
"""tril = torch.tril(torch.ones(block_size, block_size))
# YOUR CODE HERE: mask future positions to -inf, softmax, then weighted sum of v
scores = ...
weights = ...
out = ...
print("attention weights row 0:")
print(weights[0, 0].round(decimals=2))
print("out:", out.shape)"""),
("md", """## Step 3 · Package as a Head module"""),
("code", """class Head(nn.Module):
    def __init__(self, C, head_size, block_size):
        super().__init__()
        self.key   = nn.Linear(C, head_size, bias=False)
        self.query = nn.Linear(C, head_size, bias=False)
        self.value = nn.Linear(C, head_size, bias=False)
        self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size)))
        self.scale = head_size ** -0.5
    def forward(self, x):
        B, T, C = x.shape
        k, q, v = self.key(x), self.query(x), self.value(x)
        att = q @ k.transpose(-2, -1) * self.scale
        att = att.masked_fill(self.tril[:T, :T] == 0, float("-inf"))
        att = F.softmax(att, dim=-1)
        return att @ v

h = Head(32, 16, 8)
print("Head output:", h(torch.randn(4, 8, 32)).shape)    # (4, 8, 16)"""),
("md", "✅ You built attention. Next: run several heads in parallel."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 07 — Multi-Head Attention
# ════════════════════════════════════════════════════════════════════════════
emit(7, "multihead_attention", "Multi-Head Attention — heads in parallel", [
("md", """## Goal

One head learns one kind of relationship. **Multi-head attention** runs `n_head` heads in parallel
(each with `head_size = C // n_head`), concatenates their outputs back to `C`, and projects once
more. More heads = more relationship types learned at once."""),
("code", SETUP),
("code", """# Reuse the Head from Chapter 06
class Head(nn.Module):
    def __init__(self, C, head_size, block_size):
        super().__init__()
        self.key   = nn.Linear(C, head_size, bias=False)
        self.query = nn.Linear(C, head_size, bias=False)
        self.value = nn.Linear(C, head_size, bias=False)
        self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size)))
        self.scale = head_size ** -0.5
    def forward(self, x):
        B, T, C = x.shape
        k, q, v = self.key(x), self.query(x), self.value(x)
        att = q @ k.transpose(-2, -1) * self.scale
        att = att.masked_fill(self.tril[:T, :T] == 0, float("-inf"))
        att = F.softmax(att, dim=-1)
        return att @ v"""),
("todo",
"""class MultiHeadAttention(nn.Module):
    def __init__(self, C, n_head, block_size):
        super().__init__()
        head_size = C // n_head
        self.heads = nn.ModuleList([Head(C, head_size, block_size) for _ in range(n_head)])
        self.proj = nn.Linear(C, C)
    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)   # (B, T, C)
        return self.proj(out)

mha = MultiHeadAttention(C=32, n_head=4, block_size=8)
print("MHA output:", mha(torch.randn(4, 8, 32)).shape)        # (4, 8, 32)""",
"""class MultiHeadAttention(nn.Module):
    def __init__(self, C, n_head, block_size):
        super().__init__()
        head_size = C // n_head
        # YOUR CODE HERE: a list of n_head Heads, plus an output projection Linear(C, C)
        self.heads = ...
        self.proj = ...
    def forward(self, x):
        # YOUR CODE HERE: run every head, concatenate along the feature dim, then project
        out = ...
        return self.proj(out)

mha = MultiHeadAttention(C=32, n_head=4, block_size=8)
print("MHA output:", mha(torch.randn(4, 8, 32)).shape)"""),
("md", "✅ Attention is complete. Next: the per-token MLP (FeedForward)."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 08 — FeedForward
# ════════════════════════════════════════════════════════════════════════════
emit(8, "feedforward", "FeedForward — the per-token MLP", [
("md", """## Goal

Attention *moves information between* tokens. The **FeedForward** network lets each token *think*
about that information on its own. It's a 2-layer MLP applied independently per position, with a 4×
hidden expansion and a non-linearity (GELU)."""),
("code", SETUP),
("todo",
"""class FeedForward(nn.Module):
    def __init__(self, C):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(C, 4 * C),     # expand
            nn.GELU(),               # non-linearity
            nn.Linear(4 * C, C),     # project back
        )
    def forward(self, x):
        return self.net(x)

ff = FeedForward(32)
print("FFN output:", ff(torch.randn(4, 8, 32)).shape)    # (4, 8, 32)""",
"""class FeedForward(nn.Module):
    def __init__(self, C):
        super().__init__()
        # YOUR CODE HERE: Linear(C->4C) -> GELU -> Linear(4C->C)
        self.net = ...
    def forward(self, x):
        return self.net(x)

ff = FeedForward(32)
print("FFN output:", ff(torch.randn(4, 8, 32)).shape)"""),
("md", "✅ Both sub-layers exist. Next: wire them into a Transformer block with residuals."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 09 — Transformer Block
# ════════════════════════════════════════════════════════════════════════════
emit(9, "transformer_block", "Transformer Block — attention + FFN + residuals", [
("md", """## Goal

A **Transformer block** combines everything with the **Pre-LN residual** pattern used by GPT-2+:

```
x = x + MultiHeadAttention(LayerNorm(x))
x = x + FeedForward(LayerNorm(x))
```

The `x +` (residual / skip connection) lets gradients flow through deep stacks; the LayerNorm sits
*inside* the residual (Pre-LN) for stable training. Stacking N of these blocks is the model's depth."""),
("code", SETUP),
("code", """# Re-define the pieces from Ch 05-08 (so this notebook is self-contained)
class Head(nn.Module):
    def __init__(s, C, hs, bs):
        super().__init__()
        s.key=nn.Linear(C,hs,bias=False); s.query=nn.Linear(C,hs,bias=False); s.value=nn.Linear(C,hs,bias=False)
        s.register_buffer("tril", torch.tril(torch.ones(bs,bs))); s.scale=hs**-0.5
    def forward(s,x):
        B,T,C=x.shape; k,q,v=s.key(x),s.query(x),s.value(x)
        a=(q@k.transpose(-2,-1)*s.scale).masked_fill(s.tril[:T,:T]==0,float("-inf"))
        return F.softmax(a,-1)@v
class MultiHeadAttention(nn.Module):
    def __init__(s,C,nh,bs):
        super().__init__(); s.heads=nn.ModuleList([Head(C,C//nh,bs) for _ in range(nh)]); s.proj=nn.Linear(C,C)
    def forward(s,x): return s.proj(torch.cat([h(x) for h in s.heads],-1))
class FeedForward(nn.Module):
    def __init__(s,C): super().__init__(); s.net=nn.Sequential(nn.Linear(C,4*C),nn.GELU(),nn.Linear(4*C,C))
    def forward(s,x): return s.net(x)"""),
("todo",
"""class Block(nn.Module):
    def __init__(self, C, n_head, block_size):
        super().__init__()
        self.sa  = MultiHeadAttention(C, n_head, block_size)
        self.ff  = FeedForward(C)
        self.ln1 = nn.LayerNorm(C)
        self.ln2 = nn.LayerNorm(C)
    def forward(self, x):
        x = x + self.sa(self.ln1(x))      # Pre-LN residual around attention
        x = x + self.ff(self.ln2(x))      # Pre-LN residual around FFN
        return x

block = Block(C=32, n_head=4, block_size=8)
print("Block output:", block(torch.randn(4, 8, 32)).shape)   # (4, 8, 32) — shape preserved""",
"""class Block(nn.Module):
    def __init__(self, C, n_head, block_size):
        super().__init__()
        self.sa  = MultiHeadAttention(C, n_head, block_size)
        self.ff  = FeedForward(C)
        self.ln1 = nn.LayerNorm(C)
        self.ln2 = nn.LayerNorm(C)
    def forward(self, x):
        # YOUR CODE HERE: Pre-LN residual — add attention(ln1(x)), then add ff(ln2(x))
        x = ...
        x = ...
        return x

block = Block(C=32, n_head=4, block_size=8)
print("Block output:", block(torch.randn(4, 8, 32)).shape)"""),
("md", "✅ The repeating unit is done. Next: turn the final hidden state into vocab logits."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — LM Head (Vocabulary Logits)
# ════════════════════════════════════════════════════════════════════════════
emit(10, "lm_head", "LM Head — hidden state → next-token logits", [
("md", """## Goal

After the blocks we have `(B, T, C)` hidden states. To predict the next token we need a score for
every vocabulary entry at every position: `(B, T, vocab_size)`. That's a final LayerNorm + a single
Linear (the **language-model head**). Softmax over the last dim turns logits into probabilities."""),
("code", SETUP),
("todo",
"""C, vocab_size = 32, 65

ln_f    = nn.LayerNorm(C)
lm_head = nn.Linear(C, vocab_size)

h = torch.randn(4, 8, C)               # final hidden states (B, T, C)
logits = lm_head(ln_f(h))              # (B, T, vocab_size)
print("logits:", logits.shape)         # (4, 8, 65)

probs = F.softmax(logits, dim=-1)
print("probs sum to 1:", probs[0, 0].sum().item())""",
"""C, vocab_size = 32, 65

ln_f    = nn.LayerNorm(C)
# YOUR CODE HERE: a Linear that maps C-dim hidden states to vocab_size logits
lm_head = ...

h = torch.randn(4, 8, C)
logits = lm_head(ln_f(h))
print("logits:", logits.shape)

probs = F.softmax(logits, dim=-1)
print("probs sum to 1:", probs[0, 0].sum().item())"""),
("md", """## The loss

Training compares logits to the true next token with **cross-entropy**. PyTorch wants
`(B*T, vocab)` logits and `(B*T,)` targets, so we flatten."""),
("code", """targets = torch.randint(0, vocab_size, (4, 8))      # pretend next-token labels
loss = F.cross_entropy(logits.view(-1, vocab_size), targets.view(-1))
print("loss:", loss.item())
print("random-guess loss ≈ ln(vocab) =", round(torch.log(torch.tensor(float(vocab_size))).item(), 3))"""),
("md", "✅ Every piece exists. Next: assemble the full nanoGPT."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 11 — nanoGPT (assemble)
# ════════════════════════════════════════════════════════════════════════════
emit(11, "nanogpt", "nanoGPT — assemble the full model", [
("md", """## Goal

Bolt everything together into one `GPT` module:

```
ids → Embedding → [Block × N] → final LayerNorm → LM head → logits
```

The full forward also computes the loss when given targets, and we add a `generate()` method to
sample text. This is a complete, trainable GPT in ~40 lines."""),
("code", SETUP),
("code", """# All components from Ch 04-10, compactly (self-contained)
class Head(nn.Module):
    def __init__(s,C,hs,bs):
        super().__init__()
        s.key=nn.Linear(C,hs,bias=False); s.query=nn.Linear(C,hs,bias=False); s.value=nn.Linear(C,hs,bias=False)
        s.register_buffer("tril",torch.tril(torch.ones(bs,bs))); s.scale=hs**-0.5
    def forward(s,x):
        B,T,C=x.shape; k,q,v=s.key(x),s.query(x),s.value(x)
        a=(q@k.transpose(-2,-1)*s.scale).masked_fill(s.tril[:T,:T]==0,float("-inf"))
        return F.softmax(a,-1)@v
class MHA(nn.Module):
    def __init__(s,C,nh,bs): super().__init__(); s.heads=nn.ModuleList([Head(C,C//nh,bs) for _ in range(nh)]); s.proj=nn.Linear(C,C)
    def forward(s,x): return s.proj(torch.cat([h(x) for h in s.heads],-1))
class FF(nn.Module):
    def __init__(s,C): super().__init__(); s.net=nn.Sequential(nn.Linear(C,4*C),nn.GELU(),nn.Linear(4*C,C))
    def forward(s,x): return s.net(x)
class Block(nn.Module):
    def __init__(s,C,nh,bs): super().__init__(); s.sa=MHA(C,nh,bs); s.ff=FF(C); s.ln1=nn.LayerNorm(C); s.ln2=nn.LayerNorm(C)
    def forward(s,x): x=x+s.sa(s.ln1(x)); x=x+s.ff(s.ln2(x)); return x"""),
("todo",
"""class GPT(nn.Module):
    def __init__(self, vocab_size, C=64, n_head=4, n_layer=4, block_size=32):
        super().__init__()
        self.block_size = block_size
        self.tok = nn.Embedding(vocab_size, C)
        self.pos = nn.Embedding(block_size, C)
        self.blocks = nn.Sequential(*[Block(C, n_head, block_size) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(C)
        self.head = nn.Linear(C, vocab_size)

    def forward(self, ids, targets=None):
        B, T = ids.shape
        x = self.tok(ids) + self.pos(torch.arange(T, device=ids.device))   # (B,T,C)
        x = self.blocks(x)
        logits = self.head(self.ln_f(x))                                   # (B,T,vocab)
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

    @torch.no_grad()
    def generate(self, ids, max_new_tokens):
        for _ in range(max_new_tokens):
            ids_cond = ids[:, -self.block_size:]          # crop to context window
            logits, _ = self(ids_cond)
            probs = F.softmax(logits[:, -1, :], dim=-1)   # last-step distribution
            next_id = torch.multinomial(probs, 1)
            ids = torch.cat([ids, next_id], dim=1)
        return ids

model = GPT(vocab_size=65).to(device)
print("params:", sum(p.numel() for p in model.parameters()), "trainable")
logits, loss = model(torch.randint(0, 65, (4, 32)).to(device),
                     torch.randint(0, 65, (4, 32)).to(device))
print("logits:", logits.shape, "| loss:", round(loss.item(), 3))""",
"""class GPT(nn.Module):
    def __init__(self, vocab_size, C=64, n_head=4, n_layer=4, block_size=32):
        super().__init__()
        self.block_size = block_size
        self.tok = nn.Embedding(vocab_size, C)
        self.pos = nn.Embedding(block_size, C)
        self.blocks = nn.Sequential(*[Block(C, n_head, block_size) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(C)
        self.head = nn.Linear(C, vocab_size)

    def forward(self, ids, targets=None):
        B, T = ids.shape
        # YOUR CODE HERE: embed (token + position), run blocks, final LN, project to logits
        x = ...
        x = self.blocks(x)
        logits = ...
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

    @torch.no_grad()
    def generate(self, ids, max_new_tokens):
        for _ in range(max_new_tokens):
            ids_cond = ids[:, -self.block_size:]
            logits, _ = self(ids_cond)
            # YOUR CODE HERE: softmax the last step, sample one token, append it
            probs = ...
            next_id = ...
            ids = torch.cat([ids, next_id], dim=1)
        return ids

model = GPT(vocab_size=65).to(device)
print("params:", sum(p.numel() for p in model.parameters()), "trainable")
logits, loss = model(torch.randint(0, 65, (4, 32)).to(device),
                     torch.randint(0, 65, (4, 32)).to(device))
print("logits:", logits.shape, "| loss:", round(loss.item(), 3))"""),
("md", "✅ A complete GPT! It's untrained (random) for now. Next: the training loop."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 12 — Trainer
# ════════════════════════════════════════════════════════════════════════════
emit(12, "trainer", "Trainer — the training loop", [
("md", """## Goal

Train the GPT on Tiny Shakespeare. The loop is the same four steps as any PyTorch model:
`forward → loss → backward → step`, with **AdamW** as the optimizer. We also estimate validation
loss periodically. On CPU this is slow but works; on a Colab T4 GPU it's a couple of minutes."""),
("code", SETUP),
("code", DATA),
("code", """# Tokenizer + data (Chapter 01) and the GPT (Chapter 11), compact + self-contained
chars=sorted(set(text)); vocab_size=len(chars)
stoi={c:i for i,c in enumerate(chars)}; itos={i:c for i,c in enumerate(chars)}
encode=lambda s:[stoi[c] for c in s]; decode=lambda l:"".join(itos[i] for i in l)
data=torch.tensor(encode(text),dtype=torch.long); n=int(0.9*len(data))
train_data,val_data=data[:n],data[n:]
block_size,batch_size=32,32
def get_batch(split):
    d=train_data if split=="train" else val_data
    ix=torch.randint(len(d)-block_size,(batch_size,))
    x=torch.stack([d[i:i+block_size] for i in ix]); y=torch.stack([d[i+1:i+block_size+1] for i in ix])
    return x.to(device),y.to(device)

class Head(nn.Module):
    def __init__(s,C,hs,bs):
        super().__init__(); s.key=nn.Linear(C,hs,bias=False);s.query=nn.Linear(C,hs,bias=False);s.value=nn.Linear(C,hs,bias=False)
        s.register_buffer("tril",torch.tril(torch.ones(bs,bs)));s.scale=hs**-0.5
    def forward(s,x):
        B,T,C=x.shape;k,q,v=s.key(x),s.query(x),s.value(x)
        a=(q@k.transpose(-2,-1)*s.scale).masked_fill(s.tril[:T,:T]==0,float("-inf"));return F.softmax(a,-1)@v
class MHA(nn.Module):
    def __init__(s,C,nh,bs):super().__init__();s.heads=nn.ModuleList([Head(C,C//nh,bs) for _ in range(nh)]);s.proj=nn.Linear(C,C)
    def forward(s,x):return s.proj(torch.cat([h(x) for h in s.heads],-1))
class FF(nn.Module):
    def __init__(s,C):super().__init__();s.net=nn.Sequential(nn.Linear(C,4*C),nn.GELU(),nn.Linear(4*C,C))
    def forward(s,x):return s.net(x)
class Block(nn.Module):
    def __init__(s,C,nh,bs):super().__init__();s.sa=MHA(C,nh,bs);s.ff=FF(C);s.ln1=nn.LayerNorm(C);s.ln2=nn.LayerNorm(C)
    def forward(s,x):x=x+s.sa(s.ln1(x));x=x+s.ff(s.ln2(x));return x
class GPT(nn.Module):
    def __init__(s,vocab_size,C=128,nh=4,nl=4,bs=32):
        super().__init__();s.block_size=bs;s.tok=nn.Embedding(vocab_size,C);s.pos=nn.Embedding(bs,C)
        s.blocks=nn.Sequential(*[Block(C,nh,bs) for _ in range(nl)]);s.ln_f=nn.LayerNorm(C);s.head=nn.Linear(C,vocab_size)
    def forward(s,ids,targets=None):
        B,T=ids.shape;x=s.tok(ids)+s.pos(torch.arange(T,device=ids.device));x=s.blocks(x)
        logits=s.head(s.ln_f(x));loss=None
        if targets is not None: loss=F.cross_entropy(logits.view(-1,logits.size(-1)),targets.view(-1))
        return logits,loss
    @torch.no_grad()
    def generate(s,ids,n):
        for _ in range(n):
            l,_=s(ids[:,-s.block_size:]);p=F.softmax(l[:,-1,:],-1);ids=torch.cat([ids,torch.multinomial(p,1)],1)
        return ids
model=GPT(vocab_size).to(device)
print("params:",sum(p.numel() for p in model.parameters()))"""),
("md", """## The training loop

`max_iters=2000` gives readable output in a few minutes on a T4. Lower it to `500` for a quick test
on CPU. Watch the loss drop from ~4.2 (random) toward ~1.6."""),
("todo",
"""@torch.no_grad()
def estimate_loss(iters=50):
    model.eval(); out={}
    for split in ("train","val"):
        losses=torch.zeros(iters)
        for k in range(iters):
            xb,yb=get_batch(split); _,l=model(xb,yb); losses[k]=l.item()
        out[split]=losses.mean().item()
    model.train(); return out

optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
max_iters = 2000
for it in range(max_iters):
    xb, yb = get_batch("train")
    logits, loss = model(xb, yb)        # forward
    optimizer.zero_grad(set_to_none=True)
    loss.backward()                     # backward
    optimizer.step()                    # update
    if it % 500 == 0 or it == max_iters - 1:
        l = estimate_loss()
        print(f"iter {it:>4}: train {l['train']:.3f} | val {l['val']:.3f}")""",
"""@torch.no_grad()
def estimate_loss(iters=50):
    model.eval(); out={}
    for split in ("train","val"):
        losses=torch.zeros(iters)
        for k in range(iters):
            xb,yb=get_batch(split); _,l=model(xb,yb); losses[k]=l.item()
        out[split]=losses.mean().item()
    model.train(); return out

optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
max_iters = 2000
for it in range(max_iters):
    xb, yb = get_batch("train")
    # YOUR CODE HERE: forward -> zero_grad -> backward -> step  (the 4 lines of training)
    logits, loss = ...
    ...
    ...
    ...
    if it % 500 == 0 or it == max_iters - 1:
        l = estimate_loss()
        print(f"iter {it:>4}: train {l['train']:.3f} | val {l['val']:.3f}")"""),
("md", "✅ Loss is falling — the model is learning Shakespeare. Final chapter: generate text."),
])


# ════════════════════════════════════════════════════════════════════════════
# CHAPTER 13 — Generate
# ════════════════════════════════════════════════════════════════════════════
emit(13, "generate", "Generate — sample text from your model", [
("md", """## Goal

The payoff. Feed the trained model a starting token and let it autoregressively sample new
characters one at a time. Right after training (Chapter 12) run this in the same session so `model`,
`decode`, and `device` are in scope. We also explore **temperature** — the knob that trades coherence
for creativity."""),
("md", """> ℹ️ This chapter assumes you've just run **Chapter 12** and have a trained `model`,
> plus `decode` and `device` in memory. If not, train the model first."""),
("todo",
"""# Greedy-ish sampling from the trained model
start = torch.zeros((1, 1), dtype=torch.long, device=device)   # token 0 as the seed
generated = model.generate(start, max_new_tokens=400)
print(decode(generated[0].tolist()))""",
"""# Greedy-ish sampling from the trained model
start = torch.zeros((1, 1), dtype=torch.long, device=device)
# YOUR CODE HERE: call model.generate(...) for 400 new tokens, then decode the result
generated = ...
print(decode(generated[0].tolist()))"""),
("md", """## Temperature — coherence vs creativity

Divide logits by `T` before softmax. `T<1` sharpens (safer, repetitive); `T>1` flattens (wilder).
This is the single most useful generation knob."""),
("code", """@torch.no_grad()
def generate_temp(model, start, n, temperature=1.0):
    ids = start
    for _ in range(n):
        logits, _ = model(ids[:, -model.block_size:])
        logits = logits[:, -1, :] / temperature
        probs = F.softmax(logits, dim=-1)
        ids = torch.cat([ids, torch.multinomial(probs, 1)], dim=1)
    return ids

for T in (0.5, 1.0, 1.3):
    out = generate_temp(model, torch.zeros((1,1), dtype=torch.long, device=device), 200, T)
    print(f"\\n=== temperature {T} ===")
    print(decode(out[0].tolist()))"""),
("md", """## 🎉 You built and trained an LLM from scratch

You now have, in pure PyTorch and your own hands:
- a tokenizer + dataloader (Ch 01)
- token + position embeddings (Ch 02-04)
- LayerNorm, attention, multi-head attention, feed-forward (Ch 05-08)
- the transformer block and the full GPT (Ch 09-11)
- a training loop and a text sampler (Ch 12-13)

**Where to go next** (see the README roadmap): swap the char tokenizer for **tiktoken/BPE**, scale
the model (more layers/heads/`C`), train longer on a bigger corpus (TinyStories), add **RoPE**
positional encoding, then **instruction-tune** it into a chat model.

For the *production* versions of every idea here — fine-tuning, RAG, alignment, edge deployment,
mechanistic interpretability — see the companion **[Data Science Roadmap](https://github.com/kader-xai/data-science-roadmap)** (Parts 8, 12, 15)."""),
])

print("\\nDONE — all chapters generated.")
