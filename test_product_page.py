from .pages.base_page import BasePage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.get_book_name()
    page.get_book_price()
    page.add_in_busket()
    page.solve_quiz_and_get_code()
    page.is_book_name_correct()
    page.is_book_price_correct()