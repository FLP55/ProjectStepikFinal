from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_send = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_send.send_keys(email)
        password_send = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_send.send_keys(password)
        password_send_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_CONFIRM)
        password_send_confirm.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()
