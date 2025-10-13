import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attaches
import logging
from dotenv import load_dotenv
import os


@pytest.fixture(scope="session", autouse=True)
def load_env():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    dotenv_path = os.path.join(base_dir, '.env')
    load_dotenv(dotenv_path=dotenv_path)

    logging.basicConfig(level=logging.INFO)
    logging.info(f"SELENOID_LOGIN={os.getenv('SELENOID_LOGIN')}")
    logging.info(f"SELENOID_PASS={os.getenv('SELENOID_PASS')}")
    logging.info(f"SELENOID_URL={os.getenv('SELENOID_URL')}")


selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")


@pytest.fixture(scope="function")
def setup_browser(request):
    options = Options()
    options.page_load_strategy = "eager"

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
    )

    browser = Browser(Config(driver))
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    attaches.add_logs(browser)
    attaches.add_html(browser)
    attaches.add_screenshot(browser)
    attaches.add_video(browser)

    browser.quit()
