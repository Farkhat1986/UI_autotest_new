import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL
from locators.home_page_locator import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    """Главная страница сайта"""

    URL = f"{BASE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует главную страницу

        Args:
            driver (WebDriver): зкземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locators = HomePageLocators()

    @allure.step("Открыть главную страницу")
    def open(self) -> "HomePage":
        """Открывает главную страницу сайта

        Returns:
            HomePage: текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step("Перейти на Practice Site через меню Resources")
    def form_test(self) -> None:
        """Выполняет навигацию к Practice Site через выпадающее меню 'Resources'"""
        resources_menu = self.find_element(self.locators.RESOURCES)

        self.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            resources_menu,
        )

        self.click(self.locators.RESOURCES)
        self.click(self.locators.PRACTICE_SITE_2)
        self.click(self.locators.HOME)
