import io
import unittest
from contextlib import redirect_stdout

# Étapes B & C:
# - Étape B: affiche(n) RETOURNE la chaîne 1..n.
# - Étape C: affiche(n1, n2) IMPRIME la chaîne n1..n2 (stdout).

from tp2.fizzbuzz import affiche

class TestFizzBuzzStepB(unittest.TestCase):
    def test_affiche_n_returns_example_15(self):
        expected_1_to_15 = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        self.assertEqual(affiche(15), expected_1_to_15)

    def test_affiche_100_prefix_suffix(self):
        expected_prefix_1_to_20 = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz19Buzz"
        expected_suffix_97_to_100 = "9798FizzBuzz"
        out = affiche(100)
        self.assertTrue(
            out.startswith(expected_prefix_1_to_20),
            f"Préfixe incorrect.\nGot:      {out[:len(expected_prefix_1_to_20)]}\nExpected: {expected_prefix_1_to_20}",
        )
        self.assertTrue(
            out.endswith(expected_suffix_97_to_100),
            f"Suffixe incorrect.\nGot:      {out[-len(expected_suffix_97_to_100):]}\nExpected: {expected_suffix_97_to_100}",
        )

class TestFizzBuzzStepC(unittest.TestCase):
    def test_affiche_range_5_10_prints(self):
        expected_5_to_10 = "BuzzFizz78FizzBuzz"
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = affiche(5, 10)
        out = buf.getvalue().strip()
        self.assertEqual(out, expected_5_to_10)
        self.assertIsNone(ret)  # on IMPRIME, on ne retourne rien

    def test_affiche_range_10_16_prints(self):
        expected_10_to_16 = "Buzz11Fizz1314FrisBee16"
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = affiche(10, 16)
        out = buf.getvalue().strip()
        self.assertEqual(out, expected_10_to_16)
        self.assertIsNone(ret)