from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControlsPage:
    URL = "https://the-internet.herokuapp.com/dynamic_controls"
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def is_checkbox_present(self) -> bool:
        return len(self.driver.find_elements(*self.CHECKBOX)) > 0

    def click_remove(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()
        self.wait.until(EC.invisibility_of_element_located(self.CHECKBOX))

    def click_add(self):
        self.driver.find_element(*self.ADD_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(self.CHECKBOX))

    def get_message(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(self.MESSAGE))
        return el.text.strip()
