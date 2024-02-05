import allure
import pytest

from constants import urls
from constants import user_locators as loc
from pages.personal_account_page import AccountPage


@allure.suite("Личный кабинет")
@pytest.mark.usefixtures('driver', 'auth')
class TestAccountPage:

    @allure.title("Переход в Личный кабинет")
    def test_follow_account(self):
        profile = AccountPage(self.driver)
        profile.follow_page(urls.MAIN_URL)
        profile.click_personal_account()
        profile.wait_visibility(10, loc.LOGOUT_BUTTON)
        assert profile.driver.current_url == urls.EP_PROFILE, 'переход в личный кабинет не произошел'

    @allure.title("Переход к Истории заказов")
    def test_history(self):
        profile = AccountPage(self.driver)
        profile.follow_page(urls.MAIN_URL)
        profile.click_personal_account()
        profile.wait_visibility(10, loc.LOGOUT_BUTTON)
        profile.click_order_history()
        assert profile.driver.current_url == urls.EP_ORDER_STORY, 'переход к вкладке История заказов не произошел'

    @allure.title("Выход из аккаунта")
    def test_logout(self):
        profile = AccountPage(self.driver)
        profile.follow_page(urls.MAIN_URL)
        profile.click_personal_account()
        profile.wait_visibility(10, loc.LOGOUT_BUTTON)
        profile.click_logout()
        profile.wait_visibility(10, loc.LOGIN_BUTTON)
        assert profile.driver.current_url == urls.EP_LOGIN, 'переход на страницу авторизации не произошел'
