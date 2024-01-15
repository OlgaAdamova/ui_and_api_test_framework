from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec


from core.elements.base_elements import BaseElements
from core.pages.base_page import BasePage


class EnterPasswordPageElements(BaseElements):
    def password_input(self) -> WebElement:
        locator = By.CSS_SELECTOR, 'input[name="password"]'
        wait_method = ec.presence_of_element_located(locator)
        self.wait.until(method=wait_method)
        element = self.scope.find_element(*locator)
        return element

    def button_log_in(self) -> WebElement:
        locator = By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]'
        wait_method = ec.presence_of_element_located(locator)
        self.wait.until(method=wait_method)
        element = self.scope.find_element(*locator)
        return element


class EnterPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(
            driver=driver,
            scope=driver,
            url=None,
            unique_locator=(By.XPATH, '//span[text()="Enter your password"]'),
            elements=EnterPasswordPageElements,
        )
