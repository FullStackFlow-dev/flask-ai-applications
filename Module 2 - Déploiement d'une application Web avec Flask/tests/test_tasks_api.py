"""Tests de l'API CRUD Flask."""

import sys
from pathlib import Path

MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from flask_crud_api import create_app  # noqa: E402


def test_create_and_list_task():
    """Une tâche créée doit apparaître dans la collection."""
    client = create_app({"TESTING": True}).test_client()
    created = client.post("/api/tasks", json={"title": "Écrire les tests"})

    assert created.status_code == 201
    assert created.get_json()["done"] is False
    assert client.get("/api/tasks").get_json() == [created.get_json()]


def test_empty_title_is_rejected():
    """Une requête incomplète doit renvoyer une erreur 400."""
    response = (
        create_app({"TESTING": True})
        .test_client()
        .post("/api/tasks", json={"title": "  "})
    )

    assert response.status_code == 400


def test_unknown_task_returns_404():
    """Une tâche inexistante doit renvoyer une erreur JSON."""
    response = create_app({"TESTING": True}).test_client().get("/api/tasks/99")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Tâche introuvable."
