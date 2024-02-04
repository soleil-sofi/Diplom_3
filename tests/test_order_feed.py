import allure
import pytest

from constants import urls
from constants import locators as loc
from pages.order_feed_page import OrderFeedPage


@allure.suite("Основной функционал (заказ)")
@pytest.mark.usefixtures('driver', 'auth')
class TestOrderFeed:

    @allure.title('Детали заказа')
    def test_order_details(self):
        order_feed = OrderFeedPage(self.driver)
        order_feed.follow_page(urls.EP_ORDER_FEED)
        order_feed.wait_clickable(10, loc.ORDER_FROM_FEED)
        order_feed.click_order()
        assert order_feed.driver.find_element(*loc.ORDER_POPUP)
