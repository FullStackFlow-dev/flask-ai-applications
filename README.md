# Développer des applications d'IA avec Python et Flask

Dépôt personnel d'apprentissage inspiré du parcours IBM/Coursera **Developing AI Applications with Python and Flask**. Le code et les notes ajoutés ici sont des implémentations originales ; ils ne remplacent ni ne reproduisent les supports, laboratoires ou évaluations Coursera.

## Parcours du dépôt

| Module | Objectif | Réalisation |
| --- | --- | --- |
| 1 | Style Python, tests et packaging | `learning_tools`, tests unitaires et configuration qualité |
| 2 | Flask, routes, erreurs et CRUD | API REST de tâches dans `flask_crud_api` |
| 3 | Application IA avec Flask | Détecteur d'émotions dans `emotion_detector` |

Le détail des objectifs et des commandes est dans [docs/PLAN_DE_TRAVAIL.md](docs/PLAN_DE_TRAVAIL.md).

## Installation

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Copiez ensuite `.env.example` vers `.env` si vous souhaitez renseigner des identifiants externes. Ne versionnez jamais ce fichier.

## Lancer les applications

```powershell
# Module 2 : API CRUD
python "Module 2 - Déploiement d'une application Web avec Flask/flask_crud_api/app.py"

# Module 3 : interface de détection d'émotions
python "Module 3 - Création d'une application AI et déploiement à l'aide de Flask/emotion_detector/app.py"
```

Les deux serveurs écoutent par défaut sur `http://127.0.0.1:5000`; lancez-les séparément.

## Vérifications

```powershell
python -m pytest
python -m black --check .
python -m pylint "Module 1 - Pratiques de codage et concepts d'empaquetage en Python/learning_tools"
```

## GitHub

```powershell
git init
git add .
git commit -m "Initialiser le dépôt d'apprentissage Flask et IA"
git branch -M main
git remote add origin <URL_DE_VOTRE_DEPOT_GITHUB>
git push -u origin main
```

Avant le `git add`, vérifiez avec `git status` qu'aucun secret ni le dossier `venv/` ne sont inclus.
