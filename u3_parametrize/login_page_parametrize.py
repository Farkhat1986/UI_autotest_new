import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL, REGISTRATION_APP_PATH
from locators.login_page_locator import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница входа в приложение регистрации на сайте"""

    URL = f"{BASE_URL}{REGISTRATION_APP_PATH}/#/login"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу входа

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Открыть страницу входа")
    def open(self) -> "LoginPage":
        """Открывает URL страницы входа

        Returns:
            LoginPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step(
        "Заполнить форму входа с username='{username}', password='{password}' и description='{desc}'"
    )
    def fill_login_form(self, username: str, password: str, desc: str) -> None:
        """Заполняет поля формы входа: имя пользователя, пароль и описание

        Args:
            username (str): имя пользователя
            password (str): пароль
            desc (str): описание пользователя
        """
        self.send_keys(self.locators.USERNAME_INPUT, username)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.send_keys(self.locators.USERNAME_DESCRIPTION, desc)

    @allure.step("Нажать кнопку 'Login'")
    def click_login(self) -> None:
        """Выполняет клик по кнопке входа"""
        self.click(self.locators.LOGIN_BUTTON)

    @allure.step("Получить текст сообщения об успехе")
    def get_success_message(self) -> str:
        """Возвращает текст сообщения об успешном входе

        Returns:
            str: текст сообщения
        """
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    @allure.step("Получить текст сообщения об ошибке")
    def get_error_message(self) -> str:
        """Возвращает текст сообщения об ошибке входа

        Returns:
            str: текст ошибки
        """
        return self.get_text(self.locators.ERROR_MESSAGE)

    @allure.step("Нажать кнопку 'Logout'")
    def click_logout(self) -> None:
        """Выполняет клик по кнопке выхода из системы"""
        self.click(self.locators.LOGOUT_BUTTON)

    @allure.step(
        "Выполнить полный вход с username='{username}', password='{password}', description='{desc}'"
    )
    def login(self, username: str, password: str, desc: str) -> None:
        """Выполняет полный сценарий входа: заполняет все поля и нажимает 'Login'

        Args:
            username (str): имя пользователя
            password (str): пароль
            desc (str): описание пользователя
        """
        self.fill_login_form(username, password, desc)
        self.click_login()

    @allure.step("Проверить, видна ли вся форма входа")
    def is_login_form_visible(self) -> bool:
        """Проверяет, что все поля формы входа видны одновременно

        Returns:
            bool: True, если все поля видны, иначе False
        """
        return (
            self.is_element_visible(self.locators.USERNAME_INPUT)
            and self.is_element_visible(self.locators.PASSWORD_INPUT)
            and self.is_element_visible(self.locators.USERNAME_DESCRIPTION)
        )
