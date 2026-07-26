from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def start_checkout(self):
        self.checkout_button.click()


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator('input[data-test="firstName"]')
        self.last_name_input = page.locator('input[data-test="lastName"]')
        self.postal_code_input = page.locator('input[data-test="postalCode"]')
        self.continue_button = page.locator('input[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.confirmation_header = page.locator('[data-test="complete-header"]')

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()
        