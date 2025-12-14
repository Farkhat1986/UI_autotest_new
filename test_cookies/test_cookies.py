import os

import allure
from dotenv import load_dotenv

from test_cookies.login_page_cookies import CookiesPage
from utils.cookies import load_cookies, save_cookies

load_dotenv()


def ensure_logged_in(login_page, username, password):
    """Пльзователь залогинен в противном случае возвращает True, если использовались куки"""
    if load_cookies(login_page.driver):
        login_page.driver.refresh()
        if login_page.is_element_visible(login_page.locators.PERSONAL_PAGE_LINK):
            return True

    login_page.login(username, password)
    assert login_page.is_element_visible(
        login_page.locators.PERSONAL_PAGE_LINK
    ), "Не удалось авторизоваться"
    save_cookies(login_page.driver)
    return False


@allure.epic("Аутентификация")
@allure.feature("Работа с куками")
class TestCookies:

    @allure.story("Авторизация с сохранением куков и повторное использование")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_cookies(self, driver):
        username = os.getenv("SQL_EX_LOGIN")
        password = os.getenv("SQL_EX_PASSWORD")
        assert username, "Переменная окружения SQL_EX_LOGIN не задана"
        assert password, "Переменная окружения SQL_EX_PASSWORD не задана"

        login_page = CookiesPage(driver)
        login_page.open()

        ensure_logged_in(login_page, username, password)

        with allure.step("Фиксируем успешную авторизацию"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="После авторизации",
                attachment_type=allure.attachment_type.PNG,
            )
