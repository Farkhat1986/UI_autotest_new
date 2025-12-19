from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    USERNAME_DESCRIPTION = (By.NAME, "formly_1_input_username_0")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[ng-click='Auth.login()']")
    SUCCESS_MESSAGE = (By.XPATH, '//p[text()="You\'re logged in!!"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
