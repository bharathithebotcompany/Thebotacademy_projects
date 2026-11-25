import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 00 — Environment & Python Refresher

## Terms & Definitions
- **Tensor**: a multi-dimensional array (generalizing scalars, vectors, matrices) that PyTorch uses to represent all data and model parameters.
- **`nn.Module`**: PyTorch's base class for anything with learnable parameters (a layer, a whole model).
- **Autograd**: PyTorch's automatic differentiation engine — it records operations on tensors so it can compute gradients automatically via `.backward()`.
- **Gradient**: the derivative of a loss with respect to a parameter; tells us which direction to nudge the parameter to reduce the loss.
- **Device**: where a tensor's data lives and where its computations run — `"cpu"`, `"cuda"` (NVIDIA GPU), or `"mps"` (Apple Silicon GPU).

## Why this notebook exists
Every later notebook in this curriculum assumes comfort with basic PyTorch tensor operations and the training loop pattern (forward pass → loss → backward pass → optimizer step). If you already know PyTorch, skim this and move to `01_what_is_a_language_model.ipynb`.

## This machine
This curriculum was built and tested on a machine with **no NVIDIA/AMD GPU** — only an Intel integrated GPU — so `torch.cuda.is_available()` is `False` here, and every notebook defaults to `device = "cpu"`. That's fine: the whole point of using a ~20M parameter model is that CPU training is fast enough to iterate on. If you're running this on a machine *with* a CUDA GPU, the code will pick it up automatically.
"""),
    code("""
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print("device:", device)
"""),
    md("""
## Tensors

A tensor is just an array with a shape (its "dimensions"). Scalars are 0-D tensors, vectors are 1-D, matrices are 2-D, and language models mostly work with 3-D tensors shaped `(batch, sequence_length, features)`.
"""),
    code("""
scalar = torch.tensor(3.0)
vector = torch.tensor([1.0, 2.0, 3.0])
matrix = torch.randn(2, 3)          # 2 rows, 3 columns, random values
batch  = torch.randn(4, 5, 6)       # e.g. 4 sequences, 5 tokens each, 6 features per token

for name, t in [("scalar", scalar), ("vector", vector), ("matrix", matrix), ("batch", batch)]:
    print(f"{name:8s} shape={tuple(t.shape)} ndim={t.ndim}")
"""),
    md("""
Common operations you'll see constantly in the transformer code later: matrix multiplication (`@`), reshaping (`.view`/`.reshape`), and transposing dimensions (`.transpose`).
"""),
    code("""
a = torch.randn(2, 3)
b = torch.randn(3, 4)
c = a @ b  # matrix multiply: (2,3) @ (3,4) -> (2,4)
print("a @ b shape:", c.shape)

flat = torch.arange(12)
reshaped = flat.view(3, 4)
print("reshaped:\\n", reshaped)

transposed = reshaped.transpose(0, 1)
print("transposed shape:", transposed.shape)
"""),
    md("""
## `nn.Module` and parameters

Every learnable component in PyTorch — a single linear layer or an entire GPT — subclasses `nn.Module`. It holds parameters (tensors with `requires_grad=True`) and defines a `forward()` method describing how input becomes output.
"""),
    code("""
import torch.nn as nn

linear = nn.Linear(in_features=3, out_features=1)  # y = xW^T + b
print("weight shape:", linear.weight.shape)
print("bias shape:", linear.bias.shape)

x = torch.randn(5, 3)  # batch of 5 examples, 3 features each
y = linear(x)
print("output shape:", y.shape)

n_params = sum(p.numel() for p in linear.parameters())
print("total parameters:", n_params)  # 3*1 weight + 1 bias = 4
"""),
    md("""
## Autograd: how a model learns

1. Run a **forward pass**: input → model → prediction.
2. Compute a **loss**: a single number measuring how wrong the prediction was.
3. Call **`loss.backward()`**: PyTorch walks backward through every operation and computes the gradient of the loss with respect to every parameter.
4. An **optimizer** (e.g. Adam) uses those gradients to nudge each parameter slightly in the direction that reduces the loss.
5. Repeat, thousands of times, and the model's predictions get better. This is the entire training loop every notebook from here on uses — the only things that change are *what* the model predicts and *what* the loss measures.
"""),
    code("""
# A tiny end-to-end example: fit y = 2x + 1 from noisy data.
torch.manual_seed(0)

x = torch.linspace(-1, 1, 64).unsqueeze(1)   # shape (64, 1)
y_true = 2 * x + 1 + 0.1 * torch.randn_like(x)

model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for step in range(200):
    y_pred = model(x)
    loss = ((y_pred - y_true) ** 2).mean()   # mean squared error

    optimizer.zero_grad()   # clear old gradients
    loss.backward()          # compute new gradients
    optimizer.step()         # update parameters

    if step % 50 == 0:
        print(f"step {step:3d}  loss={loss.item():.4f}")

w, b = model.weight.item(), model.bias.item()
print(f"\\nlearned: y = {w:.2f}x + {b:.2f}  (target was y = 2x + 1)")
"""),
    md("""
## Exercise
Change the optimizer from `SGD` to `torch.optim.Adam` and re-run — notice it converges in fewer steps. Every notebook from here uses `AdamW` (Adam with a small tweak for regularization), so it's worth seeing the difference firsthand.

## Summary
- Tensors are the universal data structure; shapes matter and `.view`/`.transpose` reshape them.
- `nn.Module` + parameters + `forward()` defines any model, tiny or huge.
- Autograd + an optimizer is the entire learning mechanism: forward, loss, backward, step.
- This machine trains on CPU — the curriculum is sized (~20M params) specifically so that's not a problem.

Next: **01 — What Is a Language Model** (no more generic PyTorch — from here everything is about language models specifically).
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "00_environment_and_python_refresher.ipynb", cells)
