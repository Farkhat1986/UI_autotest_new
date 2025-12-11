from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы для Home Page"""

    RESOURCES = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Resources']/ancestor::a",
    )
    PRACTICE_SITE_2 = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Practice Site 2']/ancestor::a",
    )
    HOME = (By.LINK_TEXT, "Home")
