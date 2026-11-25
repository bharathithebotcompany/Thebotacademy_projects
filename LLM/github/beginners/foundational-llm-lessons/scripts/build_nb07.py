import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 07 — Building the Model

## Terms & Definitions
- **Model configuration**: the set of hyperparameters (depth, width, heads, context length, vocab size) that determine a model's size and shape before any training happens.
- **Weight tying**: reusing the same parameter matrix for both the input token embedding and the output projection (`lm_head`) — a common trick to cut parameter count with little to no quality cost.
- **Forward pass**: running input through the model to get output logits (no training yet — no loss, no gradients).

## Sizing `GPTMicro` to ~20M Parameters

Where does a Transformer's parameter count actually come from? For a config with vocabulary size $V$, embedding dimension $d$, context length $T$, and $L$ layers:

| Component | Parameter count |
|---|---|
| Token embedding | $V \\times d$ |
| Positional embedding | $T \\times d$ |
| Per block: attention (QKV + output proj) | $4d^2 + 4d$ |
| Per block: MLP (4x expand + project back) | $8d^2 + 5d$ |
| Per block: 2x LayerNorm | $4d$ |
| Final LayerNorm | $2d$ |
| Output head (`lm_head`) | $0$ if tied to token embedding, else $V \\times d$ |

With **weight tying** (`lm_head.weight = token_emb.weight`, done in `src/model.py`), the output head is free — we don't pay for a second $V \\times d$ matrix. This is exactly what GPT-2 does, and it's why `GPTMicro` uses it too: at small model sizes, the embedding table is a large fraction of total parameters, so tying meaningfully shrinks the model without hurting quality.

We chose: `vocab_size=8000` (from notebook 02's BPE tokenizer), `n_embd=480`, `n_layer=6`, `n_head=8` (so `head_dim = 480/8 = 60`), `block_size=256`. Let's verify this lands near 20M.
"""),
    code("""
import sys
sys.path.insert(0, "..")

from src.model import GPTMicro, GPTConfig
import torch

torch.manual_seed(0)

config = GPTConfig(
    vocab_size=8000,
    block_size=256,
    n_layer=6,
    n_head=8,
    n_embd=480,
    dropout=0.1,
)
model = GPTMicro(config)

total_params = model.num_params()
print(f"Total parameters: {total_params:,}  ({total_params/1e6:.2f}M)")
"""),
    md("""
## Parameter Breakdown

Let's verify the table above matches reality by inspecting the actual named parameters.
"""),
    code("""
from collections import defaultdict

group_totals = defaultdict(int)
for name, p in model.named_parameters():
    if "token_emb" in name:
        group = "token_emb (shared with lm_head via tying)"
    elif "pos_emb" in name:
        group = "pos_emb"
    elif "blocks" in name:
        group = "transformer blocks (all 6 combined)"
    elif "ln_f" in name:
        group = "final layernorm"
    else:
        group = name
    group_totals[group] += p.numel()

for group, count in sorted(group_totals.items(), key=lambda kv: -kv[1]):
    print(f"{group:45s} {count:>10,}  ({count/total_params*100:5.1f}%)")

print(f"\\n{'TOTAL':45s} {total_params:>10,}")
"""),
    md("""
Notice the token embedding table alone is a large share of the total — this is typical for small models with reasonably sized vocabularies; it's precisely why weight tying (not paying for `lm_head` separately) matters more at this scale than it would for a billion-parameter model, where the embedding table is a tiny fraction of the total.

## Forward Pass on Dummy Data

Before training anything, let's just confirm the model runs and produces correctly-shaped output.
"""),
    code("""
batch_size, seq_len = 4, 32
dummy_input = torch.randint(0, config.vocab_size, (batch_size, seq_len))

logits, loss = model(dummy_input)  # no targets passed -> loss is None
print("input shape: ", dummy_input.shape)
print("logits shape:", logits.shape, "-- (batch, seq_len, vocab_size)")
print("loss (no targets given):", loss)
"""),
    code("""
# Now with targets, so we get a real loss value.
dummy_targets = torch.randint(0, config.vocab_size, (batch_size, seq_len))
logits, loss = model(dummy_input, targets=dummy_targets)
print("loss:", loss.item())

import math
print(f"ln(vocab_size) = {math.log(config.vocab_size):.3f}  <- expected loss for an untrained/random model")
"""),
    md("""
An untrained model assigns roughly uniform probability to every token, so its cross-entropy loss should be close to $\\ln(V)$ — confirmed above. Watching this number drop from ~9.0 toward something much smaller is exactly what pretraining (next notebook) looks like.

## Exercise
Try changing `n_layer` from 6 to 4 or 8 in the config above and re-run the parameter count cell — see how much each additional layer costs in parameters, and compare it to changing `n_embd` instead (which affects cost quadratically, since attention/MLP weight matrices scale as $d^2$).

## Summary
- `GPTMicro` (in `src/model.py`) assembles exactly the notebook 06 architecture: embeddings → 6 decoder blocks → final LayerNorm → tied output head.
- Chosen config (`vocab_size=8000, n_embd=480, n_layer=6, n_head=8, block_size=256`) lands at **~20.6M parameters**.
- Weight tying (sharing the embedding and output-projection matrices) is what keeps the model this small given an 8000-token vocabulary.
- A forward pass with random weights produces a loss near $\\ln(\\text{vocab\\_size})$, exactly as expected for an untrained model — our baseline to beat.

Next: **08 — Pretraining Loop** (actually train this model on the *Electricity for Boys* corpus and watch the loss drop).
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "07_building_the_model.ipynb", cells)
