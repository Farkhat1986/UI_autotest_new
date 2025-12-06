import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL
from locators.site_test_page_locator import TestPageLocators

from .base_page import BasePage


class SiteTestPage(BasePage):
    """Страница для перехода к Practice Site 2 через выпадающее меню Resources"""

    URL = f"{BASE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locator = TestPageLocators()

    @allure.step("Открыть главную страницу сайта")
    def open(self) -> "SiteTestPage":
        """Открывает главную страницу

        Returns:
            SiteTestPage: Текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step("Перейти в Practice Site 2 через выпадающее меню Resources")
    def form_test(self) -> None:
        """Выполняет навигацию к 'Practice Site 2' через меню 'Resources'

        Последовательность действий:
        1. Находит элемент меню 'Resources'
        2. Эмулирует наведение курсора
        3. Кликает по 'Resources', затем по ссылке 'Practice Site 2'
        """
        resources_menu = self.find_element(self.locator.RESOURCES)
        self.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            resources_menu,
        )

    @allure.step("Клик на элемент 'Resources'")
    def click_resources(self):
        """Кликает на элемент 'Resources'"""
        self.click(self.locator.RESOURCES)

    @allure.step("Клик на элемент Practice Site 2")
    def click_practice_site_2(self):
        """Кликает на элемент Practice Site 2"""
        self.click(self.locator.PRACTICE_SITE_2)
