from selenium.webdriver.common.by import By


class CookiesPageLocators:
    """Локаторы для Cookies"""

    USERNAME_INPUT = (By.NAME, "login")
    PASSWORD_INPUT = (By.NAME, "psw")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Вход']")
    PERSONAL_PAGE_LINK = (By.XPATH, "//h2[text()='Практическое владение языком SQL']")
