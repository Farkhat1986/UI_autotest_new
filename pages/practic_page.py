import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL
from locators.practic_page_locator import PracticPageLocators
from pages.base_page import BasePage


class PracticPage(BasePage):
    """Страница для навигации к демо-разделу 'Resizable' на Practice Site 1"""

    URL = f"{BASE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locator = PracticPageLocators()

    @allure.step("Открыть главную страницу сайта")
    def open(self) -> "PracticPage":
        """Открывает главную страницу

        Returns:
            PracticPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step("Перейти в Practice Site 1  затем демо 'Resizable'")
    def practic_test(self) -> None:
        """Выполняет навигацию к демо-примеру 'Resizable' через меню сайта

        Последовательность действий:
        1. Наводится на пункт меню 'Resources' с помощью mouseover
        2. Кликает по 'Resources'
        3. Переходит в 'Practice Site 1'
        4. Кликает по кнопке навигации 'Button'
        5. Выбирает подпункт 'Resizable'
        """
        resources_menu = self.find_element(self.locator.RESOURCES)
        self.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            resources_menu,
        )

    @allure.step("Клик на элемент Resources")
    def click_resources(self):
        self.click(self.locator.RESOURCES)

    @allure.step("Клик на элемент Practice Site 1")
    def click_practice_site_1(self):
        self.click(self.locator.PRACTICE_SITE_1)

    @allure.step("Клик на элемент BUTTON")
    def click_button(self):
        self.click(self.locator.BUTTON)

    @allure.step("Клик на элемент BUTTON RESIZABLE")
    def click_button_resizable(self):
        self.click(self.locator.BUTTON_RESIZABLE)
