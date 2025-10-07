"""
Crypto - Étape A (TDD)
- crypt(message): remplace chaque caractère par le suivant dans:
  ascii_letters + ascii_punctuation + ascii_digits + " "
- Décalage circulaire.
"""

import string

CARACTERES = string.ascii_letters + string.ascii_punctuation + string.ascii_digits + " "
_INDEX = {c: i for i, c in enumerate(CARACTERES)}  # indexation rapide

def crypt(message: str) -> str:
    if not isinstance(message, str):
        raise TypeError("message doit être une chaîne de caractères (str).")

    # Chaîne vide -> renvoie vide
    if message == "":
        return ""

    L = len(CARACTERES)
    out_chars = []
    for ch in message:
        i = _INDEX.get(ch)
        if i is None:
            # Si besoin, vous pouvez choisir de "laisser tel quel" au lieu d'erreur.
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out_chars.append(CARACTERES[(i + 1) % L])

    return "".join(out_chars)