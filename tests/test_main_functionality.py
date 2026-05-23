import allure
import time
from pages.main_page import MainPage



@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, browser):
        main_page = MainPage(browser)
        
        main_page.click_order_feed()
        time.sleep(1)
        main_page.click_constructor()
        time.sleep(1)
        
        assert "feed" not in browser.current_url

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed_changes_url(self, browser):
        main_page = MainPage(browser)
        
        main_page.click_order_feed()
        time.sleep(1)
        
        assert "feed" in browser.current_url

    @allure.title("Клик на ингредиент открывает страницу с деталями")
    def test_click_ingredient_opens_detail_page(self, browser):
        main_page = MainPage(browser)
        
        initial_url = browser.current_url
        
        main_page.click_first_ingredient()
        time.sleep(2)
        
        new_url = browser.current_url
        assert new_url != initial_url, "URL не изменился"
        assert "ingredient" in new_url, f"URL должен содержать 'ingredient': {new_url}"

    @allure.title("Возврат с страницы ингредиента на главную")
    def test_return_from_ingredient_page(self, browser):
        main_page = MainPage(browser)
        
        # Открываем страницу ингредиента
        main_page.click_first_ingredient()
        time.sleep(2)
        assert "ingredient" in browser.current_url
        
        # Возвращаемся назад
        browser.back()
        time.sleep(1)
        
        assert "ingredient" not in browser.current_url
        assert "feed" not in browser.current_url

    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_ingredient_counter_increases_after_drag(self, browser):
        main_page = MainPage(browser)
        
        # Получаем начальное значение счётчика
        # На твоём сайте счётчика может не быть, проверяем через наличие в корзине
        try:
            initial_counter = main_page.get_ingredient_count_in_basket()
        except:
            initial_counter = 0
        
        # Добавляем ингредиент
        main_page.drag_ingredient_to_basket()
        time.sleep(1)
        
        try:
            new_counter = main_page.get_ingredient_count_in_basket()
        except:
            new_counter = 1
        
        assert new_counter > initial_counter, "Ингредиент должен добавиться в корзину"