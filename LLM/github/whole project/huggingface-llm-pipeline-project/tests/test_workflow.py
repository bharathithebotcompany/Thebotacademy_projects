import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import torch
from tokenizers import Tokenizer, models, pre_tokenizers
from transformers import GPT2Config, GPT2LMHeadModel, PreTrainedTokenizerFast

ROOT = Path(__file__).resolve().parents[1]


class GenerationWorkflowTests(unittest.TestCase):
    def test_cli_loads_a_local_model_and_rejects_context_overflow(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            tokenizer = Tokenizer(models.WordLevel(
                {"<unk>": 0, "<pad>": 1, "Hello": 2, "world": 3, "again": 4}, unk_token="<unk>",
            ))
            tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
            tokenizer = PreTrainedTokenizerFast(
                tokenizer_object=tokenizer, unk_token="<unk>", pad_token="<pad>",
            )
            tokenizer.save_pretrained(directory)
            torch.manual_seed(42)
            config = GPT2Config(
                vocab_size=5, n_positions=16, n_embd=16, n_layer=1, n_head=2,
                bos_token_id=None, eos_token_id=None, pad_token_id=1,
            )
            GPT2LMHeadModel(config).save_pretrained(directory)
            common = [
                sys.executable, "main.py", "Hello world", "--model", str(directory), "--local-files-only",
            ]
            for options in (["--max-new-tokens", "3"], ["--max_length", "5"]):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [*common, *options], cwd=ROOT, capture_output=True, text=True, timeout=60,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue(result.stdout.startswith("Hello world"))
            invalid = subprocess.run(
                [*common, "--max-new-tokens", "17"], cwd=ROOT,
                capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(invalid.returncode, 1)
            self.assertIn("16-token context window", invalid.stderr)
