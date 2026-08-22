# Résumé — Module 1 : Pratiques de codage et concepts d'empaquetage en Python

## Cycle de vie du développement d'une application

Le cycle de vie du développement d'une application comporte **sept phases** :

1. **La collecte des besoins** : Vous recueillez les besoins des utilisateurs, des entreprises et des techniciens pour l'application.
2. **L'analyse** : Vous analysez les besoins.
3. **Conception** : Vous concevez la solution complète.
4. **Code et test** : Vous construisez et testez les différents composants de l'application.
5. **Test de l'utilisateur et du système** : Les utilisateurs testent la convivialité de l'application, et vous effectuez des tests d'intégration du système et des tests de performance.
6. **Production** : L'application est disponible pour tous les utilisateurs finaux.
7. **Maintenance** : Vous mettez à niveau ou corrigez tout problème lié aux utilisateurs ou au système.

---

## Applications web et API

Toutes les applications web sont des API, mais toutes les API ne sont pas des applications web. Les deux partagent des données entre les applications, mais toutes les API ne nécessitent pas de réseaux comme les applications web.

---

## Lignes directrices PEP8 — Lisibilité du code

- Quatre espaces pour l'indentation
- Des lignes vides pour séparer les fonctions et les classes
- Espaces autour des opérateurs et après les virgules

---

## Conventions de codage PEP8 — Cohérence et facilité de gestion

- Ajoutez des blocs de code plus importants à l'intérieur des fonctions
- Nommez les fonctions et les fichiers en utilisant des **minuscules** et des **traits de soulignement**
- Nommez les classes en utilisant la **CamelCase**
- Nommez les constantes en **lettres majuscules** et séparez les mots par des traits de soulignement

---

## Analyse statique du code

Pour vous assurer que votre code respecte le style et les normes prédéfinis **sans l'exécuter**, vous pouvez utiliser la méthode d'**analyse statique du code**.

---

## Test unitaire

Le **test d'unité** est une méthode permettant de valider si les unités de code fonctionnent comme prévu. Vous devez tester chaque unité avant de l'intégrer à la base de code finale.

---

## Créer un package Python

Pour créer un paquetage :

1. Créez un dossier portant le nom du paquetage
2. Créez un fichier `__init__.py` vide
3. Créez les modules nécessaires
4. Dans le fichier `__init__.py`, ajoutez du code pour référencer les modules nécessaires au paquetage

> Vous pouvez vérifier le paquetage via le terminal bash dans un shell Python.
