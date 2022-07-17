from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_has_empty_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TAG), 'Basket isnt empty!'

    def is_basket_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_ITEM), 'Basket has item!'

