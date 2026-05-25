import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.modal_page import ModalPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_order_counter_increases_after_order(self, auth_browser):
        driver = auth_browser
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        modal_page = ModalPage(driver)
        
        main_page.click_order_feed()
        initial_total = order_feed_page.get_total_order_count()
        
        main_page.click_constructor()
        main_page.drag_ingredient_to_basket()
        main_page.place_order()
        
        modal_page.close_order_modal()
        
        main_page.click_order_feed()
        new_total = order_feed_page.get_total_order_count()
        
        assert new_total > initial_total, f"Было: {initial_total}, стало: {new_total}"

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_order_counter_increases_after_order(self, auth_browser):
        driver = auth_browser
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        modal_page = ModalPage(driver)
        
        main_page.click_order_feed()
        initial_today = order_feed_page.get_today_order_count()
        
        main_page.click_constructor()
        main_page.drag_ingredient_to_basket()
        main_page.place_order()
        
        modal_page.close_order_modal()
        
        main_page.click_order_feed()
        new_today = order_feed_page.get_today_order_count()
        
        assert new_today > initial_today, f"Было: {initial_today}, стало: {new_today}"

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_appears_in_progress_section(self, auth_browser):
        driver = auth_browser
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        modal_page = ModalPage(driver)
        
        main_page.click_order_feed()
        before_orders = order_feed_page.get_orders_in_progress()
        
        main_page.click_constructor()
        main_page.drag_ingredient_to_basket()
        main_page.place_order()
        
        modal_page.close_order_modal()
        
        main_page.click_order_feed()
        after_orders = order_feed_page.get_orders_in_progress()
        
        assert len(after_orders) > len(before_orders), "Новый заказ не появился в разделе «В работе»"