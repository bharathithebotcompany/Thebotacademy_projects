import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 01 — What Is a Language Model

## Terms & Definitions
- **Language model**: a system that assigns a probability to sequences of text, or equivalently, predicts the next token given the tokens before it.
- **Corpus**: the body of text a model is trained on.
- **Token**: the basic unit a model reads/writes — could be a character, a word piece, or a whole word (notebook 02 covers this in depth).
- **Autoregressive**: generating output one token at a time, where each new token is conditioned on everything generated so far.
- **Context window**: the maximum number of preceding tokens the model can "see" when predicting the next one.
- **Parameters**: the model's learnable numbers (weights and biases) — what training actually adjusts.
- **Inference**: running a trained model to produce output (as opposed to training it).
- **Perplexity**: a measure of how "surprised" a model is by real text — lower is better (covered in depth in notebook 09).

## A Brief History
- **1948 — Shannon's information theory**: Claude Shannon modeled English text with simple statistical models (n-grams) and measured how predictable language is — arguably the conceptual ancestor of language modeling.
- **1980s–2000s — N-gram models**: count how often each word follows the previous *N-1* words in a corpus, and use those frequencies as probabilities. Simple, fast, but can't capture long-range structure and the counts table explodes in size as *N* grows.
- **2000s–2010s — Neural language models**: replace lookup tables with neural networks (initially small feedforward nets, then **RNNs** and **LSTMs**) that compress context into a fixed-size hidden state. Better at generalizing, but still struggle with long sequences (state gets "forgotten") and are slow to train (must process tokens one-by-one, in order).
- **2017 — "Attention Is All You Need"**: the Transformer architecture replaces recurrence with *attention* (notebook 05), letting the model look directly at any earlier token and process a whole sequence in parallel. This is the architecture every modern LLM (GPT, Claude, Llama, Gemini, ...) is built on.
- **2018–present — Scaling up**: GPT, GPT-2, GPT-3, GPT-4, Claude, Llama, Gemini... same core Transformer idea, scaled to billions/trillions of parameters and trained on huge web-scale corpora, with additional stages (CPT, SFT, RLHF — notebooks 10–13) added on top of raw next-token pretraining to make them follow instructions and behave helpfully.

**Where this curriculum sits**: we're building a real, working member of this same GPT lineage — just at ~20M parameters instead of billions, trained on one small book instead of the internet. The mechanics are identical; only the scale differs.

## The Core Idea: Next-Token Prediction
Almost every modern LLM is trained on one deceptively simple objective: **given some text, predict the next token.**

That's it. There's no explicit "answer questions" or "be helpful" objective during pretraining — those behaviors emerge later (SFT, RLHF). Predicting the next token accurately, over and over, on enough text, turns out to require the model to implicitly learn grammar, facts, reasoning patterns, and style.

## Applicability
Every stage of this curriculum builds on this same idea:
- **Pretraining** (08): learn to predict the next token on raw text.
- **CPT** (10): keep predicting the next token, but on a new/adjacent corpus, to shift the model's "style".
- **SFT** (11): predict the next token, but only in the *response* portion of instruction/response pairs.
- **RLHF** (12–13): after SFT, use a reward model to reshape which *sequences* of tokens the model prefers to generate.

Let's build intuition for next-token prediction using the simplest possible language model: an **n-gram model**.
"""),
    code("""
import re
from collections import defaultdict, Counter
import random

random.seed(0)
"""),
    md("""
## A Toy Bigram Model

A **bigram** model predicts the next word using only the *single* preceding word: it counts, for every word, what tends to come after it in the training corpus. This is exactly the "count how often each word follows the previous word" idea from 1980s-era n-gram models — no neural network at all yet.
"""),
    code("""
toy_corpus = (
    "the cat sat on the mat . the cat likes the mat . "
    "the dog sat on the rug . the dog likes the rug . "
    "the cat and the dog sat on the mat ."
)

words = toy_corpus.split()
print(f"corpus has {len(words)} words, vocabulary of {len(set(words))} unique words")

# Count: for each word, what words follow it, and how often.
bigram_counts = defaultdict(Counter)
for w1, w2 in zip(words[:-1], words[1:]):
    bigram_counts[w1][w2] += 1

print()
print("What follows 'the'?")
for word, count in bigram_counts["the"].most_common():
    print(f"  {word!r}: {count} times")
"""),
    code("""
def bigram_predict_next(word, bigram_counts):
    \"\"\"Sample the next word proportionally to how often it followed `word`
    in the training corpus -- the model's entire 'prediction' mechanism.\"\"\"
    choices = bigram_counts[word]
    if not choices:
        return random.choice(words)
    population, weights = zip(*choices.items())
    return random.choices(population, weights=weights, k=1)[0]


def generate(start_word, n_words, bigram_counts):
    current = start_word
    output = [current]
    for _ in range(n_words):
        current = bigram_predict_next(current, bigram_counts)
        output.append(current)
    return " ".join(output)

for _ in range(3):
    print(generate("the", 12, bigram_counts))
"""),
    md("""
Notice the output is locally coherent (word pairs that appeared together in training show up again) but has no real long-range structure — a bigram model has no memory beyond the single previous word. This is exactly the limitation that motivated RNNs, then Transformers: **more context needs to inform each prediction.**

## Exercise
Try changing `bigram_predict_next` to look at the *previous two words* instead of one (a **trigram** model) using a `(w1, w2) -> next_word` counts table. You'll likely need much more training text before it generates anything coherent — this is the "n-gram counts explode" problem mentioned above: with a vocabulary of size *V*, a bigram table has up to *V²* entries, but a trigram table has up to *V³*.

## Summary
- A language model predicts the next token given previous tokens — everything else is built on this.
- N-gram models (bigram/trigram) are the simplest possible version: just counting frequencies.
- They break down because they can't use long-range context and their tables grow explosively with more context — the exact problem attention (notebook 05) solves elegantly.
- Real LLMs use the same "predict the next token" objective, just with a vastly more powerful predictor (a Transformer) instead of a counts table.

Next: **02 — Tokenization** (before we can predict "the next token," we need to define what a token even is).
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "01_what_is_a_language_model.ipynb", cells)
