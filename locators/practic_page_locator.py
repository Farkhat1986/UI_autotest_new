from selenium.webdriver.common.by import By


class PracticPageLocators:
    """Локаторы для Practic Page"""

    RESOURCES = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Resources']/ancestor::a",
    )
    PRACTICE_SITE_1 = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Practice Site 1']/ancestor::a",
    )
    BUTTON = (By.CSS_SELECTOR, "[data-testid='enter-testing-site']")
    BUTTON_RESIZABLE = (By.CSS_SELECTOR, "[data-testid='resizable-link']")
