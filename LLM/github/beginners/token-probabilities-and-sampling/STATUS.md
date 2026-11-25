# Status

## Current State: Complete

All 5 workshop notebooks are built and validated.

## What Was Completed

- **01_logits_and_softmax.ipynb** — Logits, softmax step-by-step, temperature scaling, log-probs, realistic vocab sizes
- **02_tokenization_and_next_token.ipynb** — BPE tokenization, GPT-2 forward pass, next-token predictions, per-position analysis
- **03_sampling_strategies.ipynb** — Greedy, random, top-k, top-p (nucleus), combined strategies with side-by-side visualization
- **04_autoregressive_generation.ipynb** — Step-by-step traced generation, decision tree visualization, KV cache speedup demo, sequence scoring
- **05_practical_applications.ipynb** — Perplexity comparison, confidence heatmaps, uncertainty/hallucination detection, completion ranking
- **requirements.txt** — Pinned dependencies
- **README.md** — Setup instructions and notebook overview
- **.gitignore** — Standard Python/Jupyter ignores

## Known Issues

- Ollama (v0.20.2) does not return logprobs via its API, so Notebook 05 was redesigned to use GPT-2 via HuggingFace Transformers instead. All probability-based analysis uses direct logit access.
- GPT-2 is a small (124M param) model — predictions are reasonable but not state-of-the-art. This is by design: it runs fast on CPU/MPS and provides full internal access for teaching.

## What's Left

- Run through all notebooks end-to-end in Jupyter before the workshop to confirm all visualizations render properly
- Consider adding Ollama back if a future version supports logprobs (would be Notebook 06)
