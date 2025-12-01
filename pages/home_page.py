from locators.locators import PracticLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.way2automation.com/"

    def open(self):
        self.driver.get(self.URL)
        return self

    def form_test(self):
        all_courses = self.find_element(PracticLocators.RESOURCES)
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            all_courses,
        )

        self.click(PracticLocators.RESOURCES)
        self.click(PracticLocators.PRACTICE_SITE_2)
        self.click(PracticLocators.HOME)
