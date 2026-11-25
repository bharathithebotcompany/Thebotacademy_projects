"""Data loading and tokenization helpers shared across notebooks 02, 08, 10, 11, 12."""

import json
import random
from pathlib import Path

import torch
from tokenizers import Tokenizer, models, pre_tokenizers, trainers, decoders

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TOKENIZER_PATH = DATA_DIR / "tokenizer.json"


def load_electricity_for_boys() -> str:
    """Load the raw text corpus: 'Electricity for Boys' by J.S. Zerbe
    (Project Gutenberg #22766, public domain)."""
    path = DATA_DIR / "electricity_for_boys.txt"
    return path.read_text(encoding="utf-8")


def train_bpe_tokenizer(text: str, vocab_size: int = 8000, save_path: Path = TOKENIZER_PATH) -> Tokenizer:
    """Train a byte-level BPE tokenizer on the given text (see notebook 02)."""
    tokenizer = Tokenizer(models.BPE(unk_token="<unk>"))
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tokenizer.decoder = decoders.ByteLevel()

    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=["<pad>", "<unk>", "<bos>", "<eos>"],
    )
    tokenizer.train_from_iterator([text], trainer=trainer)

    save_path.parent.mkdir(parents=True, exist_ok=True)
    tokenizer.save(str(save_path))
    return tokenizer


def load_tokenizer(path: Path = TOKENIZER_PATH) -> Tokenizer:
    return Tokenizer.from_file(str(path))


def encode_corpus_to_tensor(text: str, tokenizer: Tokenizer) -> torch.Tensor:
    ids = tokenizer.encode(text).ids
    return torch.tensor(ids, dtype=torch.long)


def get_train_val_split(data: torch.Tensor, val_fraction: float = 0.1):
    n = int(len(data) * (1 - val_fraction))
    return data[:n], data[n:]


def get_batch(data: torch.Tensor, block_size: int, batch_size: int, device: str = "cpu"):
    """Sample a random batch of (input, target) sequences for language-model
    pretraining, where target is input shifted by one token."""
    ix = torch.randint(len(data) - block_size - 1, (batch_size,))
    x = torch.stack([data[i : i + block_size] for i in ix])
    y = torch.stack([data[i + 1 : i + 1 + block_size] for i in ix])
    return x.to(device), y.to(device)


class InstructionDataset(torch.utils.data.Dataset):
    """Loads (instruction, response) pairs from a JSONL file and formats them as
    a single prompt string with a clear separator, masking the loss on the
    instruction portion so the model only learns to predict the response
    (see notebook 11 on prompt masking)."""

    PROMPT_TEMPLATE = "### Instruction:\n{instruction}\n### Response:\n"

    def __init__(self, jsonl_path: Path, tokenizer: Tokenizer, block_size: int):
        self.examples = [json.loads(line) for line in Path(jsonl_path).read_text().splitlines() if line.strip()]
        self.tokenizer = tokenizer
        self.block_size = block_size

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        ex = self.examples[idx]
        prompt = self.PROMPT_TEMPLATE.format(instruction=ex["instruction"])
        full_text = prompt + ex["response"]

        prompt_ids = self.tokenizer.encode(prompt).ids
        full_ids = self.tokenizer.encode(full_text).ids

        full_ids = full_ids[: self.block_size + 1]
        input_ids = full_ids[:-1] if len(full_ids) > 1 else full_ids
        target_ids = full_ids[1:] if len(full_ids) > 1 else full_ids

        # Mask the loss (-100 is torch's ignore_index) on every target position
        # that falls within the instruction/prompt, so gradients only flow from
        # tokens that predict the response.
        prompt_len = min(len(prompt_ids), len(target_ids))
        labels = list(target_ids)
        for i in range(prompt_len - 1):
            labels[i] = -100

        pad_len = self.block_size - len(input_ids)
        if pad_len > 0:
            pad_id = self.tokenizer.token_to_id("<pad>")
            input_ids = input_ids + [pad_id] * pad_len
            labels = labels + [-100] * pad_len

        return (
            torch.tensor(input_ids, dtype=torch.long),
            torch.tensor(labels, dtype=torch.long),
        )


class PreferenceDataset(torch.utils.data.Dataset):
    """Loads (prompt, chosen, rejected) triples for reward-model training
    (see notebook 12)."""

    def __init__(self, jsonl_path: Path, tokenizer: Tokenizer, block_size: int):
        self.examples = [json.loads(line) for line in Path(jsonl_path).read_text().splitlines() if line.strip()]
        self.tokenizer = tokenizer
        self.block_size = block_size

    def __len__(self):
        return len(self.examples)

    def _encode(self, prompt: str, response: str):
        text = InstructionDataset.PROMPT_TEMPLATE.format(instruction=prompt) + response
        ids = self.tokenizer.encode(text).ids[: self.block_size]
        true_len = len(ids)  # last real (non-pad) token index is true_len - 1
        pad_id = self.tokenizer.token_to_id("<pad>")
        ids = ids + [pad_id] * (self.block_size - len(ids))
        return torch.tensor(ids, dtype=torch.long), true_len

    def __getitem__(self, idx):
        ex = self.examples[idx]
        chosen, chosen_len = self._encode(ex["prompt"], ex["chosen"])
        rejected, rejected_len = self._encode(ex["prompt"], ex["rejected"])
        return chosen, chosen_len, rejected, rejected_len


def set_seed(seed: int = 1337):
    random.seed(seed)
    torch.manual_seed(seed)
