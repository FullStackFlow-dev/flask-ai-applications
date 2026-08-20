"""Fonctions simples servant à illustrer un module Python testable."""


def word_count(text: str) -> int:
    """Retourner le nombre de mots non vides dans *text*.

    Raises:
        TypeError: Si la valeur fournie n'est pas une chaîne.
    """
    if not isinstance(text, str):
        raise TypeError("text doit être une chaîne de caractères")
    return len(text.split())
