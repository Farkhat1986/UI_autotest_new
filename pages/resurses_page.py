from locators.locators import PracticLocators

from .base_page import BasePage


class ResursesPage(BasePage):
    URL = "https://www.way2automation.com/"

    def open(self):
        self.driver.get(self.URL)
        return self

    def navigate_to_resurses(self):
        all_courses = self.find_element(PracticLocators.RESOURCES)
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            all_courses,
        )

        self.click(PracticLocators.RESOURCES)
        self.click(PracticLocators.PRACTICE_SITE_1)
