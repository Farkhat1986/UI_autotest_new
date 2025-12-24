import allure
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL, TABS_PAGE_URL
from locators.tabs_page_locator import TabsPageLocators


from pages.base_page import BasePage

class TabsPage(BasePage):
    URL = f"{BASE_URL}{TABS_PAGE_URL}"

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = TabsPageLocators()

    @allure.step("Открыть страницу с iframe")
    def open(self) -> "TabsPage":
        self.open_url(self.URL)
        return self

    @allure.step("Переключиться во фрейм и нажать ссылку 'New Browser Tab'")
    def open_new_tab_from_iframe(self) -> None:
        iframe_element = self.find_element(self.locators.IFRAME)
        self.driver.switch_to.frame(iframe_element)
        self.click(self.locators.NEW_TAB_LINK)
        self.driver.switch_to.default_content()

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self, original_window_handle: str) -> str:
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != original_window_handle:
                self.driver.switch_to.window(handle)
                return handle
        raise RuntimeError("Не удалось найти новую вкладку")

    @allure.step("Попытаться открыть ещё одну вкладку")
    def open_another_tab_if_possible(self) -> bool:
        try:
            self.click(self.locators.NEW_TAB_LINK)
            return True
        except Exception:
            return False

    @allure.step("Открыть третью вкладку через JavaScript (резервный способ)")
    def open_third_tab_via_js(self) -> None:
        self.driver.execute_script("window.open('about:blank', '_blank');")

    @allure.step("Получить количество открытых вкладок")
    def get_window_handles_count(self) -> int:
        return len(self.driver.window_handles)