# Changelog — Journal des modifications

Toutes les modifications, erreurs détectées, corrections et commits sont documentés ici.  
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

Catégories utilisées :
- **Ajouté** — nouveaux fichiers ou fonctionnalités
- **Modifié** — changements sur des fichiers existants
- **Supprimé** — fichiers ou lignes retirés
- **Corrigé** — bugs ou erreurs résolus
- **Erreur** — problème identifié (avant correction)

---

## [Non publié] — en cours

### Ajouté
- [`Module 1/.../tests/test_modulaire.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/tests/test_modulaire.py)
  — Tests modulaires organisés en deux classes `pytest` :
  - `TestWordCountValides` (6 cas) : phrase normale, chaîne vide, espaces multiples, un mot, espaces seuls, ponctuation
  - `TestWordCountInvalides` (4 cas) : `int`, `list`, `None`, `float` → vérifie que `TypeError` est levée
- [`Module 1/.../sample1.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/sample1.py)
  — Fichier d'exploration et d'exemples du Module 1
- [`CHANGELOG.md`](CHANGELOG.md)
  — Ce fichier, journal exhaustif des modifications du projet

---

## [dacca03] — 2026-08-20 · *Configurer le venv Python 3.14*

### Erreur identifiée
- [`pyproject.toml`](pyproject.toml) — `target-version = ["py313"]` pointait vers Python 3.13 alors que l'environnement actif est Python 3.14
- [`.vscode/settings.json`](.vscode/settings.json) — `python.defaultInterpreterPath` manquait après la suppression du commit précédent (`81823b6`), VS Code ne trouvait plus le bon interpréteur

### Corrigé
- [`pyproject.toml`](pyproject.toml) — `target-version` mis à jour : `py313` → `py314`
- [`.vscode/settings.json`](.vscode/settings.json) — réintégration de `"python.defaultInterpreterPath"` pointant vers `${workspaceFolder}\\venv\\Scripts\\python.exe`

---

## [81823b6] — 2026-08-20 · *Retirer la référence au venv Python 3.13*

### Erreur identifiée
- [`.vscode/settings.json`](.vscode/settings.json) — `python.defaultInterpreterPath` référençait un venv Python 3.13 qui n'existait plus / n'était plus utilisé

### Supprimé
- [`.vscode/settings.json`](.vscode/settings.json) — retrait de la clé `"python.defaultInterpreterPath"` obsolète (venv Python 3.13)

> ⚠️ Ce retrait a été incomplet : la clé a dû être réintroduite dans le commit suivant `dacca03` en la corrigeant vers le bon venv.

---

## [02e8793] — 2026-08-20 · *Configurer VS Code et corriger les imports Python*

### Erreurs identifiées & corrigées

#### 🐛 Erreur 1 — Nom de dossier tronqué (Module 1)
- **Problème** : le dossier du Module 1 avait été créé avec un nom tronqué :
  `Module 1 - Pratiques de codage et concepts d'empaquetage en **Pytho**`
  au lieu de `…en **Python**`
- **Impact** : tous les chemins vers `learning_tools`, `tests/`, `.md` étaient cassés ; `pylint`, `pytest` et les imports échouaient
- **Correction** : renommage du dossier + migration de tous les fichiers concernés :

| Fichier déplacé | Ancien chemin (tronqué) | Nouveau chemin (correct) |
|---|---|---|
| `Cycle_de_vie_du_developpement.md` | `…Pytho/` | `…Python/` |
| `Introduction_applications_web_et_API.md` | `…Pytho/` | `…Python/` |
| `Python_Flask_projets_grande_echelle.md` | `…Pytho/` | `…Python/` |
| `learning_tools/__init__.py` | `…Pytho/` | `…Python/` |
| `learning_tools/text_metrics.py` | `…Pytho/` | `…Python/` |
| `tests/test_text_metrics.py` | `…Pytho/` | `…Python/` |

