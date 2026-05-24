import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers.urls import Urls
from helpers.user_data import generate_random_user
from pages.auth_page import AuthPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    
    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function")
def auth_browser(browser):
    """Фикстура с зарегистрированным и авторизованным браузером"""
    driver = browser
    auth_page = AuthPage(driver)
    
    user = generate_random_user()
    
    auth_page.register_user(user)
    
    auth_page.login_after_registration(user)
    
    driver.get(Urls.BASE_URL)
    
    return driver