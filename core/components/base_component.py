import abc

from selenium.webdriver.remote.webelement import WebElement

from core.html_holder import HtmlHolder
from core.pages.base_page import BasePage


class BaseComponent(HtmlHolder, abc.ABC):
    def __init__(
            self,
            owner: BasePage,
            container: WebElement,
            elements,
    ):
        self.owner: BasePage = owner
        self.container: WebElement = container
        self.elements = elements
        super().__init__(
             driver=owner.driver,
             scope=container,
             wait_timeout=owner.wait._timeout,  # noqa
        )
