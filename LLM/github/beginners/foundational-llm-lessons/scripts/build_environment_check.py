import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# Environment Check

Run this notebook first. It confirms your Python environment has everything
the rest of the curriculum needs, and reports whether you're training on CPU
or GPU (this curriculum is designed to work fine on CPU, since the model is
only ~20M parameters).
"""),
    code("""
import sys
print("Python version:", sys.version)
"""),
    code("""
import torch, numpy, matplotlib, tokenizers

print("torch        :", torch.__version__)
print("numpy        :", numpy.__version__)
print("matplotlib   :", matplotlib.__version__)
print("tokenizers   :", tokenizers.__version__)

print()
print("CUDA available:", torch.cuda.is_available())
print("MPS available :", torch.backends.mps.is_available() if hasattr(torch.backends, "mps") else False)

device = "cuda" if torch.cuda.is_available() else ("mps" if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available() else "cpu")
print("This machine will train on:", device)
"""),
    md("""
## Quick tensor sanity check

If this cell runs without error and prints a small tensor, PyTorch is working correctly.
"""),
    code("""
x = torch.randn(3, 3)
y = torch.randn(3, 3)
z = x @ y
print(z)
print("Sum:", z.sum().item())
"""),
    md("""
## Repo layout check

Confirms the shared `src/` modules and `data/` files this curriculum depends on
are present and importable.
"""),
    code("""
import sys
sys.path.insert(0, "..")  # so `import src` works from inside notebooks/

from src.model import GPTMicro, GPTConfig
from src.data import load_electricity_for_boys

cfg = GPTConfig()
model = GPTMicro(cfg)
print(f"GPTMicro loaded OK: {model.num_params()/1e6:.2f}M parameters")

text = load_electricity_for_boys()
print(f"Corpus loaded OK: {len(text):,} characters")
"""),
    md("""
## You're ready

If every cell above ran without errors, you have everything you need. Continue to
`notebooks/00_environment_and_python_refresher.ipynb`.
"""),
]

write_notebook(REPO_ROOT / "environment_check.ipynb", cells)
