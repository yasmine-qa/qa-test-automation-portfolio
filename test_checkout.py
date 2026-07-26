from playwright.sync_api import Page, expect


def login(page: Page):
    """Fonction utilitaire pour se connecter avant chaque test de panier/checkout."""
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', "standard_user")
    page.fill('input[data-test="password"]', "secret_sauce")
    page.click('input[data-test="login-button"]')
    page.wait_for_load_state()


def test_add_product_to_cart(page: Page):
    login(page)

    # Ajoute le premier produit (sac à dos) au panier
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')

    # Vérifie que le badge du panier affiche bien 1 article
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    expect(cart_badge).to_have_text("1")


def test_checkout_full_flow(page: Page):
    login(page)

    # Ajoute un produit et va au panier
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="shopping-cart-link"]')

    # Vérifie qu'on est bien sur la page du panier avec le bon produit
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text("Sauce Labs Backpack")

    # Lance le checkout
    page.click('[data-test="checkout"]')

    # Remplit les informations de livraison
    page.fill('input[data-test="firstName"]', "Yasmine")
    page.fill('input[data-test="lastName"]', "Test")
    page.fill('input[data-test="postalCode"]', "13000")
    page.click('input[data-test="continue"]')

    # Vérifie le résumé de commande, puis termine
    expect(page.locator('[data-test="finish"]')).to_be_visible()
    page.click('[data-test="finish"]')

    # Vérifie le message de confirmation final
    confirmation = page.locator('[data-test="complete-header"]')
    expect(confirmation).to_have_text("Thank you for your order!")
    