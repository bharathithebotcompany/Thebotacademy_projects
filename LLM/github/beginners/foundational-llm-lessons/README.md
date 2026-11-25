# LLM Lessons

A hands-on, self-contained curriculum for learning how large language models actually work — by building and training a real one, end to end, on your own machine.

You'll build a ~20M-parameter GPT-style Transformer from scratch, then take it through the same pipeline every modern LLM assistant goes through: **pretraining → continued pretraining (CPT) → supervised fine-tuning (SFT) → reward modeling → reinforcement learning (RLHF/PPO)**.

The model is intentionally small (~20M parameters, vs. billions in production LLMs) so that:
- Every stage trains in minutes on a **CPU** — no GPU required.
- You can re-run cells, change hyperparameters, and see the effect immediately.
- The whole pipeline stays inspectable — small enough to reason about, not a black box.

Each notebook mixes **terms & definitions, history, concept explanations, light math, and runnable code** — written for a complete beginner to language models.

## Getting Started

```bash
pip install -r requirements.txt
python scripts/prepare_corpus.py              # downloads and cleans the training text
python scripts/generate_instruction_data.py    # generates toy instruction + preference data
jupyter lab
```

Then open `environment_check.ipynb` first to confirm everything is working, and proceed through the notebooks in order.

## Curriculum

| # | Notebook | Covers |
|---|---|---|
| — | `environment_check.ipynb` | Confirm your Python/PyTorch/Jupyter setup works |
| 00 | `00_environment_and_python_refresher.ipynb` | Tensors, `nn.Module`, autograd, the training loop pattern |
| 01 | `01_what_is_a_language_model.ipynb` | History (n-grams → RNNs → Transformers), next-token prediction, a toy bigram model |
| 02 | `02_tokenization.ipynb` | Char/word/subword tokenization, training a real BPE tokenizer |
| 03 | `03_embeddings.ipynb` | Token & positional embeddings, visualizing embedding space |
| 04 | `04_neural_network_foundations.ipynb` | Linear layers, activations, LayerNorm, residual connections, softmax, cross-entropy |
| 05 | `05_attention_mechanism.ipynb` | Scaled dot-product attention, causal masking, multi-head attention, from scratch |
| 06 | `06_transformer_architecture.ipynb` | Assembling a decoder block, stacking blocks, decoder-only vs. encoder-only |
| 07 | `07_building_the_model.ipynb` | The real `GPTMicro` model, sized to ~20M parameters, param-count breakdown |
| 08 | `08_pretraining_loop.ipynb` | The real training loop: LR schedule, gradient clipping, checkpointing — actually pretrain the model |
| 09 | `09_evaluating_and_sampling.ipynb` | Perplexity, greedy/sampling/top-k decoding, temperature |
| 10 | `10_continued_pretraining_cpt.ipynb` | Domain-adapting the pretrained model via CPT |
| 11 | `11_supervised_fine_tuning_sft.ipynb` | Instruction/response format, prompt masking, SFT |
| 12 | `12_reward_modeling.ipynb` | Preference pairs, Bradley-Terry loss, training a reward model |
| 13 | `13_reinforcement_learning_ppo.ipynb` | RLHF: PPO, KL penalty, a minimal but complete RL fine-tuning loop |
| 14 | `14_putting_it_all_together.ipynb` | Full pipeline recap, side-by-side generation comparison, further reading |

## Repo Layout

```
src/            shared, reusable code (model, data loading, training helpers)
data/           training corpus + generated instruction/preference datasets
notebooks/      the curriculum, in order
scripts/        one-off data-prep scripts + notebook-generation scripts (not part of the lessons)
checkpoints/    trained model weights land here (gitignored)
```

## Training Corpus

Raw-text pretraining uses **_Electricity for Boys_ by James Slough Zerbe** (Project Gutenberg #22766, public domain, 1914) — an early-1900s expository text teaching electrical concepts through hands-on experiments. Chosen instead of the more common Tiny Shakespeare corpus for a different flavor (technical/instructional prose) and because its plainer sentence structure suits a small model well.

The instruction-tuning and preference data (`data/instruction_data.jsonl`, `data/preference_pairs.jsonl`) are programmatically generated toy tasks — arithmetic, string formatting, and simple Q&A about the corpus — not scraped from anywhere.

## A Note on Scale

This is a teaching tool, not a production system. At ~20M parameters trained on one small book, expect the model to learn real English structure (spelling, local grammar, some vocabulary from the source text) but not long-range coherence, factual reliability, or real reasoning. That's the correct, expected outcome — the goal is understanding the *mechanism* every stage uses, which is identical in shape to what powers billion-parameter production LLMs.
