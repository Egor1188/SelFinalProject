from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # тайм-аут по умолчанию для явных ожиданий (неявное ожидание не используем)
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

    def should_have_text(self, how, what, expected_text, exact=True, timeout=None):
        # exact=True — текст элемента полностью совпадает (как have.text), exact=False — содержит подстроку
        if timeout is None:
            timeout = self.timeout

        def text_matches(browser):
            try:
                actual = browser.find_element(how, what).text.strip()
            except (NoSuchElementException, StaleElementReferenceException):
                return False
            return actual == expected_text if exact else expected_text in actual

        try:
            WebDriverWait(self.browser, timeout).until(text_matches)
        except TimeoutException:
            try:
                actual = self.browser.find_element(how, what).text.strip()
            except NoSuchElementException:
                actual = "<element not found>"
            raise AssertionError(
                f"Element {(how, what)} should {'have' if exact else 'contain'} text "
                f"'{expected_text}', but actual text is '{actual}'")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"

    def should_be_user_cart(self):
        assert self.is_element_present(*BasePageLocators.USER_CART), "User cart is not present"

    def go_to_user_cart(self):
        cart = self.browser.find_element(*BasePageLocators.USER_CART)
        cart.click()

    def is_user_authorized(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User icon is absent, probably unauthorized user'
