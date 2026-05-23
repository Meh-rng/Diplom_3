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
        
        browser_name = self.driver.capabilities['browserName'].lower()
        
        if browser_name == "firefox":
            # Эмуляция через JavaScript для Firefox
            self.driver.execute_script("""
                var ingredient = arguments[0];
                var basket = arguments[1];
                
                function emitEvent(element, eventType, clientX, clientY) {
                    var event = new MouseEvent(eventType, {
                        view: window,
                        bubbles: true,
                        cancelable: true,
                        clientX: clientX,
                        clientY: clientY
                    });
                    element.dispatchEvent(event);
                }
                
                var rectIng = ingredient.getBoundingClientRect();
                var rectBas = basket.getBoundingClientRect();
                
                var startX = rectIng.left + rectIng.width / 2;
                var startY = rectIng.top + rectIng.height / 2;
                var endX = rectBas.left + rectBas.width / 2;
                var endY = rectBas.top + rectBas.height / 2;
                
                emitEvent(ingredient, 'mousedown', startX, startY);
                emitEvent(ingredient, 'dragstart', startX, startY);
                emitEvent(document.elementFromPoint(endX, endY), 'dragenter', endX, endY);
                emitEvent(document.elementFromPoint(endX, endY), 'dragover', endX, endY);
                emitEvent(basket, 'drop', endX, endY);
                emitEvent(ingredient, 'dragend', endX, endY);
                emitEvent(basket, 'mouseup', endX, endY);
            """, ingredient, basket)
            time.sleep(2)
        else:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(ingredient, basket).perform()
            time.sleep(1)

    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        if self.is_element_visible(self.FIRST_INGREDIENT_COUNTER):
            text = self.get_text(self.FIRST_INGREDIENT_COUNTER)
            return int(text) if text.isdigit() else 0
        return 0

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click_element(self.PLACE_ORDER_BUTTON)