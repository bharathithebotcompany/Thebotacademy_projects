"""Shared training loop helpers used by the pretraining (08), CPT (10), and SFT (11)
notebooks, so each notebook can focus on what's different about that stage rather
than re-implementing boilerplate."""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import torch

CHECKPOINT_DIR = Path(__file__).resolve().parent.parent / "checkpoints"


def get_lr(step: int, warmup_steps: int, max_steps: int, max_lr: float, min_lr_ratio: float = 0.1) -> float:
    """Linear warmup followed by cosine decay -- the standard GPT-style LR schedule."""
    if step < warmup_steps:
        return max_lr * (step + 1) / warmup_steps
    if step > max_steps:
        return max_lr * min_lr_ratio
    decay_ratio = (step - warmup_steps) / max(1, max_steps - warmup_steps)
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio))
    return max_lr * min_lr_ratio + coeff * max_lr * (1 - min_lr_ratio)


@torch.no_grad()
def estimate_loss(model, data, block_size, batch_size, device, eval_iters, get_batch_fn):
    model.eval()
    losses = torch.zeros(eval_iters)
    for i in range(eval_iters):
        x, y = get_batch_fn(data, block_size, batch_size, device)
        _, loss = model(x, targets=y)
        losses[i] = loss.item()
    model.train()
    return losses.mean().item()


def save_checkpoint(model, name: str):
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    path = CHECKPOINT_DIR / f"{name}.pt"
    torch.save(
        {"model_state_dict": model.state_dict(), "config": vars(model.config)}, path
    )
    return path


def load_checkpoint(model, name: str, device: str = "cpu"):
    """Loads a checkpoint saved by `save_checkpoint` in this same repo. `weights_only=False`
    is safe here because we only ever load files we created ourselves -- never do this
    with a checkpoint downloaded from an untrusted source."""
    path = CHECKPOINT_DIR / f"{name}.pt"
    ckpt = torch.load(path, map_location=device, weights_only=False)
    model.load_state_dict(ckpt["model_state_dict"])
    return model


def plot_losses(train_losses, val_losses=None, title="Training Loss"):
    plt.figure(figsize=(8, 4))
    plt.plot(train_losses, label="train")
    if val_losses:
        xs = [i * (len(train_losses) // max(1, len(val_losses))) for i in range(len(val_losses))]
        plt.plot(xs, val_losses, label="val", marker="o")
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
