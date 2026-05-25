from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ModalPage(BasePage):
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    @allure.step("Закрыть модальное окно с номером заказа")
    def close_order_modal(self):
        try:
            overlay = self.find_element(self.MODAL_OVERLAY)
            self.driver.execute_script("arguments[0].click();", overlay)
        except:
            pass