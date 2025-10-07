"""
FizzBuzz - Étape A (TDD)
- affiche() doit IMPRIMER la concaténation de 1 à 100 avec:
  3 -> "Fizz", 5 -> "Buzz", 15 -> "FrisBee".
"""

def affiche():
    out = []
    for i in range(1, 101):
        if i % 15 == 0:
            out.append("FrisBee")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    # On imprime (comportement demandé), sans retourner de valeur
    print("".join(out))