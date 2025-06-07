import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

class TestLogin:
    @pytest.mark.parametrize("username,password,expected_substring", [
        ("wrongUser", "wrongPass", "Your username is invalid!"),
    ])
    def test_invalid_login_shows_error(self, driver, username, password, expected_substring):
        page = LoginPage(driver)
        page.open()
        page.login(username, password)

        wait = WebDriverWait(driver, 5)
        flash_el = wait.until(EC.visibility_of_element_located(LoginPage.FLASH_MESSAGE))
        flash_text = flash_el.text.strip()

        assert expected_substring in flash_text

    def test_valid_login_success(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")

        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("/secure"))

        h2_el = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
        header_text = h2_el.text.strip()
        assert "Secure Area" == header_text

        logout_button = driver.find_element(By.XPATH, "//a[@href='/logout']")
        assert logout_button is not None
