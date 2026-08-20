# Introduction aux applications web et aux API

## Objectifs pédagogiques

Après avoir visionné cette vidéo, vous serez capable de :

- Décrire les **applications web**
- Décrire une **interface de programmation d'application (API)**
- **Comparer** les applications web et les API

---

## 1. Les applications web

### Définition

Une **application web** est un programme stocké sur un serveur distant et accessible via Internet. L'utilisateur interagit avec l'application à l'aide d'un **navigateur**.

> Bien que certaines applications puissent dépendre du navigateur utilisé, la plupart des applications web fonctionnent sur tous les navigateurs web modernes.

### Les trois composants d'une application web

Une application web nécessite **trois composants** pour traiter une requête client :

| Composant | Rôle |
|---|---|
| **Serveur web** | Gérer les requêtes entrantes |
| **Serveur d'applications** | Exécuter la tâche demandée |
| **Base de données** | Stocker les informations nécessaires à l'exécution de la tâche |

### Technologies de développement

| Côté | Technologies |
|---|---|
| **Front-end** (interface utilisateur) | JavaScript, HTML, CSS |
| **Back-end** (serveur) | Python, Java, Ruby |

### Avantages des applications web

- ✅ Mise à disposition de l'application pour **plusieurs utilisateurs simultanément**
- ✅ Accessibles depuis la **plateforme de leur choix** (ordinateur de bureau, ordinateur portable ou appareil mobile)
- ✅ Accessibles via le **navigateur de leur choix**
- ✅ **Aucune installation** requise sur le système de l'utilisateur

---

## 2. Les API (Application Programming Interface)

### Définition

Une **API** est un composant logiciel qui permet à **deux applications non connectées de communiquer**.

Les API offrent une plus grande flexibilité aux développeurs et leur permettent d'interroger des applications qui, autrement, resteraient fermées.

De ce fait, les API possèdent des **règles et fonctions standardisées** qui déterminent :
- Quelles données peuvent être **extraites ou modifiées** au sein d'une application
- **Comment** ce processus se déroule

### Exemple concret — Application météo

> Une application météo **ne génère pas elle-même de données météorologiques** ; elle se contente de les afficher.
>
> L'**API** connecte le logiciel qui collecte et stocke les données météorologiques à l'application sur votre appareil mobile. Ce dernier vous fournit ensuite des prévisions détaillées pour le lendemain.

Un autre exemple : les applications de votre téléphone nécessitent votre autorisation pour accéder à différentes fonctionnalités telles que la **géolocalisation, l'appareil photo, l'audio et l'enregistreur**.

### Architectures d'API

Plusieurs architectures sont utilisées par les développeurs pour créer une API. Les plus courantes sont :

| Architecture | Nom complet |
|---|---|
| **REST** | Representational State Transfer |
| **SOAP** | Simple Object Access Protocol |

> Ces architectures seront abordées dans une autre vidéo.

### Avantages des API

- ✅ Améliore la **connectivité** entre les applications
- ✅ Prend en charge les opérations **CRUD** (Création, Lecture, Mise à jour, Suppression)
- ✅ Compatible avec les **verbes HTTP** : `PUT`, `POST`, `DELETE`, `GET`
- ✅ Basée sur HTTP, elle est **personnalisable**

---

## 3. Applications web vs API — Comparaison

### Exemple : site de commerce électronique

```
Navigateur (desktop)          →  API  →  Application web
Application mobile (téléphone) →  API  →  Application web
```

- Lorsque vous accédez au site depuis un **navigateur**, ce dernier fait office d'API et vous connecte à l'application web.
- Lorsque vous sélectionnez un produit, l'application **vérifie sa disponibilité** et affiche son prix.
- Depuis un **appareil mobile**, c'est l'application installée sur votre appareil qui fait office d'API et se connecte au site.

### Relation entre applications web et API

> La nature même des applications web est de **partager des données** avec d'autres applications ; en substance, toutes les applications web peuvent être considérées comme des API.

Cependant, le terme **API est générique** et englobe :
- Les applications **« en ligne »** (ou web)
- Les applications **« hors ligne »**

| Affirmation | Vrai / Faux |
|---|---|
| Toutes les applications web sont des API | ✅ Vrai |
| Toutes les API sont des applications web | ❌ Faux |

---

## Résumé

| Concept | Points clés |
|---|---|
| **Application web** | Programme sur serveur distant, accessible via navigateur, multi-plateforme, sans installation |
| **API** | Composant logiciel de communication entre deux applications non connectées, règles standardisées |
| **Différence clé** | Toutes les applications web sont des API, mais toutes les API ne nécessitent pas un réseau comme les applications web |

> 💡 **À retenir :** les deux permettent le **partage de données** entre applications, mais toutes les API ne nécessitent pas de réseau comme les applications web.
