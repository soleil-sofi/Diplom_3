import allure
import pytest

from constants import urls
from constants import locators as loc
from pages.reset_password_page import ResetPasswordPage


@allure.suite("Восстановление пароля")
@pytest.mark.usefixtures('driver')
class TestResetPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_follow_reset_password(self):
        reset_page = ResetPasswordPage(self.driver)
        reset_page.follow_page(urls.EP_LOGIN)
        reset_page.wait_visibility(10, loc.RESET_PASSWORD_LINK)
        reset_page.follow_reset_password_link()
        reset_page.wait_visibility(10, loc.RESET_PASSWORD_BUTTON)
        assert reset_page.driver.current_url == urls.EP_FORGOT_PASSWORD

    @allure.title("Ввод почты для восстановления пароля")
    def test_email_check(self, create_new_user):
        reset_page = ResetPasswordPage(self.driver)
        reset_page.follow_page(urls.EP_FORGOT_PASSWORD)
        reset_page.set_email(create_new_user[0])
        assert reset_page.get_value(loc.EMAIL_FIELD_RESET_PAGE, 'value') == create_new_user[0]

    @allure.title("Кнопка 'Восстановить'")
    def test_reset_button(self, create_new_user):
        reset_page = ResetPasswordPage(self.driver)
        reset_page.follow_page(urls.EP_FORGOT_PASSWORD)
        reset_page.set_email(create_new_user[0])
        reset_page.click_reset_button()
        reset_page.wait_visibility(10, loc.EYE_BUTTON)
        assert reset_page.driver.current_url == urls.EP_RESET_PASSWORD

    @allure.title("Кнопка показать/скрыть в поле ввода пароля")
    def test_eye_button(self):
        reset_page = ResetPasswordPage(self.driver)
        reset_page.follow_page(urls.EP_FORGOT_PASSWORD)
        reset_page.click_reset_button()
        reset_page.wait_visibility(10, loc.EYE_BUTTON)
        reset_page.click_eye_button()
        assert 'input__placeholder-focused' in reset_page.get_value(loc.PASSWORD_FIELD, 'class')
