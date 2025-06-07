from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        username_field = self.driver.find_element(*self.USERNAME_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_flash_message(self) -> str:
        return self.driver.find_element(*self.FLASH_MESSAGE).text.strip()