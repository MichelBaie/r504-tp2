"""
FizzBuzz - Étapes A & B (TDD)
- Étape A: affiche() IMPRIME 1..100 avec remplacements:
  3 -> "Fizz", 5 -> "Buzz", 15 -> "FrisBee".
- Étape B: affiche(n) RETOURNE la chaîne 1..n (mêmes règles).
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
    return "".join(_token(i) for i in range(from_inclusive, to_inclusive + 1))

def affiche(n: int | None = None):
    """
    - Sans argument: imprime 1..100 (retourne None).
    - Avec n: retourne la chaîne 1..n (ne rien imprimer).
    """
    if n is None:
        print(_build_range(1, 100))
        return None
    if not isinstance(n, int):
        raise TypeError("n doit être un entier (int).")
    if n < 1:
        # L'énoncé ne précise pas le cas n < 1; ici on renvoie une chaîne vide.
        return ""
    return _build_range(1, n)