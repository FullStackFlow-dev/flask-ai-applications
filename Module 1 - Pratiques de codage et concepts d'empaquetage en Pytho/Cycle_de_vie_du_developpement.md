# Cycle de vie du développement d'applications

## Objectifs pédagogiques

Après avoir visionné cette vidéo, vous serez capable de :

- Lister les étapes du cycle de vie du développement d'applications
- Décrire les différentes phases de ce cycle
- Comprendre l'importance d'écrire le code de l'application dans plusieurs fichiers

---

## Introduction

Imaginez qu'un client vous demande de créer une application pour aider ses employés à **suivre leurs tâches quotidiennes**. Imaginez maintenant une application de **réservations d'hôtel**, de la création à la sortie du client.

Dans les deux cas, pouvez-vous commencer à développer l'application dès que le client fait sa demande ? **Pas vraiment !**

Vous devrez effectuer certaines activités telles que l'analyse des besoins, la planification et le codage avant que l'application ne soit prête pour les utilisateurs.

> Quel que soit le type d'application, chaque application passe par différentes phases, appelées **cycle de vie du développement applicatif**.

---

## Les 7 phases du cycle de vie

```
Recueil des besoins → Analyse → Conception → Codage & Tests → Tests utilisateur → Production → Maintenance
```

---

### 1. 📋 Recueil des besoins

Durant cette phase, vous recensez les besoins relatifs à **tous les aspects de l'application** :

| Type de besoin | Exemple (application hôtel) |
|---|---|
| **Utilisateur** | Consulter les chambres et équipements disponibles |
| **Métier** | Déterminer le tarif approprié pour les chambres et prestations |
| **Technique** | Compatibilité avec tous les navigateurs et appareils mobiles |

**Objectif :** recenser un maximum d'exigences, même celles qui semblent redondantes ou triviales.

Il est également essentiel d'identifier les **contraintes de conception** et de **viabilité du modèle économique**.

> **Exemple de contrainte :** pour une application de réservation d'hôtel, le serveur doit maintenir à jour en permanence le statut de disponibilité des chambres, ce qui engendre des coûts. Pour assurer la viabilité de l'entreprise, des frais de service minimes sont ajoutés au paiement final.

---

### 2. 🔍 Analyse

Après avoir rassemblé les exigences et les contraintes, il convient de les **analyser** afin de proposer une solution pour la conception de l'application.

---

### 3. 🎨 Conception

Lors des phases d'analyse et de conception, plusieurs **cycles de vérification et de révision** peuvent être nécessaires pour créer une solution modèle répondant à toutes les exigences spécifiées.

Tout au long de ces phases, il est impératif de **maintenir une documentation rigoureuse**, consignant toutes les mises à jour de la conception.

- Cette documentation doit être **claire et concise**
- Elle sert de **référence lors des phases de codage et de test**

---

### 4. 💻 Codage et tests

Durant cette phase, l'équipe utilise les exigences de programmation définies dans la documentation de conception pour :

1. **Coder** les programmes de l'application
2. **Tester** le code
3. **Réviser** selon les résultats
4. **Retester** jusqu'à ce que le code réponde à toutes les exigences documentées

#### Types de tests

| Type de test | Description |
|---|---|
| **Tests unitaires** | Tests au niveau de la programmation pour vérifier toutes les spécifications requises |
| **Tests d'intégration** | Vérifient que les composants fonctionnent correctement après intégration et au sein d'un framework plus vaste |
| **Tests de performance** | Évaluent le comportement de l'application en fonction de différentes charges de travail |
| **Tests utilisateur** | Vérifient les fonctionnalités du point de vue de l'utilisateur |

---

### 5. 🚀 Production (Déploiement)

Après les tests, vous pouvez générer une nouvelle version de l'application et la **déployer en production**.

- Les utilisateurs finaux peuvent y accéder et l'utiliser
- Vous devez vous assurer que l'application **fonctionne correctement** et est **accessible**
- Dans un état stable, **aucune modification** ne doit être apportée à l'application

> **Cependant**, des modifications peuvent être nécessaires en cas d'erreur. Ces modifications sont rigoureusement contrôlées et testées de manière approfondie avant leur mise en production.

---

### 6. 🔧 Maintenance

La dernière phase du cycle de vie. L'application peut nécessiter :

- Une **mise à jour**
- L'**ajout de nouvelles fonctionnalités**

> Dans ce cas, les nouvelles fonctionnalités doivent passer par **toutes les phases précédentes** avant d'être intégrées à la version de l'application déployée en production.

---

## Bonne pratique : organisation en plusieurs fichiers

Chaque application possède généralement **plusieurs fonctionnalités**, et les exigences de chacune d'elles peuvent varier.

### Approche recommandée

```
application/
├── main.py           ← Programme central (point d'entrée)
├── feature_a.py      ← Fonctionnalité A
├── feature_b.py      ← Fonctionnalité B
└── feature_c.py      ← Fonctionnalité C
```

- **Coder chaque fonctionnalité dans un fichier séparé**
- Créer un **programme central** qui exécute l'application et appelle les différents fichiers pour réaliser des fonctions spécifiques

### Avantages

| Avantage | Explication |
|---|---|
| **Maintenance facilitée** | Chaque fichier est indépendant et facile à modifier |
| **Ajout de fonctionnalités simplifié** | Seul le nouveau fichier suit le processus complet de conception et vérification |
| **Lisibilité** | Le code est mieux organisé et plus compréhensible |

---

## Résumé

Le cycle de vie du développement d'une application comporte **7 phases** :

| # | Phase | Description |
|---|---|---|
| 1 | **Recueil des besoins** | Collecte des exigences utilisateur, métier et techniques |
| 2 | **Analyse** | Analyse des exigences et contraintes |
| 3 | **Conception** | Conception de la solution avec documentation rigoureuse |
| 4 | **Codage et tests** | Développement et test des différents composants |
| 5 | **Tests utilisateur** | Tests d'intégration et de performance pour tous les utilisateurs finaux |
| 6 | **Production** | Déploiement et mise à disposition aux utilisateurs |
| 7 | **Maintenance** | Mise à jour et correction des problèmes |

> 💡 **À retenir :** utilisez un **programme central** pour appeler les fichiers et fonctions individuels et effectuer différentes actions — cela facilite la maintenance et l'évolution de votre application.
