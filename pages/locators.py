from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")
    BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    BOOK_PRICE_MAIN = (By.XPATH, "//*[@class = 'price_color']")
    BOOK_NAME_MAIN = (By.XPATH, "//h1[1]")