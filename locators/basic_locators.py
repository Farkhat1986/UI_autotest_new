from selenium.webdriver.common.by import By


class BasicPageLocators:
    DISPLAY_IMAGE_BUTTON = (By.XPATH, "//input[@value='Display Image']")
    AUTHENTICATED_IMAGE = (By.TAG_NAME, "img")