import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers.user_data import generate_random_user


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
    driver.get("https://stellarburgers.education-services.ru")
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function")
def auth_browser(browser):
    """Фикстура с зарегистрированным и авторизованным браузером"""
    driver = browser
    
    # Генерируем нового пользователя
    user = generate_random_user()
    
    # 1. Переход на страницу регистрации
    driver.get("https://stellarburgers.education-services.ru/register")
    time.sleep(2)
    
    # Поле "Имя"
    name_input = driver.find_element(By.XPATH, "//input[@name='name']")
    name_input.send_keys(user["name"])
    
    # Поле "Email" (второе поле с type='text' на странице регистрации)
    email_input = driver.find_elements(By.XPATH, "//input[@type='text']")[1]  # второе поле
    email_input.send_keys(user["email"])
    
    # Поле "Пароль"
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(user["password"])
    
    # Кнопка "Зарегистрироваться"
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()
    
    time.sleep(3)
    
    # 2. После регистрации редирект на логин
    if "login" in driver.current_url:
        # Поле "Email"
        email_input = driver.find_element(By.XPATH, "//input[@type='text']")
        email_input.send_keys(user["email"])
        
        # Поле "Пароль"
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(user["password"])
        
        # Кнопка "Войти"
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
        time.sleep(3)
    
    # Возвращаемся на главную страницу
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(2)
    
    return driver