import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from selenium.webdriver.support import expected_conditions as EC


class ModalPage(BasePage):
    # Модальное окно с номером заказа
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    
    # Правильный локатор кнопки закрытия (из твоего скриншота)
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal_close_modified')]")
    
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    @allure.step("Закрыть модальное окно с номером заказа")
    def close_order_modal(self):
        """Закрывает модальное окно кликом по крестику"""
        time.sleep(2)
        
        # Поиск всех кнопок в модальном окне для отладки
        try:
            modal = self.driver.find_element(*self.ORDER_MODAL)
            buttons = modal.find_elements(By.TAG_NAME, "button")
            print(f"Найдено кнопок в модалке: {len(buttons)}")
            for btn in buttons:
                print(f"  Класс кнопки: {btn.get_attribute('class')}")
        except:
            pass
        
        # Клик по крестику через JavaScript с правильным локатором
        try:
            close_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Modal_modal_close_modified')]")
            self.driver.execute_script("arguments[0].click();", close_button)
            time.sleep(1)
            print("✅ Модальное окно закрыто")
            return
        except Exception as e:
            print(f"Ошибка закрытия: {e}")
        
        # Альтернатива: клик по оверлею
        try:
            overlay = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
            self.driver.execute_script("arguments[0].click();", overlay)
            time.sleep(1)
            print("✅ Модальное окно закрыто через оверлей")
        except Exception as e:
            print(f"Не удалось закрыть модалку: {e}")
    
    @allure.step("Ожидание появления номера заказа")
    def wait_for_order_number(self):
        """Ожидает появления модального окна с номером заказа"""
        time.sleep(2)
        return self.is_element_visible(self.ORDER_MODAL)