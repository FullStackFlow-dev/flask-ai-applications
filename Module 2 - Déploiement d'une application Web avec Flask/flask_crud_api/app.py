"""API REST Flask originale illustrant les opérations CRUD."""

from __future__ import annotations

from itertools import count

from flask import Flask, jsonify, request


def create_app(test_config: dict | None = None) -> Flask:
    """Créer l'application et son stockage mémoire de démonstration."""
    app = Flask(__name__)
    app.config.from_mapping(TESTING=False)
    if test_config:
        app.config.update(test_config)

    tasks: dict[int, dict[str, object]] = {}
    next_identifier = count(1)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    @app.get("/api/tasks")
    def list_tasks():
        return jsonify(list(tasks.values()))

    @app.post("/api/tasks")
    def create_task():
        payload = request.get_json(silent=True)
        title = payload.get("title", "").strip() if isinstance(payload, dict) else ""
        if not title:
            return {"error": "Le champ 'title' est obligatoire."}, 400

        identifier = next(next_identifier)
        task = {"id": identifier, "title": title, "done": False}
        tasks[identifier] = task
        return jsonify(task), 201

    @app.get("/api/tasks/<int:task_id>")
    def get_task(task_id: int):
        return _task_or_404(tasks, task_id)

    @app.patch("/api/tasks/<int:task_id>")
    def update_task(task_id: int):
        task_or_response = _task_or_404(tasks, task_id)
        if not isinstance(task_or_response, dict):
            return task_or_response
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return {"error": "Un objet JSON est attendu."}, 400
        if "title" in payload:
            title = str(payload["title"]).strip()
            if not title:
                return {"error": "Le titre ne peut pas être vide."}, 400
            task_or_response["title"] = title
        if "done" in payload:
            task_or_response["done"] = bool(payload["done"])
        return jsonify(task_or_response)

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id: int):
        if task_id not in tasks:
            return {"error": "Tâche introuvable."}, 404
        del tasks[task_id]
        return "", 204

    @app.errorhandler(404)
    def not_found(_error):
        return {"error": "Ressource introuvable."}, 404

    return app


def _task_or_404(tasks: dict[int, dict[str, object]], task_id: int):
    """Renvoyer une tâche ou une réponse JSON 404."""
    task = tasks.get(task_id)
    if task is None:
        return {"error": "Tâche introuvable."}, 404
    return task


if __name__ == "__main__":
    create_app().run(debug=True)
