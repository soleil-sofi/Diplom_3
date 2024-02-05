import allure
from constants import feed_locators as loc
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть на заказ')
    def click_order(self):
        self.driver.find_element(*loc.ORDER_FROM_FEED).click()

    @allure.step('Свернуть поп-ап заказа (кликнуть на крестик)')
    def minimize_order_popup(self):
        self.driver.find_element(*loc.CLOSE_ORDER_POPUP).click()
