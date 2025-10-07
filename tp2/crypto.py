"""
Crypto - Étape A (TDD)
- crypt(message): remplace chaque caractère par le suivant dans:
  ascii_letters + ascii_punctuation + ascii_digits + " "
- Décalage circulaire.
"""

import string

CARACTERES = string.ascii_letters + string.ascii_punctuation + string.ascii_digits + " "

def crypt(message: str) -> str:
    # Squelette initial: retourne tel quel (les tests doivent échouer)
    if not isinstance(message, str):
        raise TypeError("message doit être une chaîne de caractères (str).")
    return message