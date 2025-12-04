from typing import List

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL
from locators.main_page_locator import MainPageLocators

from .base_page import BasePage


class MainPage(BasePage):
    """Главная страница сайта"""

    URL = f"{BASE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует главную страницу

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Открыть главную страницу")
    def open(self) -> "MainPage":
        """Открывает главную страницу сайта

        Returns:
            MainPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.open_url(self.URL)
        return self

    @allure.step("Проверить, видна ли контактная информация в шапке")
    def is_header_contact_visible(self) -> bool:
        """Проверяет видимость контактной информации в верхнем хедере

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_visible(self.locators.HEADER_CONTACT)

    @allure.step("Получить количество номеров телефонов в шапке")
    def get_phone_numbers_count(self) -> int:
        """Считает количество телефонных номеров в хедере

        Returns:
            int: количество найденных элементов с телефонами
        """
        return len(self.driver.find_elements(*self.locators.PHONE_NUMBERS))

    @allure.step("Получить количество ссылок на соцсети в шапке")
    def get_social_links_count(self) -> int:
        """Считает количество иконок/ссылок на социальные сети в хедере

        Returns:
            int: количество найденных ссылок
        """
        return len(self.driver.find_elements(*self.locators.SOCIAL_LINKS))

    @allure.step("Проверить, присутствует ли ссылка на Skype в шапке")
    def is_skype_link_present(self) -> bool:
        """Проверяет наличие ссылки на Skype в хедере

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_present(self.locators.SKYPE_LINK)

    @allure.step("Проверить, присутствует ли ссылка на Email в шапке")
    def is_email_link_present(self) -> bool:
        """Проверяет наличие email в хедере

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_present(self.locators.EMAIL_LINK)

    @allure.step("Проверить, виден ли основной блок навигации")
    def is_navigation_block_visible(self) -> bool:
        """Проверяет видимость основного навигационного блока

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_visible(self.locators.NAVIGATION_BLOCK)

    @allure.step("Проверить, видна ли кнопка 'Register'")
    def is_register_button_visible(self) -> bool:
        """Проверяет видимость кнопки регистрации в навигации

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_visible(self.locators.REGISTER_BUTTON_I)

    @allure.step("Проверить, виден ли блок курсов")
    def is_courses_section_visible(self) -> bool:
        """Проверяет видимость секции с популярными курсами

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_visible(self.locators.COURSES_SECTION)

    @allure.step("Проверить, виден ли футер")
    def is_footer_visible(self) -> bool:
        """Проверяет видимость подвала сайта

        Returns:
            bool: True, если поле видно если нет то False
        """
        return self.is_element_visible(self.locators.FOOTER)

    @allure.step("Получить текст адреса из футера")
    def get_footer_address(self) -> str:
        """Возвращает текст адреса из футера сайта

        Returns:
            str: текст адреса
        """
        return self.get_text(self.locators.FOOTER_ADDRESS)

    @allure.step("Получить количество телефонов в футере")
    def get_footer_phones_count(self) -> int:
        """Считает количество телефонных номеров в футере

        Returns:
            int: количество найденных телефонов
        """
        return len(self.driver.find_elements(*self.locators.FOOTER_PHONES))

    @allure.step("Получить количество email в футере")
    def get_footer_emails_count(self) -> int:
        """Считает количество email-адресов в футере

        Returns:
            int: количество найденных email
        """
        return len(self.driver.find_elements(*self.locators.FOOTER_EMAILS))

    @allure.step("Нажать кнопку 'Next' в слайдере курсов")
    def click_course_slider_next(self) -> None:
        """Выполняет клик по кнопке 'Next' в карусели курсов"""
        self.click(self.locators.COURSE_SLIDER_NEXT)

    @allure.step("Нажать кнопку 'Prev' в слайдере курсов")
    def click_course_slider_prev(self) -> None:
        """Выполняет клик по кнопке 'Prev' в карусели курсов"""
        self.click(self.locators.COURSE_SLIDER_PREV)

    @allure.step("Получить заголовки активных слайдов курсов")
    def get_active_course_slides(self) -> List[str]:
        """Возвращает список текстов текущих видимых слайдов курсов

        Returns:
            List[str]: список названий курсов с активных слайдов
        """
        slides = self.driver.find_elements(*self.locators.COURSE_SLIDES)
        if not slides:
            return []
        return [slide.text.strip() for slide in slides if slide.text.strip()]

    @allure.step("Прокрутить страницу до самого низа")
    def scroll_down(self) -> None:
        """Прокручивает страницу до конца"""
        self.scroll_to_bottom()

    @allure.step("Проверить, видна ли 'липкая' навигация после прокрутки")
    def is_sticky_nav_visible(self) -> bool:
        """Проверяет появление фиксированной навигационной панели при прокрутке

        Returns:
            bool: True, если 'sticky' навигация видна, если нет то False
        """
        return self.is_element_visible(self.locators.STICKY_NAV)

    @allure.step("Перейти в 'Lifetime Membership' через меню All Courses")
    def navigate_to_lifetime_membership(self) -> None:
        """Выполняет навигацию к разделу 'Lifetime Membership' через выпадающее меню"""
        all_courses = self.find_element(self.locators.ALL_COURSES_MENU)
        self.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            all_courses,
        )
        self.click(self.locators.LIFETIME_MEMBERSHIP_SUBMENU)
