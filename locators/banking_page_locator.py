from selenium.webdriver.common.by import By


class BankingPageLocators:
    """Локаторы для формы регистрации в банковском приложении"""

    SAMPLE_FORM_TAB = (By.XPATH, "//a[contains(text(), 'Sample Form')]")

    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    GENDER_MALE_RADIO = (By.XPATH, "//select[@id='gender']/option[@value='male']")
    HOBBIES_SPORTS_CHECKBOX = (By.CSS_SELECTOR, "input[value='Sports']")
    HOBBIES_READING_CHECKBOX = (By.CSS_SELECTOR, "input[value='Reading']")
    HOBBIES_TRAVELING_CHECKBOX = (By.CSS_SELECTOR, "input[value='Traveling']")
    HOBBIES = (By.CSS_SELECTOR, "input[type='checkbox']")
    ABOUT_TEXTAREA = (By.NAME, "about")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "successMessage")
