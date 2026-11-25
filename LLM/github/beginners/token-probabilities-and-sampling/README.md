# Token Probabilities Workshop

A hands-on workshop demonstrating how Large Language Models assign token probabilities — from raw logits to sampling strategies to practical applications like hallucination detection.

**Format:** 1-hour instructor-led demo (screen-shared Jupyter notebooks)
**Audience:** ML practitioners with strong Python skills

## Workshop Notebooks

The workshop is structured as 5 sequential notebooks, each building on concepts from the previous one.

| # | Notebook | ~Duration | Topics |
|---|----------|-----------|--------|
| 01 | `01_logits_and_softmax.ipynb` | 10 min | Logits, softmax (step-by-step), temperature scaling, log-probabilities, real vocabulary sizes |
| 02 | `02_tokenization_and_next_token.ipynb` | 12 min | BPE tokenization, GPT-2 forward pass, next-token prediction, per-position analysis |
| 03 | `03_sampling_strategies.ipynb` | 12 min | Greedy decoding, random sampling, top-k, top-p (nucleus), combined strategies |
| 04 | `04_autoregressive_generation.ipynb` | 12 min | Traced generation, decision tree visualization, KV cache optimization, sequence scoring |
| 05 | `05_practical_applications.ipynb` | 12 min | Perplexity, confidence heatmaps, uncertainty detection, completion ranking |

### Notebook Details

**Notebook 01 — Logits, Softmax, and Temperature** uses pure PyTorch (no model) to build intuition for the math that converts raw model outputs into probabilities. Covers softmax step-by-step, temperature's effect on distribution shape, log-probabilities for numerical stability, and how probability mass concentrates in real vocabulary sizes (50K+ tokens).

**Notebook 02 — Tokenization and Next-Token Prediction** loads GPT-2 and walks through the full pipeline: text → BPE tokens → forward pass → logits → probabilities. Demonstrates how the model predicts the next token at every position and how confidence varies between factual and open-ended prompts.

**Notebook 03 — Sampling Strategies** implements each strategy from scratch: greedy (argmax), pure random, top-k, and top-p (nucleus). Includes a side-by-side visual comparison showing how each reshapes the probability distribution, then demonstrates how strategies combine (temperature + top-p) — the way production LLM APIs actually work.

**Notebook 04 — Autoregressive Generation** traces generation step-by-step, recording the probability, entropy, and top alternatives at each token. Visualizes the "branching tree" of possibilities, demonstrates the KV cache speedup, and shows how to score existing text by measuring the probability the model assigns to each token.

**Notebook 05 — Practical Applications** applies token probabilities to real-world tasks: computing perplexity across different text types, building confidence heatmaps that color-code tokens by probability, detecting uncertainty in true vs. false statements, and ranking alternative completions by sequence probability.

## Setup

### Prerequisites

- Python 3.11+
- ~1 GB disk space (for GPT-2 model weights and dependencies)

### Installation

```bash
git clone <repo-url>
cd token-probabilities
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

GPT-2 (124M parameters, ~500 MB) downloads automatically on first run of Notebook 02.

### Running the Workshop

```bash
source .venv/bin/activate
jupyter notebook
```

Open notebooks in order: `01` → `02` → `03` → `04` → `05`. Each notebook is self-contained (re-imports and re-loads the model) so they can also be run independently.

## Technical Notes

### Why GPT-2?

All notebooks use **GPT-2** (124M params) via HuggingFace Transformers. This is deliberate:

- **Full internal access** — we get raw logit tensors, not just API responses
- **Fast on CPU/MPS** — no GPU required, runs well on a MacBook for live demos
- **Small download** — ~500 MB vs. multi-GB for larger models
- **Same architecture** — the logit → softmax → sampling pipeline is identical in GPT-4, Claude, Llama, etc. Only the quality of predictions differs.

### Key Concepts Covered

| Concept | Notebook | Description |
|---------|----------|-------------|
| Logits | 01 | Raw, unnormalized scores from the model's final layer |
| Softmax | 01 | Converting logits to a valid probability distribution |
| Temperature | 01, 03 | Controlling distribution sharpness (creativity vs. consistency) |
| Log-probabilities | 01, 04 | Numerically stable representation for sequence scoring |
| BPE Tokenization | 02 | How text becomes token IDs the model can process |
| Next-token prediction | 02 | The core operation: predict one token given all previous tokens |
| Greedy decoding | 03 | Always pick the highest-probability token |
| Top-k sampling | 03 | Sample from only the k most probable tokens |
| Top-p (nucleus) sampling | 03 | Adaptive sampling based on cumulative probability threshold |
| Autoregressive generation | 04 | Chaining single-token predictions into full text |
| KV cache | 04 | Optimization that avoids redundant computation during generation |
| Perplexity | 05 | Measuring how "surprised" a model is by text |
| Confidence estimation | 05 | Using token probabilities to gauge output reliability |
| Uncertainty detection | 05 | Flagging low-confidence tokens as potential hallucinations |

## Project Structure

```
token-probabilities/
├── 01_logits_and_softmax.ipynb         # Pure PyTorch — the math
├── 02_tokenization_and_next_token.ipynb # GPT-2 — the full pipeline
├── 03_sampling_strategies.ipynb         # GPT-2 — choosing tokens
├── 04_autoregressive_generation.ipynb   # GPT-2 — generating text
├── 05_practical_applications.ipynb      # GPT-2 — real-world uses
├── requirements.txt                     # Pinned dependencies
├── README.md
└── STATUS.md
```
