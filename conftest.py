import allure
import pytest
# import argparse
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage
import data_generators as gen
from constants import locators as loc
from constants import urls


# parser = argparse.ArgumentParser(description='driver: chrome/firefox')
# parser.add_argument('driver_name', type=str, help='host')
# args = parser.parse_args()


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    with allure.step('Открыть браузер'):
        opt = Options()
        opt.add_argument("--start-maximized")
        request.cls.driver = webdriver.Chrome(options=opt)
    yield
    with allure.step('Закрыть браузер'):
        request.cls.driver.quit()


@allure.title("Создать пользователя")
@pytest.fixture(scope="class")
def create_new_user():
    email = gen.generate_email()
    password = gen.generate_random_string()
    data = {
        "email": email,
        "password": password,
        "name": gen.generate_random_string(4)
    }
    response_json = requests.post(url=urls.EP_REGISTER, data=data).json()
    yield email, password
    requests.delete(url=urls.EP_USER, headers={"Authorization": response_json["accessToken"]})


@pytest.fixture(scope="class")
def auth(driver, request, create_new_user):
    request.cls.driver.get(urls.EP_LOGIN)
    page = BasePage(request.cls.driver)
    page.driver.find_element(*loc.EMAIL_AUTH_FIELD).send_keys(create_new_user[0])
    page.driver.find_element(*loc.PASSWORD_AUTH_FIELD).send_keys(create_new_user[1])
    page.driver.find_element(*loc.LOGIN_BUTTON).click()
    page.wait_visibility(10, loc.HEADER_MAIN_PAGE)
