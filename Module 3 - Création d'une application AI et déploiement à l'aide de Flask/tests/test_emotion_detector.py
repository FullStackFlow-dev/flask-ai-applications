"""Tests du moteur et de l'API de détection d'émotions."""

import sys
from pathlib import Path

import pytest

MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from emotion_detector.app import create_app  # noqa: E402
from emotion_detector.service import detect_emotions  # noqa: E402


def test_detects_joy_as_dominant_emotion():
    """Le mot-clé de joie doit être identifiable."""
    result = detect_emotions("Je suis ravi, cette démonstration est excellente !")

    assert result["dominant_emotion"] == "joy"
    assert result["provider"] == "local-demo"


def test_empty_text_is_rejected():
    """Le service ne doit pas analyser du texte vide."""
    with pytest.raises(ValueError, match="obligatoire"):
        detect_emotions("   ")


def test_api_returns_validation_error():
    """L'API doit traduire l'erreur de validation en HTTP 400."""
    response = (
        create_app({"TESTING": True})
        .test_client()
        .post("/api/analyze", json={"text": ""})
    )

    assert response.status_code == 400
    assert "error" in response.get_json()
