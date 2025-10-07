"""
Crypto - Étapes A, B & C (TDD)
- Étape A:
  crypt(message): remplace chaque caractère par le suivant dans
  ascii_letters + string.punctuation + string.digits + " ", avec décalage 1.
- Étape B:
  crypt(message, pas): décalage de 'pas' (entier 1..9) et concatène le 'pas' en fin.
  - Si 'pas' est fourni, on retourne le message chiffré + str(pas) en suffixe.
  - Si 'pas' n'est pas fourni (None), comportement de l'étape A (pas=1) sans suffixe.
- Étape C:
  decrypt(message): lit le 'pas' (dernier caractère, 1..9), décale en sens inverse et
  renvoie le message en clair.
"""

import string

CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "
_INDEX = {c: i for i, c in enumerate(CARACTERES)}  # indexation rapide

def crypt(message: str, pas: int | None = None) -> str:
    if not isinstance(message, str):
        raise TypeError("message doit être une chaîne de caractères (str).")

    # Détermination du pas de décalage
    if pas is None:
        step = 1  # Étape A: défaut
        append_suffix = False
    else:
        if not isinstance(pas, int):
            raise TypeError("pas doit être un entier (int).")
        if pas < 1 or pas > 9:
            raise ValueError("pas doit être un entier entre 1 et 9.")
        step = pas
        append_suffix = True

    # Chaîne vide
    if message == "":
        return ("" + (str(pas) if append_suffix else ""))

    L = len(CARACTERES)
    out_chars = []
    for ch in message:
        i = _INDEX.get(ch)
        if i is None:
            # Caractère non supporté dans l'alphabet défini
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out_chars.append(CARACTERES[(i + step) % L])

    result = "".join(out_chars)
    if append_suffix:
        result += str(pas)
    return result

def decrypt(message: str) -> str:
    """
    Déchiffre un message produit par crypt(message, pas).
    Le dernier caractère doit être un chiffre '1'..'9' indiquant le pas.
    Exemple: crypt("abc", 2) -> "cde2"; decrypt("cde2") -> "abc".
    """
    if not isinstance(message, str):
        raise TypeError("message doit être une chaîne de caractères (str).")
    if len(message) == 0:
        # Pas de suffixe, message invalide pour decrypt
        raise ValueError("message chiffré vide: suffixe 'pas' manquant.")

    suffix = message[-1]
    if suffix < "1" or suffix > "9":
        raise ValueError("suffixe invalide: le dernier caractère doit être un chiffre entre 1 et 9.")
    pas = int(suffix)

    data = message[:-1]  # peut être vide si le message en clair était vide
    if data == "":
        return ""  # cas crypt("", pas) -> str(pas)

    L = len(CARACTERES)
    out_chars = []
    for ch in data:
        i = _INDEX.get(ch)
        if i is None:
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out_chars.append(CARACTERES[(i - pas) % L])

    return "".join(out_chars)