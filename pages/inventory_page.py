from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def add_product_to_cart(self, product_slug: str):
        self.page.click(f'button[data-test="add-to-cart-{product_slug}"]')

    def go_to_cart(self):
        self.cart_link.click()
