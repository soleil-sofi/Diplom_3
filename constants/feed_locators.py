from selenium.webdriver.common.by import By

"""Локаторы ленты заказов"""

ORDER_FROM_FEED = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][1]')
ORDER_POPUP = (By.XPATH, './/*[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
CLOSE_ORDER_POPUP = (By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]'
                               '/following-sibling::button')
DONE_TODAY = (By.XPATH, './/p[contains(text(), "за сегодня")]/following-sibling::p')
DONE_ALL = (By.XPATH, './/p[contains(text(), "за все время")]/following-sibling::p')
LAST_FROM_IN_PROCESS = (By.XPATH, './/ul[@class="OrderFeed_orderList__cBvyi"]/li[1]')


def order_number_in_feed(order_number):
    return By.XPATH, (f'.//*[@class="OrderHistory_textBox__3lgbs mb-6"]/p[@class="text text_type_digits-default" '
                      f'and contains(text(), "{order_number}")]')
