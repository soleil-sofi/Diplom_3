import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage
import data_generators as gen
from constants import user_locators as loc
from constants import urls


def pytest_addoption(parser):
    parser.addoption('--driver_name', type=str, default='chrome', help='choose one of drivers: chrome or firefox')


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    driver_name = request.config.getoption('--driver_name')
    with allure.step('Открыть браузер'):
        if driver_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--width=1300')
            options.add_argument('--height=800')
            request.cls.driver = webdriver.Firefox(options=options)
        else:
            options = Options()
            options.add_argument("--start-maximized")
            request.cls.driver = webdriver.Chrome(options=options)
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
    page.wait_clickable(10, loc.EMAIL_AUTH_FIELD)
    page.driver.find_element(*loc.EMAIL_AUTH_FIELD).send_keys(create_new_user[0])
    page.wait_clickable(10, loc.PASSWORD_AUTH_FIELD)
    page.driver.find_element(*loc.PASSWORD_AUTH_FIELD).send_keys(create_new_user[1])
    page.wait_clickable(10, loc.LOGIN_BUTTON)
    page.driver.find_element(*loc.LOGIN_BUTTON).click()
    page.wait_visibility(10, loc.HEADER_MAIN_PAGE)
