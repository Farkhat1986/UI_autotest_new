from selenium.webdriver.common.by import By


class AlertPageLocators:
    IFRAME = (By.CSS_SELECTOR, "iframe[src*='alert/input-alert.html']")
    INPUT_ALERT_TAB = (By.LINK_TEXT, "INPUT ALERT")
    INPUT_ALERT_BUTTON = (By.XPATH, "//button[contains(@onclick, 'myFunction')]")
    RESULT_MESSAGE = (By.ID, "demo")