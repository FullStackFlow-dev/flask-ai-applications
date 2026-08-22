# Changelog : Journal des modifications

Toutes les modifications notables de ce projet sont documentées ici.  
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Non publié] — en cours

### Ajouté
- [`Module 1/.../tests/test_modulaire.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/tests/test_modulaire.py) — fichier de tests modulaires organisés en classes `pytest` (`TestWordCountValides` · 6 cas, `TestWordCountInvalides` · 4 cas)
- [`Module 1/.../sample1.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/sample1.py) — fichier d'exploration/exemples du Module 1

---

## [dacca03] — 2026-08-20

### Modifié
- [`pyproject.toml`](pyproject.toml) — mise à jour de l'interpréteur cible vers Python 3.14
- [`.vscode/settings.json`](.vscode/settings.json) — chemin du venv mis à jour vers l'environnement Python 3.14

---

## [81823b6] — 2026-08-20

### Supprimé
- [`.vscode/settings.json`](.vscode/settings.json) — retrait de la référence obsolète au venv Python 3.13

---

## [02e8793] — 2026-08-20

### Corrigé
- [`README.md`](README.md) — correction d'une faute de frappe dans la commande `pylint` : `Pytho/learning_tools` → `Python/learning_tools` (le chemin était tronqué et la commande échouait)

### Ajouté
- [`.vscode/extensions.json`](.vscode/extensions.json) — recommandations d'extensions VS Code pour le projet
- [`.vscode/settings.json`](.vscode/settings.json) — configuration de l'interpréteur Python, du linter et du formateur pour VS Code
- [`Module 1/.../software101/software.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/software101/software.py) — module d'illustration des concepts logiciels du Module 1
- [`Module 1/.../welcome.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/welcome.py) — script de bienvenue mis à jour

### Modifié
- [`.gitignore`](.gitignore) — ajout de règles supplémentaires d'exclusion
- [`pyproject.toml`](pyproject.toml) — ajustement de la configuration de l'interpréteur

---

## [d354a50] — 2026-08-20 — 🎉 Initialisation

### Ajouté
- Structure complète du projet en trois modules :
  - **Module 1** — `learning_tools` (paquet Python), `text_metrics.py`, `tests/test_text_metrics.py`, notes de cours (3 fichiers `.md`)
  - **Module 2** — `flask_crud_api` : API REST CRUD de tâches + tests
  - **Module 3** — `emotion_detector` : application IA Flask + service + template + tests
- [`README.md`](README.md) — documentation principale du projet
- [`docs/PLAN_DE_TRAVAIL.md`](docs/PLAN_DE_TRAVAIL.md) — plan de travail détaillé
- [`requirements.txt`](requirements.txt) — toutes les dépendances des trois modules
- [`pyproject.toml`](pyproject.toml) — configuration `pytest`, `black`, `pylint`, `isort`
- [`.gitignore`](.gitignore) — exclusions Git (venv, `.env`, `__pycache__`, etc.)
- [`.env.example`](.env.example) — modèle de variables d'environnement
