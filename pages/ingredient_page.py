from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By

class IngredientPage(BasePage):
    
    @allure.step("Проверить, что открыта страница ингредиента")
    def is_on_ingredient_page(self):
        return "ingredient" in self.driver.current_url
    
    @allure.step("Получить название ингредиента на странице")
    def get_ingredient_name(self):
        # Найди правильный локатор для названия на странице ингредиента
        name_locator = (By.XPATH, "//h2[contains(@class, 'text_type_main-large')]")
        return self.get_text(name_locator)