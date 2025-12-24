from selenium.webdriver.common.by import By


class DropPageLocators:
    IFRAME = (By.CLASS_NAME, "demo-frame")
    DRAGGABLE = (By.ID, "draggable")
    DROPPABLE = (By.ID, "droppable")