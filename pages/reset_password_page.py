import allure
from constants import locators as loc
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Кликнуть на "Восстановить пароль"')
    def follow_reset_password_link(self):
        self.scroll_method(loc.RESET_PASSWORD_LINK)
        self.driver.find_element(*loc.RESET_PASSWORD_LINK).click()

    @allure.step('Заполнить поле "Email"')
    def set_email(self, email):
        self.driver.find_element(*loc.EMAIL_FIELD_RESET_PAGE).send_keys(email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_reset_button(self):
        self.driver.find_element(*loc.RESET_PASSWORD_BUTTON).click()

    @allure.step('Кликнуть на кнопку показать/скрыть пароль (глаз)')
    def click_eye_button(self):
        self.driver.find_element(*loc.EYE_BUTTON).click()

    def check_email(self, email):
        self.set_email(email)
        self.click_reset_button()
