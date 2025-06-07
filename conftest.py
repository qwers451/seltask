import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.events import EventFiringWebDriver

from listeners.event_listener import MyListener

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-dev-tools')
    options.add_argument('--no-sandbox')

    service = Service()

    raw_driver = webdriver.Chrome(service=service, options=options)

    driver = EventFiringWebDriver(raw_driver, MyListener())

    yield driver
    driver.quit()
