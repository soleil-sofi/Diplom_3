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

"""Конструктор"""
CONSTRUCTOR_BUTTON = (By.XPATH, './/p[contains(text(),"Конструктор")]')
ORDER_FEED_BUTTON = (By.XPATH, './/*[@href="/feed"]')
INGREDIENT = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/a[1]')
INGREDIENT_NAME = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/a[1]/child::p')
HEADER_INGREDIENT_POPUP = (By.XPATH, './/h2[text()="Детали ингредиента"]')
INGREDIENT_NAME_IN_POPUP = (By.XPATH, './/h2[text()="Детали ингредиента"]/following-sibling::p')
INGREDIENT_POPUP = (By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]')
CLOSE_DETAILS_POPUP = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]'
                                 '/following-sibling::button')
INGREDIENT_COUNTER = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/a[1]'
                                '/div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p')
ORDER_SECTION = (By.XPATH, './/li[@class="BurgerConstructor_basket__listItem__aWMu1 mr-4"][2]/div')
MAKE_ORDER_BUTTON = (By.XPATH, './/*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                               'button_button_size_large__G21Vg"]')
CONFIRMATION_POPUP = (By.XPATH, './/*[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]')

"""Лента заказов"""
ORDER_FROM_FEED = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][1]')
ORDER_POPUP = (By.XPATH, './/*[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
CLOSE_ORDER_POPUP = (By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]'
                               '/following-sibling::button')
ORDER_NUMBER = (By.XPATH, './/*[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m '
                               'text text_type_digits-large mb-8"]')
ORDER_NUMBER_FROM_HISTORY = (By.XPATH, './/*[@class="OrderHistory_textBox__3lgbs mb-6"]'
                                       '/p[@class="text text_type_digits-default"]')
DONE_FOR_TODAY = (By.XPATH, './/p[contains(text(), "за сегодня")]/following-sibling::p')
DONE_SUM = (By.XPATH, './/p[contains(text(), "за все время")]/following-sibling::p')
LAST_FROM_IN_PROCESS = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]'
                                  '/li[1]/text()[2]')


def order_number_in_feed(order_number):
    return By.XPATH, f'.//*[contains(text(), "{order_number}")]'
