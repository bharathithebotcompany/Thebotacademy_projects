import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 09 — Evaluating and Sampling

## Terms & Definitions
- **Perplexity**: $e^{\\text{loss}}$ (exponentiated cross-entropy loss) — intuitively, "how many roughly-equally-likely choices was the model deciding between, on average, at each step?" Lower is better; perplexity 1 would mean perfect, certain predictions.
- **Greedy decoding**: always pick the single highest-probability next token.
- **Sampling (temperature sampling)**: draw the next token randomly from the model's predicted probability distribution, optionally reshaped by a temperature parameter.
- **Temperature**: a scalar that reshapes the probability distribution before sampling — low temperature (< 1) sharpens it (more confident/repetitive), high temperature (> 1) flattens it (more random/diverse).
- **Top-k sampling**: restrict sampling to only the *k* highest-probability tokens (zero out the rest), then sample — avoids the model occasionally picking a wildly unlikely token.
- **Top-p (nucleus) sampling**: restrict sampling to the smallest set of tokens whose cumulative probability exceeds *p*, then sample — adapts the candidate pool size per-step rather than fixing it at *k*.

## Why Not Always Use Greedy Decoding?
Greedy decoding is deterministic and simple, but tends to produce repetitive, dull text — once a model gets into a locally-likely loop (e.g. "the the the..."), greedy has no mechanism to escape it, since it always doubles down on the single best next token. Sampling introduces controlled randomness so generation can explore lower-probability-but-still-reasonable continuations, at the cost of occasional weirdness. Top-k/top-p exist to keep that randomness from picking truly bad tokens.

## The Math (light)

**Perplexity**: if $L$ is the average cross-entropy loss (in nats, i.e. using natural log) over a dataset,
$$\\text{PPL} = e^{L}$$
A model with loss $\\ln(8000) \\approx 8.99$ (our untrained baseline from notebook 07) has perplexity $8000$ — as bad as guessing uniformly at random among all 8000 vocabulary tokens. A well-trained model on a narrow corpus can get perplexity down to single or low double digits.

**Temperature sampling**: divide logits by temperature $T$ before softmax:
$$p_i = \\text{softmax}(z_i / T)$$
As $T \\to 0$, this approaches greedy (all probability mass on the argmax); as $T \\to \\infty$, it approaches uniform random sampling over the vocabulary.
"""),
    code("""
import sys
sys.path.insert(0, "..")

import math
import torch
import torch.nn.functional as F

from src.model import GPTMicro, GPTConfig
from src.data import load_electricity_for_boys, train_bpe_tokenizer, encode_corpus_to_tensor, get_batch, get_train_val_split
from src.train_utils import load_checkpoint

torch.set_num_threads(6)
torch.manual_seed(0)

text = load_electricity_for_boys()
tokenizer = train_bpe_tokenizer(text, vocab_size=8000)
data = encode_corpus_to_tensor(text, tokenizer)
_, val_data = get_train_val_split(data, val_fraction=0.1)

config = GPTConfig(vocab_size=8000, block_size=128, n_layer=6, n_head=8, n_embd=480, dropout=0.1)
model = GPTMicro(config)
load_checkpoint(model, "pretrained_electricity", device="cpu")
model.eval()
print("Loaded pretrained checkpoint.")
"""),
    md("""
## Perplexity on Held-Out Data

We measure loss on the *validation* split (text the model never trained on) — this tells us how well the model generalizes, rather than how well it memorized the training text.
"""),
    code("""
@torch.no_grad()
def compute_val_loss(model, data, block_size, batch_size, device, n_batches=20):
    losses = []
    for _ in range(n_batches):
        x, y = get_batch(data, block_size, batch_size, device)
        _, loss = model(x, targets=y)
        losses.append(loss.item())
    return sum(losses) / len(losses)

val_loss = compute_val_loss(model, val_data, config.block_size, batch_size=16, device="cpu")
val_perplexity = math.exp(val_loss)
print(f"validation loss:       {val_loss:.3f}")
print(f"validation perplexity: {val_perplexity:.1f}")
print(f"(untrained baseline was ~8000 perplexity, i.e. uniform random guessing over the vocab)")
"""),
    md("""
## Greedy vs. Sampling vs. Top-k Decoding

Let's generate text from the same prompt using different decoding strategies and compare.
"""),
    code("""
def encode_prompt(prompt, tokenizer):
    return torch.tensor([tokenizer.encode(prompt).ids], dtype=torch.long)

prompt = "Electricity is"
context = encode_prompt(prompt, tokenizer)
print("prompt token ids:", context)
"""),
    code("""
torch.manual_seed(42)

# Greedy: temperature doesn't matter if we always take argmax, so we simulate
# greedy with an extremely low temperature and top_k=1.
greedy_out = model.generate(context, max_new_tokens=40, temperature=1.0, top_k=1)
print("GREEDY (top_k=1):")
print(tokenizer.decode(greedy_out[0].tolist()))
print()

sampled_out = model.generate(context, max_new_tokens=40, temperature=1.0, top_k=None)
print("SAMPLING (temperature=1.0, no top_k):")
print(tokenizer.decode(sampled_out[0].tolist()))
"""),
    code("""
torch.manual_seed(42)
low_temp = model.generate(context, max_new_tokens=40, temperature=0.5, top_k=None)
print("LOW TEMPERATURE (0.5) -- more conservative/repetitive:")
print(tokenizer.decode(low_temp[0].tolist()))
print()

torch.manual_seed(42)
high_temp = model.generate(context, max_new_tokens=40, temperature=1.3, top_k=None)
print("HIGH TEMPERATURE (1.3) -- more random/diverse:")
print(tokenizer.decode(high_temp[0].tolist()))
print()

torch.manual_seed(42)
top_k_out = model.generate(context, max_new_tokens=40, temperature=1.0, top_k=20)
print("TOP-K (k=20) -- balances diversity with avoiding very unlikely tokens:")
print(tokenizer.decode(top_k_out[0].tolist()))
"""),
    md("""
## Setting Expectations for a 20M-Parameter Model

Compare this generated text to what you'd get from a modern billion-parameter LLM. At ~20M parameters trained on one ~227KB book, expect:
- Mostly correct spelling and local grammar (the model has clearly learned English word/character structure).
- Some real phrases and sentence fragments echoing the training text.
- **Not** long-range coherence, factual reliability, or real "reasoning" — the model is far too small and the corpus far too small for that.

This is the expected and correct outcome at this scale — the point of this curriculum is to understand *how* the mechanism works, not to build a production-quality chatbot. Every stage from here (CPT, SFT, RLHF) will visibly change this same generation behavior in characteristic ways, which is easiest to notice precisely because the model is small enough to run and inspect quickly.

## Exercise
Try a few different prompts (e.g. `"The battery"`, `"A boy who"`) and compare greedy vs. sampled output. Notice greedy decoding is far more likely to repeat itself or get stuck in short loops, especially past ~30-40 tokens.

## Summary
- Perplexity ($e^{\\text{loss}}$) is the standard way to summarize how well a language model predicts held-out text — we should see a large drop from the ~8000 untrained baseline.
- Greedy decoding is deterministic but repetitive; sampling introduces controlled randomness; temperature and top-k/top-p shape how much randomness and how it's constrained.
- At 20M parameters / ~227KB of training text, expect locally fluent but not globally coherent generations — this is the correct, expected result at this scale.

Next: **10 — Continued Pretraining (CPT)** (adapting this same pretrained model toward a new, more targeted domain of text before we move to instruction-following).
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "09_evaluating_and_sampling.ipynb", cells)
