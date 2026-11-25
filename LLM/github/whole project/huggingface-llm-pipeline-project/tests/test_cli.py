import unittest

from main import continuation_budget, parse_args


class GenerationArgumentsTests(unittest.TestCase):
    def test_legacy_alias_measures_total_tokens(self):
        args = parse_args(["A prompt", "--max_length", "12"])
        self.assertEqual(continuation_budget(4, args.max_length, args.max_new_tokens), 8)

    def test_new_tokens_are_independent_of_prompt_length(self):
        args = parse_args(["A prompt", "--max-new-tokens", "6"])
        self.assertEqual(continuation_budget(120, 50, args.max_new_tokens), 6)

    def test_full_prompt_exhausts_total_budget(self):
        with self.assertRaisesRegex(ValueError, "3 tokens"):
            continuation_budget(3, 3, None)
