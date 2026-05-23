from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
        # Прокрутка к элементу
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
        # Клик через JavaScript, чтобы избежать перехвата
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        with allure.step(f"Получить текст из: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        