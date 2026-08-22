"""Tests modulaires du paquet learning_tools.

Organisation par classes pour regrouper les cas de test par thème :
- TestWordCountValides   : entrées valides et cas limites
- TestWordCountInvalides : types incorrects et erreurs attendues
"""

import sys
from pathlib import Path

import pytest

MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from learning_tools import word_count  # noqa: E402


# Cas valides

class TestWordCountValides:
    """Tests sur des entrées valides de word_count."""

    def test_phrase_normale(self):
        """Une phrase classique doit retourner le bon nombre de mots."""
        assert word_count("Bonjour le monde") == 3

    def test_chaine_vide(self):
        """Une chaîne vide doit retourner 0."""
        assert word_count("") == 0

    def test_espaces_multiples(self):
        """Les espaces répétés ne doivent pas créer de mots fantômes."""
        assert word_count("  Flask   rend  le web simple ") == 5

    def test_un_seul_mot(self):
        """Une chaîne avec un seul mot doit retourner 1."""
        assert word_count("Python") == 1

    def test_chaine_espaces_uniquement(self):
        """Une chaîne composée uniquement d'espaces doit retourner 0."""
        assert word_count("     ") == 0

    def test_mots_avec_ponctuation(self):
        """La ponctuation attachée à un mot compte comme un seul token."""
        assert word_count("Bonjour, monde!") == 2


# ---------------------------------------------------------------------------
# Cas invalides
# ---------------------------------------------------------------------------

class TestWordCountInvalides:
    """Tests sur des entrées invalides de word_count."""

    def test_entier_leve_type_error(self):
        """Un entier doit lever TypeError."""
        with pytest.raises(TypeError, match="chaîne"):
            word_count(42)  # type: ignore[arg-type]

    def test_liste_leve_type_error(self):
        """Une liste doit lever TypeError."""
        with pytest.raises(TypeError, match="chaîne"):
            word_count(["un", "deux"])  # type: ignore[arg-type]

    def test_none_leve_type_error(self):
        """None doit lever TypeError."""
        with pytest.raises(TypeError, match="chaîne"):
            word_count(None)  # type: ignore[arg-type]

    def test_flottant_leve_type_error(self):
        """Un flottant doit lever TypeError."""
        with pytest.raises(TypeError, match="chaîne"):
            word_count(3.14)  # type: ignore[arg-type]
