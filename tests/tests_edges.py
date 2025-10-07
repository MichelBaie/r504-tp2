import io
import unittest
from contextlib import redirect_stdout
from tp2.fizzbuzz import affiche
from tp2.crypto import crypt

class TestFizzBuzzEdges(unittest.TestCase):
    def test_affiche_n_less_than_1_returns_empty(self):
        self.assertEqual(affiche(0), "")
        self.assertEqual(affiche(-5), "")

    def test_affiche_range_inverted_prints_empty(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            affiche(10, 5)  # plage inversée -> vide
        self.assertEqual(buf.getvalue().strip(), "")

class TestCryptoEdges(unittest.TestCase):
    def test_unsupported_char_raises(self):
        with self.assertRaises(ValueError):
            crypt("é")  # non présent dans l'alphabet défini