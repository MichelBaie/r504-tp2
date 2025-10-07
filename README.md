# R504 - TP2 - TDD en Python (unittest)

[![CI](https://github.com/MichelBaie/r504-tp2/actions/workflows/ci.yml/badge.svg)](https://github.com/MichelBaie/r504-tp2/actions/workflows/ci.yml)

Ce dépôt contient les exercices FizzBuzz et Cryptage réalisés en TDD, avec CI GitHub Actions.
L’historique des commits illustre les cycles TDD: test (FAIL) → implémentation (SUCCESS) → refactor.

## Prérequis
- Python 3.10+ (testé 3.10 / 3.11 / 3.12 / 3.13)
- unittest (stdlib)

## Installation locale
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (Git Bash):
source .venv/Scripts/activate
pip install -r requirements.txt  # vide pour l’instant
```

## Lancer la CI localement (optionnel)
- Lint: `ruff check .` et `black --check --line-length 100 .`
- Tests: 
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Structure du projet
```
.
├─ tp2/
│  ├─ fizzbuzz.py     # affiche(), logique FizzBuzz + helpers
│  ├─ crypto.py       # crypt(message[, pas]) + decrypt(message)
│  └─ __init__.py
├─ tests/
│  ├─ test_fizzbuzz.py
│  ├─ test_crypto.py
│  └─ test_sanity.py  # test minimal d’infrastructure
├─ .github/workflows/ci.yml
├─ .editorconfig
├─ pyproject.toml     # config Black + Ruff
├─ .gitignore
├─ LICENSE
└─ README.md
```

## FizzBuzz
- `affiche()` imprime la concaténation 1..100 avec:
  - 3 → `Fizz`, 5 → `Buzz`, 15 → `FrisBee`
- `affiche(n)` retourne la chaîne 1..n (mêmes règles).
- `affiche(n1, n2)` imprime la concaténation n1..n2 (mêmes règles).

Exemples rapides:
```bash
python -c "from tp2.fizzbuzz import affiche; affiche()"
python -c "from tp2.fizzbuzz import affiche; print(affiche(15))"
python -c "from tp2.fizzbuzz import affiche; affiche(5, 10)"
```

## Cryptage
- Alphabet circulaire: `string.ascii_letters + string.punctuation + string.digits + " "`.
- `crypt(message)` décale de 1 (sans suffixe).
- `crypt(message, pas)` décale de `pas` (1..9) et ajoute le suffixe `pas` à la fin du message chiffré.
- `decrypt(message)` lit le suffixe (1..9) et décale en sens inverse.

Exemples rapides:
```bash
python -c "from tp2.crypto import crypt; print(crypt('aZ9 '))"       # b! a
python -c "from tp2.crypto import crypt; print(crypt('abc', 2))"     # cde2
python -c "from tp2.crypto import decrypt; print(decrypt('cde2'))"   # abc
```

### Limites
- Seuls les caractères de l’alphabet défini sont supportés; sinon `ValueError`.
- `decrypt` attend un suffixe numérique 1..9; sinon `ValueError`.

## TDD et livrable
- L’évaluation s’appuie sur l’historique de commits: cycles FAIL → SUCCESS → REFACTOR.
- CI: lint (Ruff + Black) et tests unittest sur 4 versions de Python.
- Ajoutez l’enseignant comme collaborateur GitHub pour l’accès complet.

## Licence
Ce projet est sous licence *The Unlicense* (domaine public). Voir `LICENSE`.