

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=0):
        try:
            # self.browser.find_element(how, what)
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
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
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]).\
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
