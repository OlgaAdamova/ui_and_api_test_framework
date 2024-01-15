from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core.elements.base_elements import BaseElements
from core.pages.base_page import BasePage


class HomePageElements(BaseElements):
    ...


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(
            driver=driver,
            scope=driver,
            url="home",
            unique_locator=(By.CSS_SELECTOR, 'div[aria-label="Timeline: Your Home Timeline"]'),
            elements=HomePageElements,
        )
