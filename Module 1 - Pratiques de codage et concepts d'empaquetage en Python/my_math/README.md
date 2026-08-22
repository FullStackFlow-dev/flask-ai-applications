# Paquet `my_math`

Paquet Python du Module 1 regroupant des fonctions mathématiques de base organisées en deux modules : `basic` et `stats`.

---

## Structure

```
my_math/
├── basic.py   # Opérations arithmétiques : square, double, add
├── stats.py   # Fonctions statistiques  : mean, median
└── README.md  # Ce fichier
```

---

## Module `basic.py` — Opérations arithmétiques

### `square(number: float) -> float`

Retourne le carré d'un nombre.

```python
from my_math.basic import square

square(4)   # → 16
square(2.5) # → 6.25
```

### `double(number: float) -> float`

Retourne le double d'un nombre.

```python
from my_math.basic import double

double(3)   # → 6
double(1.5) # → 3.0
```

### `add(a: float, b: float) -> float`

Retourne la somme de deux nombres.

```python
from my_math.basic import add

add(2, 3)     # → 5
add(1.5, 2.5) # → 4.0
```

---

## Module `stats.py` — Fonctions statistiques

### Comprendre le code

#### `mean(numbers: list[float]) -> float`

Cette fonction prend une liste de nombres et renvoie leur moyenne.
Elle utilise la fonction intégrée `sum()` de Python pour additionner toutes les valeurs
de la liste et `len()` pour obtenir le nombre d'éléments, puis divise les deux pour
produire la moyenne.

```python
from my_math.stats import mean

mean([1, 2, 3, 4, 5]) # → 3.0
mean([10, 20, 30])     # → 20.0
```

> **Signature** : `numbers: list[float] -> float`  
> **Précondition** : la liste ne doit pas être vide.

---

#### `median(numbers: list[float]) -> float`

Cette fonction prend une liste de nombres et renvoie la valeur médiane.

Elle commence par trier la liste en ordre croissant en utilisant `sorted()` — la liste
originale **n'est pas modifiée** (contrairement à `.sort()`), puisque la médiane dépend
de la position des éléments.

Elle vérifie ensuite si la liste a un nombre **pair** ou **impair** d'éléments :

- **Nombre pair** : il n'y a pas de valeur médiane unique. La fonction sélectionne les
  deux éléments du milieu aux positions `milieu - 1` et `milieu` (où
  `milieu = len(triee) // 2`), et retourne leur moyenne.
- **Nombre impair** : il y a un seul élément médian, retourné directement à l'index
  `len(triee) // 2`.

```python
from my_math.stats import median

median([3, 1, 4, 1, 5])    # → 3   (impair : élément central)
median([1, 2, 3, 4])        # → 2.5 (pair   : moyenne de 2 et 3)
```

> **Signature** : `numbers: list[float] -> float`  
> **Précondition** : la liste ne doit pas être vide.

---

## Utilisation combinée

```python
from my_math.basic import square, double, add
from my_math.stats import mean, median

valeurs = [4, 9, 16, 25]

print(mean(valeurs))    # → 13.5
print(median(valeurs))  # → 12.5
print(add(square(2), double(3)))  # → 4 + 6 = 10
```
