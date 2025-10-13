import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attaches
from dotenv import load_dotenv
import os

# import tempfile
# import shutil


@pytest.fixture(scope="session", autouse=True)
def load_env():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    dotenv_path = os.path.join(base_dir, '.env')
    load_dotenv(dotenv_path=dotenv_path)
    # print(f"SELENOID_LOGIN={os.getenv('SELENOID_LOGIN')}")
    # print(f"SELENOID_PASS={os.getenv('SELENOID_PASS')}")
    # print(f"SELENOID_URL={os.getenv('SELENOID_URL')}")


@pytest.fixture(scope="function")
def setup_browser(request):
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.page_load_strategy = "eager"
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")

    # temp_dir = tempfile.mkdtemp()
    # options.add_argument(f'--user-data-dir={temp_dir}')

    selenoid_capabilities = {
        "browserName": "chrome",
        # "browserVersion": "100.0",
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
    # shutil.rmtree(temp_dir)
