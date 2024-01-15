import abc
from typing import Tuple, Optional
from urllib.parse import urljoin

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core.html_holder import HtmlHolder


class BasePage(HtmlHolder, abc.ABC):
    def __init__(
             self,
             driver: WebDriver,
             scope: WebDriver,
             url: Optional[str],
             unique_locator: Tuple[str, str],
             elements,
    ):
        super().__init__(
             driver=driver,
             scope=scope,
        )
        self.url: Optional[str] = url and urljoin(pytest.option.env, url)
        self.unique_locator: Tuple[str, str] = unique_locator
        self.elements = elements(owner=self)

    def is_open(self, timeout: Optional[int] = None) -> bool:
        timeout = timeout or pytest.option.PAGE_WAIT_TIMEOUT

        try:
            WebDriverWait(self.scope, timeout).until(ec.visibility_of_element_located(self.unique_locator))
        except TimeoutException:
            return False
        else:
            return True
