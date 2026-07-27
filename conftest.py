from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_and_checkout_page import CartPage, CheckoutPage


def test_add_product_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    expect(inventory_page.cart_badge).to_have_text("1")


def test_checkout_full_flow(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.start_checkout()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_information("Yasmine", "QA", "13000")
    checkout_page.finish_order()

    expect(checkout_page.confirmation_header).to_have_text("Thank you for your order!")
    