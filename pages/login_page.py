from locators.locators import InputLocators, MessageLocators

from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    def open(self):
        self.driver.get(self.URL)
        return self

    def is_username_field_visible(self):
        return self.is_element_visible(InputLocators.USERNAME_INPUT)

    def is_password_field_visible(self):
        return self.is_element_visible(InputLocators.PASSWORD_INPUT)

    def is_username_description_field_visible(self):
        return self.is_element_visible(InputLocators.USERNAME_DESCRIPTION)

    def is_login_button_disabled(self):
        button = self.find_element(InputLocators.LOGIN_BUTTON)
        return button.get_attribute("disabled") is not None

    def enter_username(self, username):
        self.send_keys(InputLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(InputLocators.PASSWORD_INPUT, password)

    def enter_username_description(self, desc):
        self.send_keys(InputLocators.USERNAME_DESCRIPTION, desc)

    def click_login(self):
        self.click(InputLocators.LOGIN_BUTTON)

    def get_success_message(self):
        return self.get_text(MessageLocators.SUCCESS_MESSAGE_I)

    def get_error_message(self):
        return self.get_text(MessageLocators.ERROR_MESSAGE)

    def click_logout(self):
        self.click(MessageLocators.LOGOUT_BUTTON)

    def login(self, username, password, desc):
        self.enter_username(username)
        self.enter_password(password)
        self.enter_username_description(desc)
        self.click_login()

    def is_login_form_visible(self):
        return (
            self.is_element_visible(InputLocators.USERNAME_INPUT)
            and self.is_element_visible(InputLocators.PASSWORD_INPUT)
            and self.is_element_visible(InputLocators.USERNAME_DESCRIPTION)
        )
