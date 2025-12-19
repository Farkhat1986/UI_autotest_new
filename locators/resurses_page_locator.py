from selenium.webdriver.common.by import By


class ResursesPageLocators:
    """Локаторы для Resurses Page"""

    RESOURCES = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Resources']/ancestor::a",
    )
    PRACTICE_SITE_1 = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Practice Site 1']/ancestor::a",
    )
