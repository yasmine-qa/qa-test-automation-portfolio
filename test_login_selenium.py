import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_standard_user_selenium(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]').click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_locked_out_user_selenium(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]').send_keys("locked_out_user")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]').click()

    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert error_message.is_displayed()
