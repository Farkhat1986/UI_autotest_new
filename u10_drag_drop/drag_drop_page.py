import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL, DROP_PAGE_URL
from locators.drop_page_locator import DropPageLocators
from pages.base_page import BasePage


class DragDropPage(BasePage):
    """Страница для тестирования Drag and Drop"""

    URL = f"{BASE_URL}{DROP_PAGE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = DropPageLocators()

    @allure.step("Открыть страницу Drag and Drop")
    def open(self) -> "DragDropPage":
        self.open_url(self.URL)
        return self

    @allure.step("Переключиться во фрейм с демо-контентом")
    def switch_to_iframe(self) -> None:
        """Переключается в iframe, где находится drag and drop"""
        iframe_element = self.find_element(self.locators.IFRAME)
        self.driver.switch_to.frame(iframe_element)

    @allure.step("Вернуться в основной контекст страницы")
    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    @allure.step("Выполнить перетаскивание элемента в зону приёма")
    def perform_drag_and_drop(self) -> None:
        """Перетаскивает draggable элемент в droppable зону"""
        draggable = self.find_element(self.locators.DRAGGABLE)
        droppable = self.find_element(self.locators.DROPPABLE)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    @allure.step("Получить текст зоны приёма")
    def get_droppable_text(self) -> str:
        return self.get_text(self.locators.DROPPABLE)

    @allure.step("Проверить, что текст зоны приёма изменился на 'Dropped!'")
    def is_dropped_successful(self) -> bool:
        text = self.get_droppable_text()
        return text.strip() == "Dropped!"