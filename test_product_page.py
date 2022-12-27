from pages.product_page import ProductPage
import time
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.check_cart_worth()

    # time.sleep(180)