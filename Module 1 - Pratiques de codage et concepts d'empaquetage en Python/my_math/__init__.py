"""Paquet mathématique de base créé durant le module 1."""

from .basic import add, double, square
from .stats import mean, median
from .geometry import area_of_rectangle, area_of_circle

__all__ = ["square", "double", "add", "mean", "median", "area_of_rectangle", "area_of_circle"]
