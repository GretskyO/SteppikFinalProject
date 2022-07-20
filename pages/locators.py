from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    BOOK_PRICE_MAIN = (By.XPATH, "//*[@class = 'price_color']")
    BOOK_NAME_MAIN = (By.XPATH, "//h1[1]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY_TAG = (By.XPATH, '//*[@id="content_inner"]/p/a')
    BASKET_EMPTY_ITEM = (By.XPATH, '//*[@id="basket_formset"]/div')

class LoginPageLocators():
    EMAIL_FIELD_FOR_REGISTATION = (By.XPATH, '//*[@id="id_registration-email"]')
    PASSWORD_FIELD_FOR_REGISTRATION_MAIN = (By.XPATH, '//*[@id="id_registration-password1"]')
    PASSWORD_FIELD_FOR_REGISTRATION_SECOND = (By.XPATH, '//*[@id="id_registration-password2"]')
    REGISTATION_BUTTOM = (By.XPATH, '//*[@id="register_form"]/button')

