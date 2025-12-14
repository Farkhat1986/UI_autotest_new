from allure import step

from config import COOKIES_PAGE_URL
from locators.cookies_page_locator import CookiesPageLocators
from pages.base_page import BasePage


class CookiesPage(BasePage):
    """Страница авторизации на сайте sql-ex.ru"""

    URL = f"{COOKIES_PAGE_URL}"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CookiesPageLocators()

    @step("Открыть страницу авторизации")
    def open(self) -> "CookiesPage":
        """Открывает URL страницы входа на sql-ex.ru

        Returns:
            LoginPage: текущий экземпляр для цепочки вызовов
        """
        self.driver.get(self.URL)
        return self

    @step("Выполнить вход с логином '{username}'")
    def login(self, username: str, password: str) -> None:
        """Выполняет авторизацию на сайте заполняя форму логина и пароля

        Args:
            username (str): имя пользователя
            password (str): пароль пользователя

        Note:
            Метод не проверяет результат входа только отправляет форму
            Для проверки успешной авторизации используйте отдельные провер
        """
        self.send_keys(self.locators.USERNAME_INPUT, username)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)
