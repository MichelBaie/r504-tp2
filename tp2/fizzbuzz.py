"""
FizzBuzz - Étapes A, B & C (TDD)
- Étape A: affiche() IMPRIME 1..100 avec remplacements:
  3 -> "Fizz", 5 -> "Buzz", 15 -> "FrisBee".
- Étape B: affiche(n) RETOURNE la chaîne 1..n (mêmes règles).
- Étape C: affiche(n1, n2) IMPRIME la chaîne n1..n2 (mêmes règles).
"""

def _token(i: int) -> str:
    if i % 15 == 0:
        return "FrisBee"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

def _build_range(from_inclusive: int, to_inclusive: int) -> str:
    # range gère naturellement le cas from_inclusive > to_inclusive (chaîne vide)
    return "".join(_token(i) for i in range(from_inclusive, to_inclusive + 1))

def affiche(n: int | None = None, n2: int | None = None):
    """
    - Sans argument: imprime 1..100 (retourne None).
    - Avec n: retourne la chaîne 1..n (ne rien imprimer).
    - Avec n et n2: imprime la chaîne n..n2 (retourne None).
    """
    # Étape A: aucun argument
    if n is None and n2 is None:
        print(_build_range(1, 100))
        return None

    # Étape B: un argument (n)
    if n is not None and n2 is None:
        if not isinstance(n, int):
            raise TypeError("n doit être un entier (int).")
        if n < 1:
            # Cas non spécifié : on renvoie une chaîne vide pour n < 1.
            return ""
        return _build_range(1, n)

    # Étape C: deux arguments (n1, n2) -> IMPRIMER
    if n is not None and n2 is not None:
        if not isinstance(n, int) or not isinstance(n2, int):
            raise TypeError("n et n2 doivent être des entiers (int).")
        print(_build_range(n, n2))
        return None

    # Cas incohérent (ex: n=None, n2 non None)
    raise TypeError("Usage: affiche(), affiche(n), ou affiche(n1, n2).")