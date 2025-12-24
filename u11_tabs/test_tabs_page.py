import allure
from selenium import webdriver

from u11_tabs.tabs_page import TabsPage


@allure.epic("Работа с окнами и вкладками")
@allure.feature("Управление вкладками через target='_blank'")
class TestTabs:

    @allure.story("Открытие новой вкладки из iframe")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_new_tab(self, driver):
        """
            1. Открыть страницу с iframe
            2. Нажать ссылку 'New Browser Tab'
            3. Переключиться на новую вкладку
            4. Убедиться, что открыто 2 вкладки
        """
        page = TabsPage(driver)
        original_window = driver.current_window_handle

        with allure.step("Открыть страницу с iframe"):
            page.open()

        with allure.step("Нажать ссылку 'New Browser Tab' внутри iframe"):
            page.open_new_tab_from_iframe()

        with allure.step("Переключиться на вторую вкладку"):
            page.switch_to_new_window(original_window)

        with allure.step("Проверить, что открыто ровно 2 вкладки"):
            window_count = page.get_window_handles_count()
            assert window_count == 2, f"Ожидалось 2 вкладки, открыто: {window_count}"

        current_title = driver.title
        assert "New Browser Tab" in current_title or "Datepicker" in current_title, f"Ожидался заголовок с 'New Browser Tab' или 'Datepicker', получено: {current_title}"