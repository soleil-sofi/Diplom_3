from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_method(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    def wait_visibility(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_clickable(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_number_of_windows(self, timeout, number):
        WebDriverWait(self.driver, timeout).until(expected_conditions.number_of_windows_to_be(number))

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_value(self, locator, value):
        return self.driver.find_element(*locator).get_attribute(value)

    def replace_element(self, locator_1, locator_2):
        element = self.driver.find_element(*locator_1)
        target = self.driver.find_element(*locator_2)
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element, target).perform()
