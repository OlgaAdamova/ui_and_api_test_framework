from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import selenium.webdriver.support.expected_conditions as ec

from core.elements.base_elements import BaseElements
from core.pages.base_page import BasePage


class EnterLoginPageElements(BaseElements):
    def user_name_input(self) -> WebElement:
        locator = By.CSS_SELECTOR, 'input[autocomplete="username"]'
        wait_method = ec.presence_of_element_located(locator)
        self.wait.until(method=wait_method)
        element = self.scope.find_element(*locator)
        return element

    def button_next(self) -> WebElement:
        locator = By.XPATH, "//span[text()='Next']"
        wait_method = ec.presence_of_element_located(locator)
        self.wait.until(method=wait_method)
        element = self.scope.find_element(*locator)
        return element


class EnterLoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(
            driver=driver,
            scope=driver,
            url="i/flow/login",
            unique_locator=(By.XPATH, '//span[text()="Sign in to X"]'),
            elements=EnterLoginPageElements,
        )
