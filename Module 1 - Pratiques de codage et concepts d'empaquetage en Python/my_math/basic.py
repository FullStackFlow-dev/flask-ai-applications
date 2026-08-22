"""Opérations arithmétiques de base illustrant un module Python testable."""


def square(number: float) -> float:
    """Retourner le carré d'un nombre.

    Args:
        number: Le nombre à élever au carré.

    Returns:
        Le carré de *number*.
    """
    return number**2


def double(number: float) -> float:
    """Retourner le double d'un nombre.

    Args:
        number: Le nombre à doubler.

    Returns:
        Le double de *number*.
    """
    return number * 2


def add(a: float, b: float) -> float:
    """Retourner la somme de deux nombres.

    Args:
        a: Premier opérande.
        b: Deuxième opérande.

    Returns:
        La somme *a* + *b*.
    """
    return a + b
