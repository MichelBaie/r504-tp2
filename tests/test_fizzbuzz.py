import io
import unittest
from contextlib import redirect_stdout

# Étape A: on s'attend à une fonction affiche() qui IMPRIME la concaténation 1..100
from tp2.fizzbuzz import affiche

class TestFizzBuzzStepA(unittest.TestCase):
    def test_affiche_prints_prefix_and_suffix(self):
        expected_prefix_1_to_20 = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz19Buzz"
        expected_suffix_97_to_100 = "9798FizzBuzz"

        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = affiche()  # doit IMPRIMER, pas retourner la chaîne
        out = buf.getvalue().strip()

        # Le début doit correspondre à 1..20
        self.assertTrue(
            out.startswith(expected_prefix_1_to_20),
            f"Le préfixe ne correspond pas.\nGot:      {out[:len(expected_prefix_1_to_20)]}\nExpected: {expected_prefix_1_to_20}",
        )
        # La fin doit se terminer par ...97 98 Fizz 100->Buzz
        self.assertTrue(
            out.endswith(expected_suffix_97_to_100),
            f"La fin ne correspond pas.\nGot:      {out[-len(expected_suffix_97_to_100):]}\nExpected: {expected_suffix_97_to_100}",
        )
        # La fonction imprime et ne retourne rien
        self.assertIsNone(ret)