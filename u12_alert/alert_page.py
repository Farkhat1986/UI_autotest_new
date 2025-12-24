import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL, ALERT_PAGE_URL
from locators.alert_page_locator import AlertPageLocators
from pages.base_page import BasePage


class AlertsPage(BasePage):
    """Страница для работы с алертами"""

    URL = f"{BASE_URL}{ALERT_PAGE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = AlertPageLocators()

    @allure.step("Открыть страницу с алертами")
    def open(self) -> None:
        self.open_url(self.URL)

    @allure.step("Переключиться на вкладку 'INPUT ALERT'")
    def switch_to_input_alert_tab(self) -> None:
        self.click(self.locators.INPUT_ALERT_TAB)
        self.wait.until(EC.presence_of_element_located(self.locators.IFRAME))

    @allure.step("Дождаться, что iframe загрузил input-alert.html")
    def wait_for_input_alert_frame(self) -> None:
        self.wait.until(
            lambda d: "input-alert.html" in d.find_element(*self.locators.IFRAME).get_attribute("src")
        )

    @allure.step("Переключиться во фрейм")
    def switch_to_iframe(self) -> None:

        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.locators.IFRAME))

        self.wait.until(EC.presence_of_element_located(self.locators.RESULT_MESSAGE))

        self.wait.until(EC.element_to_be_clickable(self.locators.INPUT_ALERT_BUTTON))

    @allure.step("Вернуться из фрейма в основной контент")
    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    @allure.step("Нажать кнопку через JavaScript")
    def click_input_alert_button(self) -> None:
        button = self.find_element(self.locators.INPUT_ALERT_BUTTON)
        self.scroll_to_element(self.locators.INPUT_ALERT_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Ввести текст в prompt")
    def handle_prompt_and_enter_text(self, text: str) -> None:
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
        alert.accept()
        self.wait.until_not(EC.alert_is_present())

    @allure.step("Получить текст результата")
    def get_result_text(self) -> str:
        return self.get_text(self.locators.RESULT_MESSAGE)

    @allure.step("Проверить результат")
    def is_result_contains(self, expected_text: str) -> bool:
        return expected_text in self.get_result_text()