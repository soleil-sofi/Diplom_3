import allure
from constants import locators as loc
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Кликнуть на "Восстановить пароль"')
    def follow_reset_password_link(self):
        self.scroll_method(loc.RESET_PASSWORD_LINK)
        self.driver.find_element(*loc.RESET_PASSWORD_LINK).click()
