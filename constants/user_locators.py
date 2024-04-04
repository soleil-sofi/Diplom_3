from selenium.webdriver.common.by import By

"""Авторизация"""

EMAIL_AUTH_FIELD = (By.NAME, 'name')
PASSWORD_AUTH_FIELD = (By.NAME, 'Пароль')
LOGIN_BUTTON = (By.XPATH, './/button[contains(text(), "Войти")]')
HEADER_MAIN_PAGE = (By.XPATH, './/h1[text()="Соберите бургер"]')

"""Восстановление пароля"""

RESET_PASSWORD_LINK = (By.XPATH, './/*[@href="/forgot-password"]')
EYE_BUTTON = (By.XPATH, './/*[@class="input__icon input__icon-action"]')
EMAIL_FIELD_RESET_PAGE = (By.XPATH, './/*[@class="text input__textfield text_type_main-default"]')
RESET_PASSWORD_BUTTON = (By.XPATH, './/*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                                   'button_button_size_medium__3zxIa"]')
PASSWORD_FIELD = (By.XPATH, './/label[contains(text(), "Пароль")]')

"""Личный кабинет"""

ACCOUNT_BUTTON = (By.XPATH, './/*[@href="/account"]')
ORDER_HISTORY = (By.XPATH, './/*[@href="/account/order-history"]')
LOGOUT_BUTTON = (By.XPATH, './/*[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
