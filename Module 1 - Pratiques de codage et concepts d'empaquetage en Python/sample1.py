"""Module pour additionner deux nombres."""


def add(number1, number2):
    """Retourne la somme de number1 et number2."""
    return number1 + number2


NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
