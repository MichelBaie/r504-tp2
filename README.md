# R504 - TP2 - TDD en Python (unittest)

Ce dépôt servira pour le TP2 (FizzBuzz + cryptage) en TDD, avec CI via GitHub Actions.

## Prérequis
- Python 3.10+ (ou 3.11/3.12)
- unittest (inclus avec Python)

## Installation (optionnelle, local)
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (Git Bash):
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Lancer les tests
```bash
python -m unittest discover -s tests -p "test_*.py" -v
``` 