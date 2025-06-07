from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HoversPage:
    URL = "https://the-internet.herokuapp.com/hovers"
    FIGURES = (By.CLASS_NAME, "figure")
    CAPTION = (By.CLASS_NAME, "figcaption")

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def open(self):
        self.driver.get(self.URL)

    def hover_over_figure(self, index: int = 0):
        figures = self.driver.find_elements(*self.FIGURES)
        if index >= len(figures):
            raise IndexError(f"Доступно {len(figures)} элементов, индекс {index} вне диапазона")
        self.action.move_to_element(figures[index]).perform()

    def get_caption_text(self, index: int = 0) -> str:
        captions = self.driver.find_elements(*self.CAPTION)
        if index >= len(captions):
            raise IndexError(f"Доступно {len(captions)} подписей, индекс {index} вне диапазона")
        return captions[index].text.strip()