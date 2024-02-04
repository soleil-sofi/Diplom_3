import allure
from constants import locators as loc
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_personal_account(self):
        self.driver.find_element(*loc.ACCOUNT_BUTTON).click()

    @allure.step('Кликнуть на "История заказов"')
    def click_order_history(self):
        self.driver.find_element(*loc.ORDER_HISTORY).click()

    @allure.step('Кликнуть на "Выход"')
    def click_logout(self):
        self.driver.find_element(*loc.LOGOUT_BUTTON).click()

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.driver.find_element(*loc.CONSTRUCTOR_BUTTON).click()
