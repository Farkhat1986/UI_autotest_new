import allure

from pages.login_page import LoginPage


@allure.epic("UI-взаимодействие")
@allure.feature("JavaScriptExecutor")
class TestExecutorOnLoginPage:

    @allure.story("Управление фокусом и проверка скролла на странице входа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_executor_on_login_page(self, driver):
        """
        Тест выполняет:
            1. Открывает страницу входа
            2. Заполняет форму (фокус появляется на последнем поле)
            3. Убирает фокус через JavaScriptExecutor
            4. Проверяет наличие вертикальной прокрутки
        """
        login_page = LoginPage(driver)
        login_page.open()

        with allure.step("Заполняем форму входа"):
            login_page.fill_login_form("tests", "tests", "tests")

        login_page.remove_focus()

        has_scroll = login_page.scrollbar()

        with allure.step("Проверка наличия вертикальной прокрутки"):
            assert has_scroll is True, "На странице входа должна быть вертикальная прокрутка"

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Страница после работы с JavaScriptExecutor",
            attachment_type=allure.attachment_type.PNG,
        )
