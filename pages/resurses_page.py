import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL
from locators.resurses_page_locator import ResursesPageLocators

from .base_page import BasePage


class ResursesPage(BasePage):
    """Страница для навигации в раздел 'Practice Site 1' через меню Resources"""

    URL = f"{BASE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу ресурсов

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locator = ResursesPageLocators()

    @allure.step("Открыть главную страницу сайта")
    def open(self) -> "ResursesPage":
        """Открывает главную страницу

        Returns:
            ResursesPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step("Перейти в Practice Site 1 через меню Resources")
    def navigate_to_resurses(self) -> None:
        """Выполняет навигацию к 'Practice Site 1' через выпадающее меню 'Resources'

        Последовательность:
        1. Находит элемент меню 'Resources'
        2. Эмулирует событие 'mouseover'
        3. Кликает по 'Resources', затем по 'Practice Site 1
        """
        resources_menu = self.find_element(self.locator.RESOURCES)
        self.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            resources_menu,
        )

    @allure.step("Клик на элемент 'Resources'")
    def click_resources(self):
        """Кликает на элемент Resources"""
        self.click(self.locator.RESOURCES)

    @allure.step("Клик на элемент Practice Site 1")
    def click_practice_site_1(self):
        """Кликает на элемент Practice Site 1"""
        self.click(self.locator.PRACTICE_SITE_1)
