import time
import allure
import pytest

from constants import urls
from constants import locators as loc
from pages.constructor_page import ConstructorPage


@allure.suite("Основной функционал (заказ)")
@pytest.mark.usefixtures('driver', 'auth')
class TestConstructorPage:

    @allure.title("Переход к Конструктору")
    def test_follow_constructor(self):
        order_page = ConstructorPage(self.driver)
        order_page.follow_page(urls.EP_ORDER_FEED)
        order_page.click_constructor()
        order_page.wait_visibility(10, loc.ORDER_SECTION)
        assert order_page.driver.current_url == f'{urls.MAIN_URL}/'

    @allure.title("Переход к Ленте заказов")
    def test_follow_feed(self):
        order_page = ConstructorPage(self.driver)
        order_page.follow_page(urls.MAIN_URL)
        order_page.click_feed_button()
        order_page.wait_visibility(10, loc.DONE_SUM)
        assert order_page.driver.current_url == urls.EP_ORDER_FEED

    @allure.title("Переход к поп-апу ингредиента")
    def test_follow_ingredient_popup(self):
        order_page = ConstructorPage(self.driver)
        order_page.follow_page(urls.MAIN_URL)
        order_page.wait_clickable(10, loc.INGREDIENT)
        order_page.click_ingredient()
        order_page.wait_visibility(10, loc.HEADER_INGREDIENT_POPUP)
        assert order_page.get_text(loc.INGREDIENT_NAME) == order_page.get_text(loc.INGREDIENT_NAME_IN_POPUP)

    @allure.title("Скрытие поп-апа ингредиента")
    def test_follow_ingredient_popup(self):
        order_page = ConstructorPage(self.driver)
        order_page.follow_page(urls.MAIN_URL)
        order_page.wait_clickable(10, loc.INGREDIENT)
        order_page.click_ingredient()
        order_page.wait_visibility(10, loc.HEADER_INGREDIENT_POPUP)
        order_page.minimize_ingredient_popup()
        assert 'Modal_modal_opened__3ISw4' not in order_page.get_value(loc.POP_UP_SECTION, "class")

    @allure.title("Cчетчик ингредиента")
    def test_ingredient_counter(self):
        order_page = ConstructorPage(self.driver)
        order_page.follow_page(urls.MAIN_URL)
        order_page.wait_clickable(10, loc.INGREDIENT)
        before_adding = int(order_page.get_text(loc.INGREDIENT_COUNTER))
        order_page.add_ingredient_to_order(loc.INGREDIENT)
        time.sleep(1)
        after_adding = int(order_page.get_text(loc.INGREDIENT_COUNTER))
        assert before_adding < after_adding

    @allure.title("Создание заказа авторизованным пользователем")
    def test_make_order_by_user(self, auth):
        order_page = ConstructorPage(self.driver)
        order_page.follow_page(urls.MAIN_URL)
        order_page.wait_clickable(10, loc.INGREDIENT)
        order_page.make_order(loc.INGREDIENT)
        order_page.wait_visibility(10, loc.CONFIRMATION_POPUP)
        assert 'Modal_modal_opened__3ISw4' in order_page.get_value(loc.POP_UP_SECTION, "class")
