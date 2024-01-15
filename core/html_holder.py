import abc
from typing import Tuple, Callable

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


class HtmlHolder(abc.ABC):
    def __init__(
            self,
            driver: WebDriver,
            scope: WebDriver | WebElement,
    ):
        self.driver: WebDriver = driver
        self.scope: WebDriver | WebElement = scope
        self.wait: WebDriverWait = WebDriverWait(
            driver=scope,
            timeout=pytest.option.ELEMENT_WAIT_TIMEOUT,
            ignored_exceptions=[StaleElementReferenceException],
        )

    def get_element(
            self,
            locator: Tuple[By, str],
            wait_method: Callable = ec.presence_of_element_located,
    ):
        method = wait_method(*locator)
        self.wait.until(method=method)
        element = self.scope.find_element(*locator)
        return element
