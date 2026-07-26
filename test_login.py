from playwright.sync_api import Page, expect


def test_login_standard_user(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[data-test="username"]', "standard_user")
    page.fill('input[data-test="password"]', "secret_sauce")
    page.click('input[data-test="login-button"]')

    page.wait_for_load_state()
    print("URL après connexion :", page.url)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[data-test="username"]', "locked_out_user")
    page.fill('input[data-test="password"]', "secret_sauce")
    page.click('input[data-test="login-button"]')

    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    print("Message d'erreur affiché :", error_message.inner_text())
