from pages.base_page import BasePage
from pages.locators import  UserCartLocators


class UserCart(BasePage):
    def is_empty(self):
        self.is_element_present(*UserCartLocators.CART_IS_EMPTY)
        self.is_not_element_present(*UserCartLocators.CART_ITEM)
        self.is_element_present(*UserCartLocators.CART_IS_EMPTY)
       
