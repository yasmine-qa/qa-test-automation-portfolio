import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    """Instancie LoginPage et se rend sur la page de connexion."""
    lp = LoginPage(page)
    lp.goto()
    return lp


@pytest.fixture
def logged_in_page(login_page):
    """Fixture prête à l'emploi : déjà connectée en standard_user."""
    login_page.login("standard_user", "secret_sauce")
    return login_page.page
