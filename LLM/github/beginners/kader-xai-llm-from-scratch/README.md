# 🧱 LLM From Scratch

> Build a working **GPT language model from scratch** in pure PyTorch — every line, no `transformers`
> library — one component at a time, then train it to generate text. Runs free on Google Colab
> (CPU works; a T4 GPU is faster). Inspired by [nanoGPT](https://github.com/karpathy/nanoGPT) and
> the [EveryonesLLM](https://github.com/HayatoHongo/EveryonesLLM) "build it yourself" format.

Every chapter ships in **two versions**:

- **`todo`** — has `# YOUR CODE HERE` blanks for you to fill in. **Start here.**
- **`answer`** — the complete working code, to check yourself against.

By the end you'll have built — and *understood* — a complete GPT: tokenizer, embeddings, attention,
the transformer block, the training loop, and a text sampler.

[![Open Chapter 00 in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter00_start_todo.ipynb)
&nbsp; *(start here — opens directly in Google Colab, no setup)*

---

## The chapters

Open the **todo** notebook, fill in the blanks, run it. Peek at the **answer** if you're stuck.

| # | Chapter | What you build | todo | answer |
|---|---|---|---|---|
| 00 | **Start Here** | environment + mental model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter00_start_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter00_start_answer.ipynb) |
| 01 | **Dataloader** | char tokenizer + `(x, y)` batches | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter01_dataloader_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter01_dataloader_answer.ipynb) |
| 02 | **Token Embedding** | ids → vectors (lookup table) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter02_token_embedding_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter02_token_embedding_answer.ipynb) |
| 03 | **Position Embedding** | tell the model token order | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter03_position_embedding_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter03_position_embedding_answer.ipynb) |
| 04 | **Embedding Module** | package token + position | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter04_embedding_module_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter04_embedding_module_answer.ipynb) |
| 05 | **LayerNorm** | stabilise activations (from scratch) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter05_layernorm_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter05_layernorm_answer.ipynb) |
| 06 | **Attention Head** | the core "look at other tokens" op | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter06_attention_head_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter06_attention_head_answer.ipynb) |
| 07 | **Multi-Head Attention** | several heads in parallel | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter07_multihead_attention_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter07_multihead_attention_answer.ipynb) |
| 08 | **FeedForward** | the per-token MLP | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter08_feedforward_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter08_feedforward_answer.ipynb) |
| 09 | **Transformer Block** | attention + FFN + residuals (Pre-LN) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter09_transformer_block_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter09_transformer_block_answer.ipynb) |
| 10 | **LM Head** | hidden state → vocabulary logits + loss | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter10_lm_head_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter10_lm_head_answer.ipynb) |
| 11 | **nanoGPT** | assemble the full model + `generate()` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter11_nanogpt_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter11_nanogpt_answer.ipynb) |
| 12 | **Trainer** | the AdamW training loop | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter12_trainer_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter12_trainer_answer.ipynb) |
| 13 | **Generate** | sample text + temperature | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/todo/Chapter13_generate_todo.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kader-xai/llm-from-scratch/blob/main/notebooks/answer/Chapter13_generate_answer.ipynb) |

> ✅ Verified end-to-end: training drops the loss from **4.21 (random) → ~1.6** and the model
> generates Shakespeare-shaped text. The full run is a couple of minutes on a Colab T4 GPU.

---

## The tensor map (keep this in your head)

A transformer is a tensor-reshaping pipeline. Knowing the shape at every step is most of the battle.

```
ids        (B, T)            integer token ids                    ← Ch 01
tok+pos    (B, T, C)         each token → C-dim vector            ← Ch 02-04
           │
   ┌───────┴── repeat N transformer blocks (shape preserved) ──────┐   ← Ch 05-09
   │  x = x + MultiHeadAttention(LayerNorm(x))                      │
   │  x = x + FeedForward(LayerNorm(x))                             │
   └───────┬───────────────────────────────────────────────────────┘
           │
ln + head  (B, T, vocab)     next-token logits                    ← Ch 10
           │
softmax    (B, T, vocab)     probabilities → sample               ← Ch 13
```

- **B** = batch size · **T** = context length · **C** = embedding dim · **vocab** = number of tokens.

See [`docs/tensor_map.md`](docs/tensor_map.md) for the full shape table.

---

## How to use it

**On Google Colab (recommended — zero setup):** click any **todo** badge link above. The first
cell installs nothing (Colab ships PyTorch) and downloads the ~1 MB Tiny Shakespeare corpus.

**On your own machine:**

```bash
git clone https://github.com/kader-xai/llm-from-scratch
cd llm-from-scratch
pip install -r requirements.txt
jupyter lab    # open notebooks/todo/Chapter00_start_todo.ipynb
```

Work the chapters **in order** — each builds on the last. Chapters 01-11 are quick (5-30 min each);
Chapter 12 trains the model (minutes on GPU, longer on CPU); Chapter 13 is the payoff.

---

## What you'll understand at the end

- **Tokenization** — why text becomes integers, and the cost of character vs subword (BPE) vocab.
- **Embeddings** — token vectors *and* position vectors, and why attention needs both.
- **Attention** — query/key/value, scaled dot-product, causal masking, multi-head — implemented by hand.
- **The transformer block** — residual connections and Pre-LayerNorm, and *why* they make depth trainable.
- **Training** — cross-entropy loss, AdamW, train/val splits, and reading a loss curve.
- **Generation** — autoregressive sampling and the temperature knob.

---

## Where to go next

This series stops at a trained char-level GPT. The natural extensions (and where to learn them):

| Next step | What changes |
|---|---|
| **Subword tokenizer** | swap the char tokenizer for **tiktoken / BPE** → fewer tokens, real words |
| **Scale up** | more layers / heads / `C`, bigger corpus (TinyStories, OpenWebText) |
| **RoPE** | replace learned position embedding with **rotary** encoding → length generalization |
| **Instruction tuning** | fine-tune the pretrained model on `(instruction, response)` pairs → a chat model |
| **Alignment** | DPO / Constitutional AI to make it helpful + harmless |

For the **production** version of every one of these — fine-tuning, RAG, agents, alignment, edge
deployment, and mechanistic interpretability — see the companion
**[Data Science Roadmap](https://github.com/kader-xai/data-science-roadmap)** (Parts 8, 12, 14, 15).

---

## Credits & license

Inspired by Andrej Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT) /
[minGPT](https://github.com/karpathy/minGPT) and Hayato Hongo's
[EveryonesLLM](https://github.com/HayatoHongo/EveryonesLLM) chapter-by-chapter "build it yourself"
format. Training corpus: Tiny Shakespeare. Released under the **MIT License**.
