# Bug Report #001 — Images de produits incorrectes avec `problem_user`

## Résumé
Lors de la connexion avec le compte `problem_user`, les images des produits affichées sur la page d'inventaire ne correspondent pas aux produits réels.

## Environnement
- **Site** : Sauce Demo (saucedemo.com)
- **Navigateur** : Chromium (Playwright)
- **Compte utilisé** : `problem_user` / `secret_sauce`

## Étapes de reproduction
1. Aller sur `https://www.saucedemo.com/`
2. Se connecter avec `problem_user` / `secret_sauce`
3. Observer les images des produits sur la page d'inventaire

## Résultat attendu
Chaque produit affiche une image qui lui correspond (ex : le sac à dos "Sauce Labs Backpack" affiche une image de sac à dos).

## Résultat obtenu
Toutes les images de produits affichent la même image (celle d'un chien), sans rapport avec les produits réels.

## Sévérité
**Mineure** — n'empêche pas l'utilisation du site, mais nuit à l'expérience utilisateur et à la confiance dans le catalogue.

## Statut
Connu et volontaire — ce compte est spécifiquement conçu par Sauce Demo pour simuler des bugs visuels à des fins d'entraînement en test exploratoire.
