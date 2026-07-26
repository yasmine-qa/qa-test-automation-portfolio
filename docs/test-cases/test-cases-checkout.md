# Cas de test — Panier et Checkout (US-02, US-03)

## TC-04 : Ajout d'un produit au panier

| Champ | Détail |
|---|---|
| **Préconditions** | L'utilisateur est connecté et sur la page d'inventaire |
| **Étapes** | 1. Cliquer sur "Add to cart" pour le produit "Sauce Labs Backpack" |
| **Résultat attendu** | Le badge du panier affiche "1" |
| **Statut** | ✅ Automatisé (`test_add_product_to_cart`) |

---

## TC-05 : Parcours complet de commande

| Champ | Détail |
|---|---|
| **Préconditions** | L'utilisateur est connecté, un produit est dans le panier |
| **Étapes** | 1. Aller dans le panier <br> 2. Cliquer sur "Checkout" <br> 3. Remplir prénom, nom, code postal <br> 4. Cliquer sur "Continue" <br> 5. Cliquer sur "Finish" |
| **Résultat attendu** | Le message "Thank you for your order!" s'affiche |
| **Statut** | ✅ Automatisé (`test_checkout_full_flow`) |

---

## TC-06 : Checkout avec un champ obligatoire manquant

| Champ | Détail |
|---|---|
| **Préconditions** | L'utilisateur est sur la page de checkout (étape 1) |
| **Étapes** | 1. Laisser le champ "Postal Code" vide <br> 2. Cliquer sur "Continue" |
| **Résultat attendu** | Un message d'erreur s'affiche : "Postal Code is required" |
| **Statut** | ⏳ Non automatisé — cas exploratoire manuel |
