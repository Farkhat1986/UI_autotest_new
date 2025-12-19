import allure


@allure.epic("Аутентификация")
@allure.feature("Сценарий входа и выхода")
class TestLogin:

    @allure.story(
        "Проверка, что все элементы формы входа отображаются, и кнопка Login изначально отключена"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_form_elements(self, login_page):
        """Проверка полей ввода и состояния кнопки"""
        login_page.open()

        assert login_page.is_element_visible(
            login_page.locators.USERNAME_INPUT
        ), "Поле Username не отображается"
        assert login_page.is_element_visible(
            login_page.locators.PASSWORD_INPUT
        ), "Поле Password не отображается"
        assert login_page.is_element_visible(
            login_page.locators.USERNAME_DESCRIPTION
        ), "Поле Description не отображается"
        assert login_page.is_element_visible(
            login_page.locators.LOGIN_BUTTON
        ), "Кнопка Login не заблокирована при пустых полях"

    @allure.story("Успешный вход с валидными учетными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, login_page):
        """Проверка успешной авторизации"""
        login_page.open()

        login_page.login("angular", "password", "angular")

        success_message = login_page.get_success_message()
        assert (
            "You're logged in!!" in success_message
        ), f"Сообщение об успешной авторизации не отображается. Получено: {success_message}"

    @allure.story("Неудачный вход с невалидными учетными данными")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login(self, login_page):
        """Проверка авторизации с невалидными данными"""
        login_page.open()

        login_page.login("invaliduser", "wrongpassword", "ner")

        error_message = login_page.get_error_message()
        assert (
            "Username or password is incorrect" in error_message
        ), f"Сообщение об ошибке не отображается. Получено: {error_message}"

    @allure.story("Успешный выход и возврат на форму входа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_logout(self, login_page):
        """Проверка успешного разлогирования"""
        login_page.open()

        login_page.login("angular", "password", "angular")

        login_page.click_logout()

        assert (
            login_page.is_login_form_visible()
        ), "Форма логина не отображается после разлогирования"
