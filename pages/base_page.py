from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.visibility_of(element))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы по локатору: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить, что URL содержит {text}")
    def url_contains(self, text):
        return text in self.driver.current_url

    @allure.step("Вернуться на предыдущую страницу")
    def go_back(self):
        self.driver.back()

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Проверить, что URL не содержит {text}")
    def url_not_contains(self, text):
        return text not in self.driver.current_url