from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, '#messages > div > div > strong')
    ITEM_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    CART_WORTH = (By.CSS_SELECTOR, '#messages > :nth-child(3) > div > p > strong')
    ITEM_WORTH = (By.CSS_SELECTOR, '.col-sm-6.product_main > .price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")