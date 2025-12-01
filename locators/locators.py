from selenium.webdriver.common.by import By


class PageLocators:
    """Локаторы для формы"""

    SAMPLE_FORM_TAB = (By.XPATH, "//a[contains(text(), 'Sample Form')]")

    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    GENDER_MALE_RADIO = (By.XPATH, "//select[@id='gender']/option[@value='male']")
    HOBBIES_SPORTS_CHECKBOX = (By.CSS_SELECTOR, "input[value='Sports']")
    HOBBIES = (By.CSS_SELECTOR, "input[type='checkbox']")
    HOBBIES_SPORTSS_CHECKBOX = (By.CSS_SELECTOR, "input[value='Sports']")
    HOBBIES_READING_CHECKBOX = (By.CSS_SELECTOR, "input[value='Reading']")
    HOBBIES_TRAVELING_CHECKBOX = (By.CSS_SELECTOR, "input[value='Traveling']")
    ABOUT_TEXTAREA = (By.NAME, "about")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "successMessage")


class InputLocators:
    """Локаторы для полей ввода"""

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    USERNAME_DESCRIPTION = (By.NAME, "formly_1_input_username_0")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[ng-click='Auth.login()']")


class MessageLocators:
    """Локаторы для сообщений"""

    SUCCESS_MESSAGE_I = (By.XPATH, '//p[text()="You\'re logged in!!"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")


class HeaderLocators:
    """Локаторы для хедера с контактной информацией"""

    HEADER_CONTACT = (By.TAG_NAME, "header")
    PHONE_NUMBERS = (By.TAG_NAME, "span")
    SKYPE_LINK = (By.CSS_SELECTOR, "a[href*='skype']")
    EMAIL_LINK = (By.CSS_SELECTOR, "a[href*='mailto']")
    SOCIAL_LINKS = (By.CSS_SELECTOR, ".ast-header-social-1-wrap a")


class NavigationLocators:
    """Локаторы для основной навигации"""

    NAVIGATION_BLOCK = NAV_MENU = (By.TAG_NAME, "nav")
    REGISTER_BUTTON_I = (By.LINK_TEXT, "Register Now")


class CursesLocators:
    """Локаторы для курсов"""

    COURSES_SECTION = (By.XPATH, "//h1[contains(text(),'Best Selenium')]")
    POPULAR_COURSES_SECTION = (
        By.XPATH,
        "//h2[contains(text(), 'Most Popular Software Testing Courses')]",
    )
    COURSE_SLIDER_NEXT = (By.CSS_SELECTOR, ".elementor-swiper-button-next")
    COURSE_SLIDER_PREV = (By.CSS_SELECTOR, ".elementor-swiper-button-prev")
    COURSE_SLIDES = (
        By.CSS_SELECTOR,
        ".pp-info-box-container .swiper-wrapper > .swiper-slide:first-child",
    )


class FooterLocators:
    """Локаторы для футера"""

    FOOTER = (By.TAG_NAME, "footer")
    FOOTER_ADDRESS = (By.CLASS_NAME, "elementor-icon-list-text")
    FOOTER_PHONES = (By.TAG_NAME, "span")
    FOOTER_EMAILS = (By.CSS_SELECTOR, "a[href*='mailto']")


class NavigationMenuLocators:
    """Локаторы для навигационного меню"""

    STICKY_NAV = (By.TAG_NAME, "nav")
    ALL_COURSES_MENU = (By.LINK_TEXT, "All Courses")
    LIFETIME_MEMBERSHIP_SUBMENU = (By.LINK_TEXT, "Lifetime Membership")


class PracticLocators:
    RESOURCES = (By.LINK_TEXT, "Resources")
    PRACTICE_SITE_1 = (By.LINK_TEXT, "Practice Site 1")
    BUTTON = (By.LINK_TEXT, "ENTER TO THE TESTING WEBSITE")
    BUTTON_RESIZABLE = (By.LINK_TEXT, "Resizable")
    PRACTICE_SITE_2 = (By.LINK_TEXT, "Practice Site 2")
    HOME = (By.LINK_TEXT, "Home")
