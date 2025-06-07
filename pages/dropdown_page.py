from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def select_by_text(self, text: str):
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        dropdown.select_by_visible_text(text)

    def get_selected_text(self) -> str:
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        return dropdown.first_selected_option.text