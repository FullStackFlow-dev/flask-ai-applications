"""Tests unitaires du paquet learning_tools."""

import sys
from pathlib import Path

import pytest

MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from learning_tools import word_count  # noqa: E402


def test_word_count_ignores_extra_whitespace():
    """Les espaces répétées ne doivent pas créer de mots."""
    assert word_count("  Flask   rend  le web simple ") == 5


def test_word_count_accepts_empty_text():
    """Une chaîne vide contient zéro mot."""
    assert word_count("") == 0


def test_word_count_rejects_non_string():
    """L'API doit échouer explicitement sur un type inattendu."""
    with pytest.raises(TypeError, match="chaîne"):
        word_count(42)  # type: ignore[arg-type]
