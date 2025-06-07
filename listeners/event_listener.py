from selenium.webdriver.support.events import AbstractEventListener
from selenium.common.exceptions import StaleElementReferenceException

class MyListener(AbstractEventListener):
    def before_click(self, element, driver):
        try:
            tag = element.tag_name
        except StaleElementReferenceException:
            tag = "<?> (stale)"
        print(f"[EVENT LISTENER] Перед кликом по элементу: <{tag}>")

    def after_click(self, element, driver):
        try:
            tag = element.tag_name
        except StaleElementReferenceException:
            tag = "<?> (stale)"
        print(f"[EVENT LISTENER] После клика по элементу: <{tag}>")

    def on_exception(self, exception, driver):
        print(f"[EVENT LISTENER] Исключение: {exception}")
