import math

from selenium.common import NoAlertPresentException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), (
            "Message about adding is not presented")
        message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert message == item_name

    def check_cart_worth(self):
        assert self.is_element_present(*ProductPageLocators.CART_WORTH), (
            "Message cart total is not presented")
        assert self.is_element_present(*ProductPageLocators.ITEM_WORTH), (
            "Product price is not presented")
        cart_worth = self.browser.find_element(*ProductPageLocators.CART_WORTH).text
        item_worth = self.browser.find_element(*ProductPageLocators.ITEM_WORTH).text
        assert cart_worth == item_worth

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED_MESSAGE), 'Success message is not disappeared, ' \
                                                                             'but should  be '


