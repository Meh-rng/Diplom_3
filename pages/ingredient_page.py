from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class IngredientPage(BasePage):
    
    INGREDIENT_NAME = (By.XPATH, "//h2[contains(@class, 'text_type_main-large')]")
    
    @allure.step("Проверить, что открыта страница ингредиента")
    def is_on_ingredient_page(self):
        return self.url_contains("ingredient")
    
    @allure.step("Получить название ингредиента на странице")
    def get_ingredient_name(self):
        return self.get_text(self.INGREDIENT_NAME)