import allure
import pytest

from constants import urls
from constants import feed_locators as f_loc, constructor_locators as c_loc
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage


@allure.suite("Лента заказов)")
@pytest.mark.usefixtures('driver', 'auth')
class TestOrderFeed:

    @allure.title('Детали заказа')
    def test_order_details(self):
        order_feed = OrderFeedPage(self.driver)
        order_feed.follow_page(urls.EP_ORDER_FEED)
        order_feed.wait_clickable(10, f_loc.ORDER_FROM_FEED)
        order_feed.click_order()
        assert order_feed.driver.find_element(*f_loc.ORDER_POPUP), 'поп-ап с деталями заказа не открылся'

    @allure.title('Заказ пользователя в Ленте заказов')
    def test_user_order_in_feed(self):
        page = ConstructorPage(self.driver)
        page.follow_page(urls.MAIN_URL)
        page.wait_clickable(10, c_loc.INGREDIENT)
        page.make_order(c_loc.INGREDIENT)
        page.wait_visibility(10, c_loc.CONFIRMATION_POPUP)
        page.wait_order_number()
        order_number = '#0' + page.get_text(c_loc.ORDER_NUMBER)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_visibility(10, f_loc.DONE_ALL)
        assert page.driver.find_element(*(f_loc.order_number_in_feed(order_number))), \
            'созданного заказа нет в ленте'

    @allure.title('Cчетчик {counter_type}')
    @pytest.mark.parametrize("counter_type, locator", [("Выполнено за всё время", f_loc.DONE_ALL),
                                                       ("Выполнено за сегодня", f_loc.DONE_TODAY)],
                             ids=["during all time", "during today"])
    def test_counter_done_all(self, counter_type, locator):
        page = ConstructorPage(self.driver)
        page.follow_page(urls.EP_ORDER_FEED)
        page.wait_clickable(10, locator)
        count_before_new_order = page.get_text(locator)
        page.click_constructor()
        page.wait_clickable(10, c_loc.INGREDIENT)
        page.make_order(c_loc.INGREDIENT)
        page.wait_order_number()
        page.wait_visibility(10, c_loc.CONFIRMATION_POPUP)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_visibility(10, locator)
        assert page.get_text(locator) > count_before_new_order, f'счетчик {counter_type} не увеличился'

    @allure.title('Заказ в разделе "В работе"')
    def test_order_in_process_list(self):
        page = ConstructorPage(self.driver)
        page.follow_page(urls.MAIN_URL)
        page.wait_clickable(10, c_loc.INGREDIENT)
        page.make_order(c_loc.INGREDIENT)
        page.wait_order_number()
        order_number = page.get_text(c_loc.ORDER_NUMBER)
        page.wait_visibility(10, c_loc.CONFIRMATION_POPUP)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_visibility(10, f_loc.DONE_ALL)
        assert page.get_text(f_loc.LAST_FROM_IN_PROCESS)[1:] == order_number, 'заказ не появился в разделе "В работе"'
