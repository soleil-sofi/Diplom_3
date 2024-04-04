import time

import allure
from constants import constructor_locators as loc
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.driver.find_element(*loc.CONSTRUCTOR_BUTTON).click()

    @allure.step('Кликнуть на кнопку "Лента заказов"')
    def click_feed_button(self):
        self.driver.find_element(*loc.ORDER_FEED_BUTTON).click()

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.driver.find_element(*loc.INGREDIENT).click()

    @allure.step('Свернуть поп-ап ингредиента (кликнуть на крестик)')
    def minimize_ingredient_popup(self):
        self.driver.find_element(*loc.CLOSE_DETAILS_POPUP).click()

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self, locator):
        ingredient = self.driver.find_element(*locator)
        order_area = self.driver.find_element(*loc.ORDER_SECTION)
        self.replace_element(ingredient, order_area)

    @allure.step('Кликнуть "Оформить заказ"')
    def click_make_order_button(self):
        self.driver.find_element(*loc.MAKE_ORDER_BUTTON).click()

    @allure.step('Сделать заказ')
    def make_order(self, locator):
        self.add_ingredient_to_order(locator)
        self.click_make_order_button()
        self.wait_clickable(10, loc.MAKE_ORDER_BUTTON)

    @allure.step('Свернуть поп-ап заказа (кликнуть на крестик)')
    def minimize_order_popup(self):
        self.driver.find_element(*loc.CLOSE_ORDER_POPUP).click()

    def wait_order_number(self):
        """Ожидание номера заказа (т.к. сразу после создания появляется номер 9999)"""
        for _ in range(10):
            if self.get_text(loc.ORDER_NUMBER) == '9999':
                time.sleep(1)
            else:
                break
