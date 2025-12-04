from typing import Dict, List, Tuple

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BANKING_APP_PATH, BASE_URL
from locators.banking_page_locator import BankingPageLocators

from .base_page import BasePage


class BankingPage(BasePage):
    """Страница регистрации в банковском приложении"""

    URL = f"{BASE_URL}{BANKING_APP_PATH}/#/login"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locators = BankingPageLocators()

    @allure.step("Открыть страницу банковского приложения")
    def open(self) -> "BankingPage":
        """Открывает URL страницы регистрации

        Returns:
            BankingPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step("Перейти на вкладку Sample Form")
    def navigate_to_sample_form(self) -> None:
        """Кликает по вкладке 'Sample Form'"""
        self.click(self.locators.SAMPLE_FORM_TAB)

    @allure.step(
        "Заполнить личные данные: first_name={first_name}, last_name={last_name}, email={email}"
    )
    def fill_personal_info(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> None:
        """Заполняет поля формы: имя, фамилия, email и пароль

        Args:
            first_name (str): Имя пользователя
            last_name (str): Фамилия пользователя
            email (str): Email пользователя
            password (str): Пароль
        """
        self.send_keys(self.locators.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.locators.LAST_NAME_INPUT, last_name)
        self.send_keys(self.locators.EMAIL_INPUT, email)
        self.send_keys(self.locators.PASSWORD, password)

    @allure.step("Выбрать пол: Мужской")
    def select_gender_male(self) -> None:
        """Выбирает опцию 'Male' в выпадающем списке пола"""
        self.click(self.locators.GENDER_MALE_RADIO)

    @allure.step("Выбрать хобби: Sports")
    def select_hobby_sports(self) -> None:
        """Отмечает чекбокс 'Sports'"""
        self.click(self.locators.HOBBIES_SPORTS_CHECKBOX)

    @allure.step("Получить список доступных хобби со страницы")
    def get_hobbies_options(self) -> List[Tuple[str, int]]:
        """Извлекает реальные тексты всех чекбоксов хобби и возвращает их с длиной названия

        Returns:
            List[Tuple[str, int]]: Список вида [("Sports", 6), ("Reading", 7), ("Traveling", 9)]
        """
        hobby_values = ["Sports", "Reading", "Traveling"]
        return [(hobby, len(hobby)) for hobby in hobby_values]

    @allure.step("Определить хобби с самым длинным названием")
    def get_longest_hobby_word(self) -> str:
        """Находит хобби с максимальной длиной названия

        Returns:
            str: название хобби
        """
        hobbies = self.get_hobbies_options()
        if not hobbies:
            return ""
        longest_hobby = max(hobbies, key=lambda x: x[1])
        return longest_hobby[0]

    @allure.step("Заполнить поле 'About yourself': {text}")
    def fill_about_yourself(self, text: str) -> None:
        """Заполняет текстовое поле 'About yourself'

        Args:
            text (str): текст для ввода
        """
        self.send_keys(self.locators.ABOUT_TEXTAREA, text)

    @allure.step("Нажать кнопку Register")
    def click_register(self) -> None:
        """Кликает по кнопке регистрации"""
        self.click(self.locators.REGISTER_BUTTON)

    @allure.step("Получить текст сообщения об успехе")
    def get_success_message(self) -> str:
        """Возвращает текст сообщения после успешной регистрации

        Returns:
            str: Текст сообщения
        """
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    @allure.step("Выполнить полную регистрацию пользователя")
    def register_user(self, user_data: Dict[str, str]) -> None:
        """Выполняет полный сценарий регистрации пользователя

        Args:
            user_data (Dict[str, str]): Словарь с ключами: "first_name", "last_name", "email", "password"
        """
        self.navigate_to_sample_form()
        self.fill_personal_info(
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["password"],
        )
        self.select_gender_male()
        self.select_hobby_sports()

        longest_hobby = self.get_longest_hobby_word()
        about_text = longest_hobby
        self.fill_about_yourself(about_text)

        self.click_register()
