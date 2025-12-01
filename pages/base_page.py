import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator):
        try:
            self.find_visible_element(locator)
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll(self, pause_time=1):
        """Прокручивает страницу до самого конца, даже если контент подгружается динамически"""
        while True:

            self.driver.execute_script(
                "window.scrollTo(0, Math.max(document.body.scrollHeight, document.documentElement.scrollHeight));"
            )

            current_height = self.driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);"
            )
            time.sleep(pause_time)
            new_height = self.driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);"
            )
            if new_height == current_height:
                break
