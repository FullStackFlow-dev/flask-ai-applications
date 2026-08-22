"""Module de géométrie : calcul d'aires de formes géométriques."""

import math


def area_of_rectangle(length, width):
    """Retourne l'aire d'un rectangle.

    Args:
        length (float): La longueur du rectangle.
        width (float): La largeur du rectangle.

    Returns:
        float: L'aire du rectangle (length * width).
    """
    return length * width


def area_of_circle(radius):
    """Retourne l'aire d'un cercle.

    Args:
        radius (float): Le rayon du cercle.

    Returns:
        float: L'aire du cercle (π * radius²).
    """
    return math.pi * radius ** 2
