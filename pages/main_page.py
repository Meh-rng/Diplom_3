from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    
    FIRST_INGREDIENT_COUNTER = (
        By.XPATH, 
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]//div[contains(@class, 'counter_counter')]//p[contains(@class, 'counter_counter_num')]"
    )
    
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and text()='Оформить заказ']")

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click_element(self.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        self.click_element(self.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click_element(self.FIRST_INGREDIENT)
        time.sleep(1)

    @allure.step("Добавить ингредиент перетаскиванием")
    def drag_ingredient_to_basket(self):
        ingredient = self.wait.until(EC.presence_of_element_located(self.FIRST_INGREDIENT))
        basket = self.wait.until(EC.presence_of_element_located(self.BASKET))
        actions = ActionChains(self.driver)
        time.sleep(1)
        actions.drag_and_drop(ingredient, basket).perform()
        time.sleep(1)

    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        counters = self.driver.find_elements(By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]//div[contains(@class, 'counter_counter')]//p")
        if counters:
            text = counters[0].text
            return int(text) if text.isdigit() else 0
        return 0

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click_element(self.PLACE_ORDER_BUTTON)