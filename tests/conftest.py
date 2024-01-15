import pytest
from _pytest.config.argparsing import Parser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from core.helpers import helpers
from core.pages.enter_login_page import EnterLoginPage
from core.pages.enter_password_page import EnterPasswordPage
from core.pages.home_page import HomePage


def pytest_addoption(parser: Parser):
    parser.addoption("--env", required=True, help="Base URL")
    parser.addoption("--TWITTER_USER_NAME", required=True)
    parser.addoption("--TWITTER_PASSWORD", required=True)
    parser.addoption("--GMAIL_USER_NAME")
    parser.addoption("--GMAIL_PASSWORD")
    parser.addoption("--screen_width", required=True, type=int)
    parser.addoption("--screen_height", required=True, type=int)


@pytest.fixture(scope="session", autouse=True)
def expose_options(request: pytest.FixtureRequest):
    pytest.option = request.config.option
    pytest.option.PAGE_WAIT_TIMEOUT = 10
    pytest.option.ELEMENT_WAIT_TIMEOUT = 5


@pytest.fixture
def driver(request: pytest.FixtureRequest) -> webdriver.Chrome:
    driver: webdriver.Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(width=request.config.option.screen_width, height=request.config.option.screen_height)
    return driver


@pytest.fixture
def home_page(request: pytest.FixtureRequest, driver: webdriver.Chrome) -> webdriver.Chrome:
    home = HomePage(driver=driver)
    driver.get(home.url)

    user_name = request.config.option.TWITTER_USER_NAME
    password = request.config.option.TWITTER_PASSWORD

    pickle_path = helpers.get_path_in_repo("temp", "cookies_by_user.pkl")
    helpers.try_load_cookies(driver=driver, pickle_path=pickle_path, user_name=user_name)

    if not home.is_open():
        enter_login_page = EnterLoginPage(driver=driver)
        driver.get(enter_login_page.url)
        enter_login_page.elements.user_name_input().send_keys(user_name)
        enter_login_page.elements.button_next().click()

        enter_password_page = EnterPasswordPage(driver=driver)
        enter_password_page.elements.password_input().send_keys(password)
        enter_password_page.elements.button_log_in().click()

        assert home.is_open()

    helpers.dump_cookies(driver=driver, pickle_path=pickle_path, user_name=user_name)

    return driver
