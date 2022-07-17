from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    book_name = ''
    book_price = ''

    def get_book_name(self):
        self.book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MAIN).text

    def get_book_price(self):
        self.book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MAIN).text

    def add_in_busket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def is_book_name_correct(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.book_name, 'wrong book'

    def is_book_price_correct(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.book_price, 'wrong price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_NAME), "Success message is presented, but should not be"