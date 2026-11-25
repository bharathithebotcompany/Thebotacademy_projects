"""Generates toy instruction/response pairs (data/instruction_data.jsonl) and
preference pairs (data/preference_pairs.jsonl) used by the SFT (11), reward
modeling (12), and PPO (13) notebooks.

Everything here is templated/programmatic -- not scraped -- so it's easy to
inspect, regenerate, and extend. Three task families are covered:
  1. Arithmetic ("What is 12 + 7?" -> "19")
  2. String formatting (reverse, uppercase, title-case a short phrase)
  3. Simple Q&A about facts drawn from the "Electricity for Boys" corpus

Run once: `python scripts/generate_instruction_data.py`
"""

import json
import random
from pathlib import Path

random.seed(1337)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# A handful of facts hand-picked from the corpus, used for the Q&A task family.
# Keeping this small and manually curated (rather than scraping the text
# automatically) keeps the ground truth reliable for a toy dataset.
ELECTRICITY_FACTS = [
    ("What is a battery used for?", "A battery stores chemical energy and converts it into electric current."),
    ("What does a galvanometer measure?", "A galvanometer detects and measures small electric currents."),
    ("What is a conductor?", "A conductor is a material, such as copper, that allows electric current to flow through it easily."),
    ("What is an insulator?", "An insulator is a material, such as rubber or glass, that does not allow electric current to flow through it."),
    ("What did Thales of Miletus discover?", "Thales of Miletus observed that rubbed amber attracted and repelled light bodies, one of the earliest recorded electrical observations."),
    ("What is a Leyden jar?", "A Leyden jar is an early device used to store static electric charge."),
    ("What is a dynamo?", "A dynamo is a machine that converts mechanical energy into electrical energy."),
    ("What is an electromagnet?", "An electromagnet is a coil of wire that produces a magnetic field when electric current flows through it."),
    ("What metals are commonly used in simple batteries?", "Zinc and copper are commonly used as the two dissimilar metals in simple batteries."),
    ("What is the purpose of a switchboard?", "A switchboard is used to control and distribute electric current to different circuits."),
]


def gen_arithmetic(n: int):
    examples = []
    ops = [("+", lambda a, b: a + b), ("-", lambda a, b: a - b), ("*", lambda a, b: a * b)]
    for _ in range(n):
        a, b = random.randint(1, 50), random.randint(1, 50)
        symbol, fn = random.choice(ops)
        correct = fn(a, b)
        wrong = correct + random.choice([-3, -2, -1, 1, 2, 3])
        instruction = f"What is {a} {symbol} {b}?"
        examples.append({"instruction": instruction, "response": str(correct), "_wrong": str(wrong)})
    return examples


def gen_formatting(n: int):
    words = ["electricity", "battery", "circuit", "magnet", "current", "wire", "spark",
              "conductor", "insulator", "voltage", "energy", "science", "workshop", "machine"]
    tasks = ["uppercase", "reverse", "titlecase"]
    examples = []
    for _ in range(n):
        w = random.choice(words)
        task = random.choice(tasks)
        if task == "uppercase":
            instruction = f"Convert '{w}' to uppercase."
            correct = w.upper()
            wrong = w.lower()
        elif task == "reverse":
            instruction = f"Reverse the word '{w}'."
            correct = w[::-1]
            wrong = w
        else:
            instruction = f"Convert '{w}' to title case."
            correct = w.title()
            wrong = w.upper()
        examples.append({"instruction": instruction, "response": correct, "_wrong": wrong})
    return examples


def gen_qa(n: int):
    examples = []
    wrong_pool = [r for _, r in ELECTRICITY_FACTS]
    for _ in range(n):
        q, a = random.choice(ELECTRICITY_FACTS)
        wrong = random.choice([w for w in wrong_pool if w != a])
        examples.append({"instruction": q, "response": a, "_wrong": wrong})
    return examples


def main():
    examples = gen_arithmetic(350) + gen_formatting(350) + gen_qa(300)
    random.shuffle(examples)

    instruction_path = DATA_DIR / "instruction_data.jsonl"
    preference_path = DATA_DIR / "preference_pairs.jsonl"

    with instruction_path.open("w") as f_instr, preference_path.open("w") as f_pref:
        for ex in examples:
            f_instr.write(json.dumps({"instruction": ex["instruction"], "response": ex["response"]}) + "\n")
            f_pref.write(json.dumps({
                "prompt": ex["instruction"],
                "chosen": ex["response"],
                "rejected": ex["_wrong"],
            }) + "\n")

    print(f"Wrote {len(examples)} examples to {instruction_path}")
    print(f"Wrote {len(examples)} preference pairs to {preference_path}")


if __name__ == "__main__":
    main()
