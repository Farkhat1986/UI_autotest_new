import pytest


class TestBanking:
    @pytest.fixture
    def user_data(self):
        return {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password",
        }

    def test_sample_form_registration(self, banking_page, user_data):
        """Проверка регистрации в Sample Form"""
        banking_page.open()

        banking_page.register_user(user_data)

        success_message = banking_page.get_success_message()
        assert (
            "User registered successfully!" in success_message
        ), f"Сообщение об успешной регистрации не отображается. Получено: {success_message}"
