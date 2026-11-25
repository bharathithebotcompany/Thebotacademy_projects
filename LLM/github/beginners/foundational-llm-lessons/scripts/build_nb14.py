import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import md, code, write_notebook

REPO_ROOT = Path(__file__).resolve().parent.parent

cells = [
    md("""
# 14 — Putting It All Together

## The Full Pipeline, Recapped

| Stage | Notebook | What it does | Checkpoint produced |
|---|---|---|---|
| Tokenization | 02 | Build a BPE vocabulary from raw text | `data/tokenizer.json` |
| Pretraining | 08 | Learn general language structure via next-token prediction on raw text | `pretrained_electricity` |
| Continued Pretraining (CPT) | 10 | Adapt the pretrained model toward a new domain's raw text | `cpt_electricity` |
| Supervised Fine-Tuning (SFT) | 11 | Teach instruction/response behavior via masked next-token loss | `sft_electricity` |
| Reward Modeling | 12 | Learn to score response quality from preference pairs | `reward_model_backbone` + `reward_head.pt` |
| RL (PPO) | 13 | Fine-tune the policy to maximize learned reward, under a KL constraint | `ppo_electricity` |

Every single stage used the *same* underlying model architecture (`GPTMicro`, ~20M parameters, `src/model.py`) and largely the *same* training loop shape (forward pass, loss, backward pass, optimizer step) — what changed each time was the **data**, the **loss/objective**, and sometimes a **frozen reference copy** for comparison. That's the core insight this whole curriculum was built to demonstrate: modern LLM training pipelines are a sequence of variations on one simple mechanism, not a different algorithm at every stage.

## Side-by-Side Generation Comparison

Let's load every checkpoint and compare how each one completes the same prompts.
"""),
    code("""
import sys
sys.path.insert(0, "..")

import torch
import torch.nn as nn

from src.model import GPTMicro, GPTConfig
from src.data import train_bpe_tokenizer, load_electricity_for_boys, InstructionDataset, set_seed
from src.train_utils import load_checkpoint

torch.set_num_threads(6)
set_seed(0)

config = GPTConfig(vocab_size=8000, block_size=128, n_layer=6, n_head=8, n_embd=480, dropout=0.1)
text = load_electricity_for_boys()
tokenizer = train_bpe_tokenizer(text, vocab_size=8000)

checkpoint_names = ["pretrained_electricity", "cpt_electricity", "sft_electricity", "ppo_electricity"]
models = {}
for name in checkpoint_names:
    m = GPTMicro(config)
    load_checkpoint(m, name, device="cpu")
    m.eval()
    models[name] = m
    print(f"loaded {name}")
"""),
    code("""
def generate_from(model, prompt, max_new_tokens=25, temperature=0.7, top_k=40, instruction_format=False):
    text_in = InstructionDataset.PROMPT_TEMPLATE.format(instruction=prompt) if instruction_format else prompt
    context = torch.tensor([tokenizer.encode(text_in).ids], dtype=torch.long)
    torch.manual_seed(0)
    out = model.generate(context, max_new_tokens=max_new_tokens, temperature=temperature, top_k=top_k)
    return tokenizer.decode(out[0, context.shape[1]:].tolist())

test_prompts = ["What is a battery used for?", "What is 8 + 4?"]

for prompt in test_prompts:
    print("=" * 70)
    print(f"PROMPT: {prompt}")
    print("=" * 70)
    for name in checkpoint_names:
        # Pretrained/CPT models never learned the instruction format, so we
        # feed them the raw prompt; SFT/PPO models expect the formatted version.
        instruction_format = name in ("sft_electricity", "ppo_electricity")
        response = generate_from(models[name], prompt, instruction_format=instruction_format)
        print(f"[{name:22s}] {response!r}")
    print()
"""),
    md("""
## What to Notice
- **Pretrained → CPT**: generations shift subtly toward the CPT corpus's shorter, more direct style, even without any instruction-following behavior yet.
- **CPT → SFT**: this is the biggest qualitative jump — the model starts producing response-shaped text instead of arbitrary continuations, because SFT explicitly taught the instruction/response format via masked loss.
- **SFT → PPO**: a smaller, more targeted shift — the policy nudges toward whatever the reward model scores highly, constrained by the KL penalty so it doesn't stray far from SFT's baseline fluency.

## Where This Curriculum's Simplifications Matter Most
Real production LLM pipelines differ from what we built here mainly in **scale and data quality**, not mechanism:
- Billions of pretraining tokens (vs. our ~50K), and vocabulary sizes of 50K-200K+ (vs. our 8K).
- Millions of human-written/human-rated SFT and preference examples (vs. our few hundred templated ones).
- Reward models that are themselves large pretrained LLMs (vs. our tiny scalar-head model).
- Much larger PPO rollout batches, multiple update epochs per batch, and often a separately-trained value function/critic (vs. our simplified baseline advantage).
- Additional safety/alignment techniques (constitutional AI, red-teaming, multiple reward models, etc.) layered on top of the basic RLHF loop we implemented.

None of that changes the *shape* of what you just built — it changes how much data, compute, and careful curation gets poured into each identical stage.

## Further Reading (the papers behind each notebook)
- **Attention Is All You Need** (Vaswani et al., 2017) — the Transformer architecture (notebooks 05, 06).
- **Language Models are Few-Shot Learners** (GPT-3 paper, Brown et al., 2020) — scaling up this exact architecture.
- **Training language models to follow instructions with human feedback** (InstructGPT, Ouyang et al., 2022) — the SFT + reward modeling + PPO pipeline (notebooks 11-13).
- **Proximal Policy Optimization Algorithms** (Schulman et al., 2017) — the RL algorithm behind notebook 13.
- **Direct Preference Optimization** (Rafailov et al., 2023) — a popular, simpler alternative to reward-model + PPO that directly optimizes the policy on preference pairs; worth exploring as a follow-up to notebook 13.

## Ideas to Extend This Curriculum
- **Bigger model / more data**: increase `n_embd`/`n_layer` in `GPTConfig` and swap in a larger corpus (multiple Gutenberg books) — everything else stays the same.
- **Try DPO instead of PPO**: implement Direct Preference Optimization directly on `preference_pairs.jsonl`, skipping the separate reward model entirely, and compare results to notebook 13.
- **Real instruction data**: replace the templated `instruction_data.jsonl` with a small slice of a real, larger instruction dataset and see how response quality changes.
- **Longer context**: increase `block_size` and see how training time and quality trade off.
- **Evaluation suite**: build a small held-out test set of instructions with known correct answers, and track accuracy across every checkpoint stage (pretrained → CPT → SFT → PPO) as a single number instead of eyeballing generations.

## Summary
You built and trained, from scratch, a complete GPT-style language model pipeline: tokenization, a ~20M-parameter Transformer, pretraining, continued pretraining, supervised fine-tuning, reward modeling, and RLHF via PPO — the same sequence of stages, in miniature, behind every major modern LLM assistant. Everything here ran on CPU in a few minutes to tens of minutes per stage, specifically so the mechanism stays inspectable and fast to iterate on, rather than a black box you can only read about.
"""),
]

write_notebook(REPO_ROOT / "notebooks" / "14_putting_it_all_together.ipynb", cells)
