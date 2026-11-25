import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 02 — Tokenization

## Terms & Definitions
- **Tokenization**: the process of splitting raw text into discrete units (tokens) a model can consume.
- **Vocabulary**: the fixed set of all possible tokens a model knows about.
- **Token ID**: the integer index of a token in the vocabulary — this is what actually gets fed into the model, not text.
- **Character-level tokenization**: each token is a single character.
- **Word-level tokenization**: each token is a whole word.
- **Subword tokenization (BPE)**: tokens are variable-length chunks — common words become a single token, rare/unknown words get split into smaller pieces.
- **BPE (Byte-Pair Encoding)**: an algorithm that builds a subword vocabulary by iteratively merging the most frequent adjacent pair of symbols.

## Why Tokenize at All?
Neural networks operate on numbers, not text. Somehow we need to turn `"Hello, world!"` into a sequence of integers, run the model, and turn integers back into text. Tokenization is that translation layer, and *how* you tokenize has real consequences:

| Scheme | Vocab size | Sequence length | Handles unseen words? |
|---|---|---|---|
| Character-level | Tiny (~100) | Very long | Yes (always, one char at a time) |
| Word-level | Huge (~100K+) | Short | No (unknown word = `<unk>`) |
| Subword (BPE) | Medium (~10K-100K) | Medium | Yes (falls back to smaller pieces) |

Modern LLMs (GPT, Claude, Llama) all use subword tokenization (usually BPE or a variant) because it gets the best of both worlds: common words are single efficient tokens, and rare/novel words/typos still get encoded losslessly by falling back to smaller pieces.

## History
BPE itself is an old **data compression** algorithm (Philip Gage, 1994) — nothing to do with language modeling originally. It was repurposed for neural machine translation tokenization in 2015 (Sennrich et al.) and became the standard approach once GPT-2 (2019) popularized *byte-level* BPE (operating on raw UTF-8 bytes so literally any string, including emoji or malformed text, can always be encoded).
"""),
    code("""
import sys
sys.path.insert(0, "..")

from src.data import load_electricity_for_boys

text = load_electricity_for_boys()
print(f"Corpus: {len(text):,} characters, {len(text.split()):,} words")
print()
print(text[:300])
"""),
    md("""
## Character-Level Tokenization

The simplest possible scheme: every unique character is a token.
"""),
    code("""
chars = sorted(set(text))
print(f"vocabulary size (unique characters): {len(chars)}")
print("".join(chars))
"""),
    code("""
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

def char_encode(s):
    return [stoi[c] for c in s]

def char_decode(ids):
    return "".join(itos[i] for i in ids)

sample = "Electricity is useful."
ids = char_encode(sample)
print("text:", sample)
print("ids: ", ids)
print("round-trip:", char_decode(ids))
"""),
    md("""
Notice how many tokens a short sentence needs at the character level — every letter and space is its own token. That means longer sequences for the same amount of text, which is more compute per sentence. This is the tradeoff subword tokenization improves on.

## Subword Tokenization (BPE)

Now let's train a real byte-level BPE tokenizer (the same family of algorithm GPT-2/GPT-3 use) on our corpus, using the `tokenizers` library.
"""),
    code("""
from src.data import train_bpe_tokenizer

tokenizer = train_bpe_tokenizer(text, vocab_size=8000)
print(f"trained vocab size: {tokenizer.get_vocab_size()}")
"""),
    code("""
sample = "Electricity is useful."
enc = tokenizer.encode(sample)

print("text:      ", sample)
print("token ids: ", enc.ids)
print("num tokens:", len(enc.ids))
print("tokens:    ", enc.tokens)
print("decoded:   ", tokenizer.decode(enc.ids))
"""),
    md("""
Compare `len(enc.ids)` (BPE) to `len(char_encode(sample))` (char-level) for the same sentence — BPE needs noticeably fewer tokens to represent the same text, because common substrings ("electricity", " is", " useful") became single tokens during training.

## Vocabulary Size Is a Design Choice

There's a real tradeoff in choosing `vocab_size`:
- **Smaller vocab** → smaller embedding table (fewer parameters spent there) but longer token sequences for the same text (more compute per sentence, and the model has to compose meaning from more pieces).
- **Larger vocab** → shorter sequences, but a bigger (and slower to train) embedding table, and rarer tokens get less training signal each.

We picked **8000** for this curriculum specifically to keep the ~20M parameter model's embedding table a reasonable fraction of its total size (see notebook 07 for the exact parameter breakdown) while still letting BPE capture common word chunks in our small corpus.

## Exercise
Try encoding a sentence with words *not* in the training corpus, e.g. `"Quantum computers use qubits."` Notice that even with rare/unseen words, BPE still successfully encodes and decodes them (unlike a pure word-level vocabulary, which would need an `<unk>` fallback) — it just uses more, smaller tokens for the unfamiliar parts.
"""),
    code("""
novel_sentence = "Quantum computers use qubits."
enc = tokenizer.encode(novel_sentence)
print("tokens:", enc.tokens)
print("decoded:", tokenizer.decode(enc.ids))
"""),
    md("""
## Summary
- Tokenization converts text <-> integers; the scheme you choose trades off vocabulary size against sequence length.
- Character-level: tiny vocab, long sequences, always works.
- Word-level: huge vocab, short sequences, breaks on unseen words.
- Subword/BPE: the practical middle ground every modern LLM uses.
- We trained a real BPE tokenizer (vocab_size=8000) on our corpus — this exact tokenizer (`src/data.py: train_bpe_tokenizer`) is reused starting in notebook 08 for pretraining.

Next: **03 — Embeddings** (token IDs are just arbitrary integers — embeddings are how the model turns them into meaningful vectors).
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "02_tokenization.ipynb", cells)
