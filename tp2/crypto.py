"""
Crypto - Étape A (TDD)
- crypt(message): remplace chaque caractère par le suivant dans:
  ascii_letters + punctuation + digits + " "
- Décalage circulaire.
"""

import string

# IMPORTANT: utiliser string.punctuation et string.digits (pas "ascii_*")
CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "
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
            # Caractère non supporté dans l'alphabet défini
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out_chars.append(CARACTERES[(i + 1) % L])

    return "".join(out_chars)