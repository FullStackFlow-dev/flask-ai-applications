"""Moteur local, déterministe et remplaçable de détection d'émotions.

Il offre une démonstration utilisable sans clé API. Pour un déploiement réel,
remplacez cette implémentation par un fournisseur IA dans un module séparé,
chargé depuis les variables d'environnement.
"""

from __future__ import annotations

from collections import Counter

EMOTION_KEYWORDS = {
    "joy": {"heureux", "heureuse", "joie", "super", "excellent", "ravi"},
    "sadness": {"triste", "tristesse", "déçu", "déçue", "malheureux"},
    "anger": {"colère", "furieux", "furieuse", "énervé", "injuste"},
    "fear": {"peur", "inquiet", "inquiète", "angoisse", "effrayé"},
}


def detect_emotions(text: str) -> dict[str, object]:
    """Analyser un texte et retourner les scores et l'émotion dominante.

    Raises:
        ValueError: Si le texte est vide ou ne contient que des espaces.
        TypeError: Si la valeur n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text doit être une chaîne de caractères")
    if not text.strip():
        raise ValueError("Le texte à analyser est obligatoire.")

    tokens = [token.strip('.,;:!?()[]"').lower() for token in text.split()]
    hits = Counter(
        emotion
        for emotion, keywords in EMOTION_KEYWORDS.items()
        for token in tokens
        if token in keywords
    )
    scores = {
        emotion: round(hits[emotion] / max(len(tokens), 1), 2)
        for emotion in EMOTION_KEYWORDS
    }
    dominant = max(scores, key=scores.get) if any(scores.values()) else "neutral"
    return {"dominant_emotion": dominant, "scores": scores, "provider": "local-demo"}
