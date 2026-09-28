from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # таймаут по умолчанию для явных ожиданий (неявное ожидание не используем)
        self.timeout = timeout

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=None):
        if timeout is None:
            timeout = self.timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=1).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"

    def should_be_user_cart(self):
        assert self.is_element_present(*BasePageLocators.USER_CART), "User cart is not present"

    def go_to_user_cart(self):
        cart = self.browser.find_element(*BasePageLocators.USER_CART)
        cart.click()

    def is_user_authorized(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User icon is absent, probably unauthorized user'
