from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [f"{product_base_link}?promo=offer{no}" if no != "7"
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]

# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser, link):
#     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.get_book_name()
#     page.get_book_price()
#     page.add_in_busket()
#     page.solve_quiz_and_get_code()
#     page.is_book_name_correct()
#     page.is_book_price_correct()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.get_book_name()
#     page.get_book_price()
#     page.add_in_busket()
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()


# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.get_book_name()
#     page.get_book_price()
#     page.add_in_busket()
#     page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_has_empty_link()
    basket_page.is_basket_no_items()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_has_empty_link()
    basket_page.is_basket_no_items()

