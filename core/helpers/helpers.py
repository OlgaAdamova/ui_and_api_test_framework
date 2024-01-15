import os.path
import pickle

from selenium.webdriver.chrome.webdriver import WebDriver

from root import ROOT_PATH


def get_path_in_repo(*rel_path_parts: str) -> str:
    return os.path.join(ROOT_PATH, *rel_path_parts)


def dump_cookies(driver: WebDriver, pickle_path: str, user_name: str):
    cookies_by_user = {user_name: driver.get_cookies()}

    with open(pickle_path, "wb") as file:
        pickle.dump(cookies_by_user, file)


def try_load_cookies(driver: WebDriver, pickle_path: str, user_name: str):
    if os.path.exists(pickle_path):
        with open(pickle_path, "rb") as file:
            cookies_by_user = pickle.load(file)

        cookies = cookies_by_user.get(user_name, [])

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()
