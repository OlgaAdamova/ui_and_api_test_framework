import abc

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from core.html_holder import HtmlHolder
from core.components.base_component import BaseComponent
from core.pages.base_page import BasePage


class BaseElements(HtmlHolder, abc.ABC):
    def __init__(self, owner: BasePage | BaseComponent):
        self.owner: BasePage | BaseComponent = owner
        self.driver: WebDriver = owner.driver
        self.scope: WebDriver | WebElement = owner.scope
        super().__init__(
             driver=owner.driver,
             scope=owner.scope,
        )
