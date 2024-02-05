import allure
from constants import user_locators as loc
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_personal_account(self):
        self.driver.find_element(*loc.ACCOUNT_BUTTON).click()

    @allure.step('Кликнуть на вкладку "История заказов"')
    def click_order_history(self):
        self.driver.find_element(*loc.ORDER_HISTORY).click()

    @allure.step('Кликнуть на кнопку "Выход"')
    def click_logout(self):
        self.driver.find_element(*loc.LOGOUT_BUTTON).click()
