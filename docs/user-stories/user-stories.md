# User Stories — Sauce Demo

## US-01 : Connexion utilisateur
**En tant que** client de Sauce Demo,
**Je veux** me connecter avec mon identifiant et mon mot de passe,
**Afin de** accéder à mon espace personnel et consulter les produits disponibles.

### Critères d'acceptation
- Un utilisateur avec des identifiants valides accède à la page d'inventaire
- Un utilisateur avec un compte bloqué reçoit un message d'erreur explicite
- Le mot de passe n'est jamais affiché en clair dans le champ

---

## US-02 : Ajout d'un produit au panier
**En tant que** client connecté,
**Je veux** ajouter un produit à mon panier,
**Afin de** préparer ma commande.

### Critères d'acceptation
- Le badge du panier s'incrémente à chaque ajout
- Le produit ajouté reste visible dans le panier après navigation

---

## US-03 : Passage de commande (checkout)
**En tant que** client avec des produits dans mon panier,
**Je veux** finaliser ma commande en renseignant mes informations de livraison,
**Afin de** recevoir mes achats.

### Critères d'acceptation
- Les champs prénom, nom, et code postal sont obligatoires
- Un message de confirmation s'affiche après validation de la commande