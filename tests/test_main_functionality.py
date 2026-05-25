import allure
from pages.main_page import MainPage
from pages.ingredient_page import IngredientPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, browser):
        main_page = MainPage(browser)
        
        main_page.click_order_feed()
        main_page.click_constructor()
        
        assert main_page.url_not_contains("feed")

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed_changes_url(self, browser):
        main_page = MainPage(browser)
        
        main_page.click_order_feed()
        
        assert main_page.url_contains("feed")

    @allure.title("Клик на ингредиент открывает страницу с деталями")
    def test_click_ingredient_opens_detail_page(self, browser):
        main_page = MainPage(browser)
        ingredient_page = IngredientPage(browser)
        
        main_page.click_first_ingredient()
        
        assert ingredient_page.is_on_ingredient_page()

    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_ingredient_counter_increases_after_drag(self, browser):
        main_page = MainPage(browser)
        
        initial_counter = main_page.get_first_ingredient_counter()
        
        main_page.drag_ingredient_to_basket()
        
        new_counter = main_page.get_first_ingredient_counter()
        
        assert new_counter > initial_counter, (
            f"Счётчик должен увеличиться. Было: {initial_counter}, стало: {new_counter}"
        )