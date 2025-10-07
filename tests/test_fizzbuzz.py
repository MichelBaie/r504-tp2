import unittest

# Étape B: on s'attend à une fonction affiche(n) qui RETOURNE la chaîne 1..n
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