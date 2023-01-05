import pytest

from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.user_cart import UserCart


@pytest.mark.login_test
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_user_cart()
    page.go_to_user_cart()
    page = UserCart(browser, browser.current_url)
    page.is_empty()
