import allure
import pytest


@allure.epic("Аутентификация")
@allure.feature("Параметризованный сценарий входа")
class TestLoginParametrized:

    @allure.story("Успешный вход с валидными данными")
    @pytest.mark.parametrize(
        "username, password, desc, expected_message",
        [
            ("angular", "password", "angular", "You're logged in!!"),
        ],
        ids=["valid_credentials"],
    )
    def test_successful_login(
        self, login_page, username, password, desc, expected_message
    ):
        login_page.open()
        login_page.login(username, password, desc)

        with allure.step("Проверка сообщения об успешном входе"):
            message = login_page.get_success_message()
            assert (
                expected_message in message
            ), f"Ожидалось {expected_message}, получено {message}"

        with allure.step("Выход и проверка возврата на форму"):
            login_page.click_logout()
            assert (
                login_page.is_login_form_visible()
            ), "Форма входа не отображается после выхода"

    @allure.story("Неудачная попытка входа с невалидными данными")
    @pytest.mark.parametrize(
        "username, password, desc, expected_message",
        [
            (
                "wronguser",
                "password",
                "invalid_username",
                "Username or password is incorrect",
            ),
            (
                "angular",
                "wrongpass",
                "invalid_password",
                "Username or password is incorrect",
            ),
            ("", "", "empty_fields", "Username or password is incorrect"),
        ],
        ids=["invalid_username", "invalid_password", "empty_fields"],
    )
    def test_failed_login(self, login_page, username, password, desc, expected_message):
        login_page.open()
        login_page.login(username, password, desc)

        with allure.step("Проверка сообщения об ошибке"):
            message = login_page.get_error_message()
            assert (
                expected_message in message
            ), f"Ожидалось {expected_message}, получено {message}"
