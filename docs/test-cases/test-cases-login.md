# Cas de test — Connexion (US-01)

## TC-01 : Connexion avec des identifiants valides

| Champ | Détail |
|---|---|
| **Préconditions** | L'utilisateur est sur la page de connexion (`saucedemo.com`) |
| **Étapes** | 1. Saisir `standard_user` dans le champ Username <br> 2. Saisir `secret_sauce` dans le champ Password <br> 3. Cliquer sur "Login" |
| **Résultat attendu** | L'utilisateur est redirigé vers la page d'inventaire (`/inventory.html`) |
| **Statut** | ✅ Automatisé (`test_login_standard_user`) |

---

## TC-02 : Connexion avec un compte bloqué

| Champ | Détail |
|---|---|
| **Préconditions** | L'utilisateur est sur la page de connexion |
| **Étapes** | 1. Saisir `locked_out_user` dans le champ Username <br> 2. Saisir `secret_sauce` dans le champ Password <br> 3. Cliquer sur "Login" |
| **Résultat attendu** | Un message d'erreur s'affiche : "Epic sadface: Sorry, this user has been locked out." |
| **Statut** | ✅ Automatisé (`test_login_locked_out_user`) |

---

## TC-03 : Connexion avec un mot de passe vide

| Champ | Détail |
|---|---|
| **Préconditions** | L'utilisateur est sur la page de connexion |
| **Étapes** | 1. Saisir `standard_user` dans le champ Username <br> 2. Laisser le champ Password vide <br> 3. Cliquer sur "Login" |
| **Résultat attendu** | Un message d'erreur s'affiche indiquant que le mot de passe est requis |
| **Statut** | ⏳ Non automatisé — cas exploratoire manuel |
