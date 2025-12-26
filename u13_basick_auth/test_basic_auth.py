import allure
from selenium import webdriver

from u13_basick_auth.basic_auth_page import BasicAuthPage


@allure.epic("Аутентификация")
@allure.feature("HTTP Basic Authentication")
class TestBasicAuth:

    @allure.story("Пройти авторизацию по условию задачи U13")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_basic_auth_as_per_requirements(self, driver):
        """
        Реализация по ТЗ:
            1. Открыть страницу
            2. Нажать 'Display Image'
            3. Пройти авторизацию (логин/пароль)
            4. Убедиться, что авторизация успешна
        """
        page = BasicAuthPage(driver)

        with allure.step("Открыть https://www.httpwatch.com/.../authentication/#showExample10"):
            page.open()

        with allure.step("Нажать на кнопку 'Display Image'"):
            page.click_display_image_button()

        with allure.step("Пройти авторизацию (логин 'httpwatch', пароль 'httpwatch')"):
            page.authenticate_and_load_image("httpwatch", "httpwatch")

        with allure.step("Убедиться, что авторизация прошла успешно"):
            assert page.is_image_loaded(), "Изображение не загружено, авторизация не удалась"
