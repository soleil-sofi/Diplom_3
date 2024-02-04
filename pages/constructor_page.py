import allure
from constants import locators as loc
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

    @allure.step('Сделать заказ')
    def make_order(self, locator):
        self.add_ingredient_to_order(locator)
        self.driver.find_element(*loc.MAKE_ORDER_BUTTON).click()
        self.wait_clickable(10, loc.MAKE_ORDER_BUTTON)
