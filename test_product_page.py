import pytest

from pages.product_page import ProductPage
import time

from pages.user_cart import UserCart

# https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.
items = [
    'coders-at-work_207/?promo=newYear2019',
    'coders-at-work_207/?promo=offer0',
    'coders-at-work_207/?promo=offer1',
    'coders-at-work_207/?promo=offer2',
    'coders-at-work_207/?promo=offer3',
    'coders-at-work_207/?promo=offer4',
    'coders-at-work_207/?promo=offer5',
    'coders-at-work_207/?promo=offer6',
    pytest.param('coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail),
    'coders-at-work_207/?promo=offer8',
    'coders-at-work_207/?promo=offer9',
    'the-shellcoders-handbook_209/?promo=newYear'
]


@pytest.mark.skip
@pytest.mark.parametrize('item', items)
def test_guest_can_add_product_to_basket(browser, item):
    link = f'https://selenium1py.pythonanywhere.com/catalogue/{item}'
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.check_cart_worth()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser=browser, url=link, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser=browser, url=link, timeout=0)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.go_to_login_page()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.should_be_user_cart()
    page.go_to_user_cart()
    page = UserCart(browser, browser.current_url)
    page.is_empty()

    # time.sleep(180)
