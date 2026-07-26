# QA Test Automation Portfolio

[![Tests automatisés](https://github.com/yasmine-qa/qa-test-automation-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/yasmine-qa/qa-test-automation-portfolio/actions/workflows/ci.yml)

Projet d'automatisation de tests avec **Playwright** (Python), réalisé dans le cadre de ma formation en test logiciel / QA.

## 📖 Contexte et démarche

Ce projet a initialement démarré sur le site **Guru99 Bank**, une référence classique en formation QA. En cours de route, j'ai découvert que le site avait changé de fonctionnement : les identifiants ne sont plus fixes et publics, mais générés à la demande par email et valables seulement 20 jours — ce qui rendait le projet non reproductible pour qui voudrait cloner ce repo.

J'ai donc choisi de basculer sur **Sauce Demo**, un site reconnu dans l'industrie du test, avec des comptes utilisateurs fixes et stables, adaptés à un projet de démonstration durable.

## 🎯 Objectif

Mettre en pratique les compétences d'un testeur logiciel : conception de scénarios de test, automatisation, couverture des cas positifs et négatifs.

## 🛠️ Stack technique

- **Python 3.14**
- **Playwright** (pytest-playwright)
- **Selenium**
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
| `test_login_standard_user_selenium` | Vérifie la connexion valide avec Selenium (framework alternatif) |
| `test_login_locked_out_user_selenium` | Vérifie le cas d'erreur avec Selenium |

## 📋 Documentation du cycle de test

En complément de l'automatisation, ce projet documente une démarche de test manuel complète :

- **[User Stories](docs/user-stories/user-stories.md)** — Besoins fonctionnels et critères d'acceptation
- **[Cas de test — Connexion](docs/test-cases/test-cases-login.md)**
- **[Cas de test — Panier & Checkout](docs/test-cases/test-cases-checkout.md)**
- **[Bug Report #001](docs/bug-reports/bug-report-001.md)** — Anomalie détectée via test exploratoire

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
- [x] Mettre en place une CI/CD avec GitHub Actions
- [x] Ajouter des tests avec Selenium en complément de Playwright


## 👤 Auteure

**Yasmine** — En formation testeuse logicielle (QA), à la recherche d'un poste de testeuse junior.
Intérêt particulier pour l'automatisation de tests et les bonnes pratiques de qualité logicielle.


