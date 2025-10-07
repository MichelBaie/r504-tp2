import unittest
from tp2.crypto import crypt, decrypt

class TestCryptoStepA(unittest.TestCase):
    def test_letters_simple_shift(self):
        # Lettres minuscules dans ascii_letters -> décalage de 1
        self.assertEqual(crypt("abc"), "bcd")

    def test_lower_to_upper_transition(self):
        # Dans ascii_letters, après 'z' vient 'A'
        self.assertEqual(crypt("z"), "A")

    def test_upper_to_punctuation_transition(self):
        # Après 'Z' (fin de ascii_letters) vient '!' (début de string.punctuation)
        self.assertEqual(crypt("Z"), "!")

    def test_punctuation_to_digits_transition(self):
        # '~' est le dernier de string.punctuation -> '0' (début de string.digits)
        self.assertEqual(crypt("~"), "0")

    def test_digit_to_space_transition(self):
        # '9' (fin de string.digits) -> ' ' (espace)
        self.assertEqual(crypt("9"), " ")

    def test_space_wraps_to_a(self):
        # Espace (dernier du jeu) -> 'a' (début de ascii_letters)
        self.assertEqual(crypt(" "), "a")

    def test_mixed_sequence(self):
        # a -> b, Z -> !, 9 -> ' ', ' ' -> a
        self.assertEqual(crypt("aZ9 "), "b! a")

    def test_empty_returns_empty(self):
        self.assertEqual(crypt(""), "")


class TestCryptoStepB(unittest.TestCase):
    def test_crypt_with_step_and_suffix(self):
        # Décalage de 2, puis suffixe '2' ajouté à la fin
        self.assertEqual(crypt("abc", 2), "cde2")

    def test_wrap_with_step(self):
        # 'Z' -> '!' (1) -> '"' (2) -> '#' (3), puis suffixe '3'
        self.assertEqual(crypt("Z", 3), "#3")

    def test_invalid_step_raises(self):
        with self.assertRaises(ValueError):
            crypt("abc", 0)
        with self.assertRaises(ValueError):
            crypt("abc", 10)
        with self.assertRaises(ValueError):
            crypt("abc", -1)

    def test_step_type_validation(self):
        with self.assertRaises(TypeError):
            crypt("abc", "2")     # pas doit être int
        with self.assertRaises(TypeError):
            crypt("abc", 2.5)     # pas doit être int

    def test_mixed_sequence_with_step(self):
        # Avec pas=2 : 'a'->'c', 'Z'->'"', '9'->'a', ' '->'b', puis suffixe '2'
        self.assertEqual(crypt("aZ9 ", 2), "c\"ab2")


class TestCryptoStepC(unittest.TestCase):
    def test_decrypt_inverts_crypt_simple(self):
        cipher = crypt("Bonjour!", 3)  # ajoute '3' en suffixe
        self.assertEqual(decrypt(cipher), "Bonjour!")

    def test_decrypt_inverts_mixed_sequence(self):
        cipher = crypt("aZ9 ", 2)      # "c\"ab2"
        self.assertEqual(decrypt(cipher), "aZ9 ")

    def test_decrypt_empty_plain_message(self):
        # crypt("", 5) -> "5"; decrypt("5") -> ""
        self.assertEqual(decrypt("5"), "")

    def test_decrypt_missing_or_invalid_suffix_raises(self):
        # Pas de suffixe (pas manquant)
        with self.assertRaises(ValueError):
            decrypt("bcd")  # provient de crypt("abc") sans pas explicite
        # Suffixe '0' invalide (doit être 1..9)
        with self.assertRaises(ValueError):
            decrypt("ab0")
        # Dernier caractère non numérique
        with self.assertRaises(ValueError):
            decrypt("abx")