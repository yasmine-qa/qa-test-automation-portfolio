from playwright.sync_api import expect


def test_login_locked_out_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_message).to_be_visible()