#### 🐛 Erreur 2 — `welcome.py` incorrect supprimé
- **Problème** : [`Module 1 - .../Pytho/welcome.py`] contenait du code NumPy (`np.array`) sans rapport avec le Module 1
- **Correction** : suppression de ce fichier erroné et création d'un [`welcome.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/welcome.py) correct avec un simple message de bienvenue

#### 🐛 Erreur 3 — Chemin tronqué dans `README.md`
- **Problème** : commande `pylint` dans [`README.md`](README.md) référençait le mauvais chemin :
  ```
  "…en Pytho/learning_tools"   ← cassé
  ```
- **Correction** :
  ```
  "…en Python/learning_tools"  ← correct
  ```

#### 🐛 Erreur 4 — Chemin tronqué dans `pyproject.toml`
- **Problème** : `testpaths` dans [`pyproject.toml`](pyproject.toml) pointait vers le mauvais dossier :
  ```toml
  "Module 1 - Pratiques de codage et concepts d'empaquetage en Pytho/tests"
  ```
- **Correction** :
  ```toml
  "Module 1 - Pratiques de codage et concepts d'empaquetage en Python/tests"
  ```

#### 🐛 Erreur 5 — `.gitignore` excluait tout `.vscode/`
- **Problème** : `.gitignore` contenait `.vscode/` ce qui empêchait de versionner `settings.json` et `extensions.json`
- **Correction** : remplacement par une règle plus fine :
  ```gitignore
  .vscode/*
  !.vscode/settings.json
  !.vscode/extensions.json
  ```

### Ajouté
- [`.vscode/extensions.json`](.vscode/extensions.json) — recommandations d'extensions VS Code (`ms-python.python`, `pylance`, `black-formatter`, `isort`)
- [`.vscode/settings.json`](.vscode/settings.json) — configuration VS Code : interpréteur Python, `extraPaths` des 3 modules, `pytest` activé, `unittest` désactivé
- [`Module 1/.../software101/software.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/software101/software.py) — script d'illustration NumPy (`np.array`)
- [`Module 1/.../welcome.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/welcome.py) — script de bienvenue (`print("Welcome to the world of programming!")`)

---

## [d354a50] — 2026-08-20 · 🎉 *Initialiser le parcours Flask et IA*

### Ajouté — 21 fichiers, 982 insertions

#### Structure du projet
- **Module 1** — Style Python, tests et packaging :
  - [`learning_tools/__init__.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/learning_tools/__init__.py) — paquet Python exposant `word_count`
  - [`learning_tools/text_metrics.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/learning_tools/text_metrics.py) — fonction `word_count(text: str) -> int`
  - [`tests/test_text_metrics.py`](Module%201%20-%20Pratiques%20de%20codage%20et%20concepts%20d'empaquetage%20en%20Python/tests/test_text_metrics.py) — 3 tests unitaires `pytest`
  - `welcome.py` — script initial (remplacé dans `02e8793`)
  - 3 fichiers `.md` de notes de cours

- **Module 2** — API REST CRUD avec Flask :
  - `flask_crud_api/__init__.py`, `flask_crud_api/app.py` — application Flask (84 lignes)
  - `tests/test_tasks_api.py` — 38 lignes de tests

- **Module 3** — Application IA avec Flask :
  - `emotion_detector/__init__.py`, `app.py`, `service.py`, `templates/index.html`
  - `tests/test_emotion_detector.py` — 38 lignes de tests

#### Fichiers de configuration
- [`README.md`](README.md) — documentation principale (57 lignes)
- [`docs/PLAN_DE_TRAVAIL.md`](docs/PLAN_DE_TRAVAIL.md) — plan de travail détaillé
- [`requirements.txt`](requirements.txt) — 97 lignes, dépendances des 3 modules
- [`pyproject.toml`](pyproject.toml) — configuration `pytest`, `black`, `pylint`, `isort`
- [`.gitignore`](.gitignore) — exclusions Git (`venv/`, `.env`, `__pycache__`, `*.db`, `.vscode/`)
- [`.env.example`](.env.example) — modèle de variables d'environnement (clés IBM Watson, OpenAI, Flask)
