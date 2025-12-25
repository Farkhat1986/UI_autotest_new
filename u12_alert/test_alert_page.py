import allure

from u12_alert.alert_page import AlertsPage


@allure.epic("JavaScript диалоги")
@allure.feature("Работа с алертами")
class TestAlerts:

    @allure.story("Ввести текст в Input Alert и проверить отображение результата")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_input_alert_with_custom_text(self, driver):
        """
        1. Открыть страницу с алертами
        2. Переключиться на вкладку 'INPUT ALERT'
        3. Переключиться во фрейм
        4. Нажать кнопку, вызывающую prompt
        5. Ввести кастомный текст
        6. Подтвердить
        7. Убедиться, что текст отобразился
        """
        custom_text = "Farhat"
        expected_message = f"Hello {custom_text}! How are you today?"

        page = AlertsPage(driver)

        with allure.step("Открыть страницу с алертами"):
            page.open()

        with allure.step("Переключиться на вкладку 'INPUT ALERT'"):
            page.switch_to_input_alert_tab()

        with allure.step("Переключиться во фрейм"):
            page.switch_to_iframe()

        with allure.step("Нажать кнопку, вызывающую prompt"):
            page.click_input_alert_button()

        with allure.step(f"Ввести текст '{custom_text}' в prompt и подтвердить"):
            page.handle_prompt_and_enter_text(custom_text)

        with allure.step(f"Проверить, что отображается сообщение: '{expected_message}'"):
            actual_result = page.get_result_text()
            assert custom_text in actual_result, f"Ожидалось сообщение, содержащее '{custom_text}', получено: '{actual_result}'"

            assert actual_result == expected_message, f"Ожидалось: '{expected_message}', получено: '{actual_result}'"