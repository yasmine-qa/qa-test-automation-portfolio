from playwright.sync_api import expect


def test_login_standard_user(login_page):
    """Test smoke : vérifie que le parcours de connexion de base fonctionne."""
    login_page.login("standard_user", "secret_sauce")
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    