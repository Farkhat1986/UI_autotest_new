import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.basic_locators import BasicPageLocators

from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    URL = "https://www.httpwatch.com/httpgallery/authentication/#showExample10"

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = BasicPageLocators()

    @allure.step("Открыть страницу с Basic Auth")
    def open(self) -> None:
        self.open_url(self.URL)

    @allure.step("Нажать кнопку 'Display Image'")
    def click_display_image_button(self) -> None:
        self.click(self.locators.DISPLAY_IMAGE_BUTTON)

    @allure.step("Пройти Basic Auth и открыть защищённое изображение")
    def authenticate_and_load_image(self, username: str = "httpwatch", password: str = "httpwatch") -> None:
        """Обходит нативный диалог Basic Auth через URL с кредами"""
        auth_url = f"https://{username}:{password}@www.httpwatch.com/httpgallery/authentication/authenticatedimage/default.aspx"
        self.open_url(auth_url)

    @allure.step("Проверить, что изображение загружено (авторизация успешна)")
    def is_image_loaded(self) -> bool:
        try:
            img = self.find_visible_element(self.locators.AUTHENTICATED_IMAGE)
            return "default.aspx" in img.get_attribute("src")
        except Exception:
            return False