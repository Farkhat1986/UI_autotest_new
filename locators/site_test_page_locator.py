from selenium.webdriver.common.by import By


class TestPageLocators:
    """Локаторы для Test Page"""

    RESOURCES = (
        By.XPATH,
        "//span[@class='menu-text' and text()='Resources']/ancestor::a",
    )
    PRACTICE_SITE_2 = (
        By.XPATH,
        "//a[contains(@href, 'protractor-angularjs-practice-website.html')]",
    )
