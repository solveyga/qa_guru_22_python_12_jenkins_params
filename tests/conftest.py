import pytest
# from selene.support.shared import browser
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attaches


# @pytest.fixture(scope="function", autouse=True)
# def open_browser():
#     browser.config.base_url = "https://demoqa.com"
#     driver_options = webdriver.ChromeOptions()
#     driver_options.page_load_strategy = "eager"
#     browser.config.driver_options = driver_options
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#     yield
#     browser.quit()


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    options.page_load_strategy = "eager"

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    attaches.add_logs(browser)
    attaches.add_html(browser)
    attaches.add_video(browser)

    browser.quit()