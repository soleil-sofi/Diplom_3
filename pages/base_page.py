import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {url}')
    def follow_page(self, url):
        return self.driver.get(url)

    def scroll_method(self, locator):
        """Скролл к элементу"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility(self, timeout, locator):
        """Ожидание видимости элемента"""
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_clickable(self, timeout, locator):
        """Ожидание кликабельности элемента"""
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def get_text(self, locator):
        """Получить текст элемента"""
        return self.driver.find_element(*locator).text

    def get_value(self, locator, value):
        """Получить значение аттрибута элемента"""
        return self.driver.find_element(*locator).get_attribute(value)

    def replace_element(self, element_locator, place_locator):
        """Переместить элемент"""
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element_locator, place_locator).perform()
