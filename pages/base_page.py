import time
from typing import Any, Tuple

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс для всех Page Object"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует базовую страницу

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """Находит элемент, который присутствует в DOM

        Args:
            locator (Tuple[str, str]): локатор в формате (By.STRATEGY, "value")

        Returns:
            WebElement: Найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator: Tuple[str, str]) -> WebElement:
        """Находит элемент, готовый к клику

        Args:
            locator (Tuple[str, str]): локатор элемента

        Returns:
            WebElement: кликабельный элемент
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator: Tuple[str, str]) -> WebElement:
        """Находит элемент, который виден на странице

        Args:
            locator (Tuple[str, str]): локатор элемента

        Returns:
            WebElement: видимый элемент
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Tuple[str, str]) -> None:
        """Выполняет клик по кликабельному элементу

        Args:
            locator (Tuple[str, str]): локатор элемента
        """
        self.find_clickable_element(locator).click()

    def send_keys(self, locator: Tuple[str, str], text: str) -> None:
        """Очищает поле ввода и вводит указанный текст

        Args:
            locator (Tuple[str, str]): локатор поля ввода
            text (str): текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Получает текст элемента

        Args:
            locator (Tuple[str, str]): локатор элемента

        Returns:
            str: текст элемента
        """
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator: Tuple[str, str]) -> bool:
        """Проверяет, виден ли элемент на странице

        Args:
            locator (Tuple[str, str]): локатор элемента

        Returns:
            bool: True если элемент найден и виден, иначе False
        """
        try:
            self.find_visible_element(locator)
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        """Прокручивает страницу до указанного элемента

        Args:
            locator (Tuple[str, str]): локатор элемента
        """
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({ block: 'center', behavior: 'smooth' });",
            element,
        )

    def scroll_to_bottom(self) -> None:
        """Прокручивает страницу до самого низа"""
        self.driver.execute_script(
            "window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });"
        )

    def scroll(self, pause_time: float = 1, max_attempts: int = 2) -> None:
        """Прокручивает страницу до конца с учётом динамической подгрузки контента

        Args:
            pause_time (float): время ожидания между прокрутками (в секундах)
            max_attempts (int): максимальное количество попыток прокрутки
        """
        attempts = 0
        while attempts < max_attempts:
            self.driver.execute_script(
                "window.scrollTo(0, Math.max(document.body.scrollHeight, document.documentElement.scrollHeight));"
            )

            current_height = self.driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);"
            )

            time.sleep(pause_time)

            new_height = self.driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);"
            )

            if new_height == current_height:
                break

            attempts += 1

    def execute_script(self, script: str, *args) -> Any:
        """Выполняет JavaScript-код в контексте текущей страницы

        Args:
            script (str): JavaScript-код для выполнения
            *args: аргументы, передаваемые в скрипт

        Returns:
            Любое значение, возвращённое JavaScript-кодом
        """
        return self.driver.execute_script(script, *args)

    def open_url(self, url: str) -> None:
        """Открывает указанный URL в браузере

        Args:
            url (str): полный URL для открытия
        """
        self.driver.get(url)

    @allure.step("Снимаем фокус с активного элемента поля ввода")
    def remove_focus(self) -> None:
        """Убирает фокус с любого активного элемента на странице"""
        self.driver.execute_script("document.activeElement?.blur();")

    @allure.step("Проверяем наличие прокрутки на странице")
    def scrollbar(self) -> bool:
        """Возвращает True, если на странице есть вертикальная прокрутка"""
        return self.driver.execute_script(
            "return document.documentElement.scrollHeight > window.innerHeight;"
        )
