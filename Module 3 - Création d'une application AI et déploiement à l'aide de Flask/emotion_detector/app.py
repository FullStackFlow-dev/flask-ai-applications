"""Interface Flask de l'application de détection d'émotions."""

from __future__ import annotations

from emotion_detector.service import detect_emotions
from flask import Flask, jsonify, render_template, request


def create_app(test_config: dict | None = None) -> Flask:
    """Créer l'application Web et l'API JSON."""
    app = Flask(__name__)
    app.config.from_mapping(TESTING=False)
    if test_config:
        app.config.update(test_config)

    @app.get("/")
    def index() -> str:
        return render_template("index.html")

    @app.post("/api/analyze")
    def analyze():
        payload = request.get_json(silent=True)
        text = payload.get("text", "") if isinstance(payload, dict) else ""
        try:
            result = detect_emotions(text)
        except (TypeError, ValueError) as error:
            return {"error": str(error)}, 400
        return jsonify(result)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
