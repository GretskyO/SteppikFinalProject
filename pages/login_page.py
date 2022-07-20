from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.browser.find_element(By.XPATH, '//*[@id="login_form"]'), "Net formi logina"

    def should_be_register_form(self):
        assert self.browser.find_element(By.XPATH, '//*[@id="register_form"]'), 'net formi registacii'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_FOR_REGISTATION)
        email_field.send_keys(email)
        password_filed1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_FOR_REGISTRATION_MAIN)
        password_filed1.send_keys(password)
        password_filed2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_FOR_REGISTRATION_SECOND)
        password_filed2.send_keys(
            password)
        self.browser.find_element(*LoginPageLocators.REGISTATION_BUTTOM).click()
