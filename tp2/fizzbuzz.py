"""
FizzBuzz - Étape A (TDD)
"""

def _token(i: int) -> str:
    if i % 15 == 0:
        return "FrisBee"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

def affiche():
    print("".join(_token(i) for i in range(1, 101)))