"""Fonctions statistiques de base illustrant un module Python testable."""


def mean(numbers: list[float]) -> float:
    """Retourner la moyenne d'une liste de nombres.

    Args:
        numbers: Liste non vide de nombres.

    Returns:
        La moyenne arithmétique des éléments de *numbers*.
    """
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """Retourner la médiane d'une liste de nombres.

    La liste est triée en interne ; la liste originale n'est pas modifiée.

    Args:
        numbers: Liste non vide de nombres.

    Returns:
        La valeur médiane de *numbers*.
    """
    triee = sorted(numbers)
    milieu = len(triee) // 2

    if len(triee) % 2 == 0:
        return (triee[milieu - 1] + triee[milieu]) / 2
    return triee[milieu]
