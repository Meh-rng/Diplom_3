from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderFeedPage(BasePage):
    # Счётчики
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    
    # Список заказов в разделе "В работе"
    ORDER_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li")

    @allure.step("Получить счётчик 'Выполнено за всё время'")
    def get_total_order_count(self):
        text = self.get_text(self.TOTAL_COUNTER)
        return int(text.replace(" ", "")) if text else 0

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_order_count(self):
        text = self.get_text(self.TODAY_COUNTER)
        return int(text.replace(" ", "")) if text else 0

    @allure.step("Получить список заказов в разделе «В работе»")
    def get_orders_in_progress(self):
        """Возвращает список номеров заказов в разделе «В работе» (только цифры)"""
        elements = self.driver.find_elements(*self.ORDER_IN_PROGRESS_LIST)
        # Фильтруем только те элементы, которые содержат цифры (номера заказов)
        orders = []
        for el in elements:
            text = el.text.strip()
            if text and text != "Все текущие заказы готовы!" and text.isdigit():
               orders.append(text)
        return orders