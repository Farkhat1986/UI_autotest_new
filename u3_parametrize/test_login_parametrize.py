import allure
import pytest


@allure.epic("Аутентификация")
@allure.feature("Параметризованный сценарий входа")
class TestLoginParametrized:

    @allure.story("Проверка различных сценариев входа")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "username, password, desc, expected_success, expected_message",
        [
            ("angular", "password", "angular", True, "You're logged in!!"),
            (
                "wronguser",
                "password",
                "desc",
                False,
                "Username or password is incorrect",
            ),
            (
                "angular",
                "wrongpass",
                "desc",
                False,
                "Username or password is incorrect",
            ),
            ("", "", "", False, "Username or password is incorrect"),
        ],
        ids=[
            "valid_credentials",
            "invalid_username",
            "invalid_password",
            "empty_fields",
        ],
    )
    def test_login_parametrized(
        self, login_page, username, password, desc, expected_success, expected_message
    ):
        login_page.open()
        login_page.login(username, password, desc)

        if expected_success:
            with allure.step("Проверка сообщения об успешном входе"):
                message = login_page.get_success_message()
                assert (
                    expected_message in message
                ), f"Ожидание: {expected_message}, получено: {message}"

            with allure.step("Выход из системы и проверка возврата на форму входа"):
                login_page.click_logout()
                assert (
                    login_page.is_login_form_visible()
                ), "Форма входа не отображается после выхода"
        else:
            with allure.step("Проверка сообщения об ошибке"):
                message = login_page.get_error_message()
                assert (
                    expected_message in message
                ), f"Ожидание: {expected_message}, получено: {message}"
