# QA Test Automation Portfolio

Projet d'automatisation de tests avec **Playwright** (Python), réalisé dans le cadre de ma formation en test logiciel / QA.

## 📖 Contexte et démarche

Ce projet a initialement démarré sur le site **Guru99 Bank**, une référence classique en formation QA. En cours de route, j'ai découvert que le site avait changé de fonctionnement : les identifiants ne sont plus fixes et publics, mais générés à la demande par email et valables seulement 20 jours — ce qui rendait le projet non reproductible pour qui voudrait cloner ce repo.

J'ai donc choisi de basculer sur **Sauce Demo**, un site reconnu dans l'industrie du test, avec des comptes utilisateurs fixes et stables, adaptés à un projet de démonstration durable.

## 🎯 Objectif

Mettre en pratique les compétences d'un testeur logiciel : conception de scénarios de test, automatisation, couverture des cas positifs et négatifs.

## 🛠️ Stack technique

- **Python 3.14**
- **Playwright** (pytest-playwright)
- **pytest**

## 🌐 Site testé

[Sauce Demo](https://www.saucedemo.com/) — site e-commerce de démonstration conçu pour l'apprentissage de l'automatisation de tests, avec plusieurs comptes utilisateurs simulant différents scénarios (connexion valide, compte bloqué, bugs visuels).

## ✅ Tests actuels

| Test | Description |
|------|-------------|
| `test_login_standard_user` | Vérifie qu'un utilisateur valide accède bien à la page d'inventaire après connexion |
| `test_login_locked_out_user` | Vérifie qu'un message d'erreur explicite s'affiche pour un compte bloqué |
| `test_add_product_to_cart` | Vérifie qu'un produit ajouté au panier met bien à jour le badge du panier |
| `test_checkout_full_flow` | Parcours complet : connexion → ajout au panier → checkout → confirmation de commande |

## 🚀 Comment lancer les tests

1. Cloner le repo
```bash
   git clone https://github.com/yasmine-qa/qa-test-automation-portfolio.git
   cd qa-test-automation-portfolio
```

2. Installer les dépendances
```bash
   pip install pytest-playwright
   playwright install
```

3. Lancer les tests
```bash
   pytest -v
```

## 📌 Prochaines étapes

- [x] Ajouter des tests sur le panier et le processus de commande (checkout)
- [x] Restructurer le code en Page Object Model (POM)
- [ ] Mettre en place une CI/CD avec GitHub Actions
- [ ] Ajouter des tests avec Selenium en complément de Playwright

## 👤 Auteure

**Yasmine** — En formation testeuse logicielle (QA), à la recherche d'un poste de testeuse junior.
Intérêt particulier pour l'automatisation de tests et les bonnes pratiques de qualité logicielle.


