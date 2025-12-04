from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для Home Page"""

    HEADER_CONTACT = (By.TAG_NAME, "header")
    PHONE_NUMBERS = (By.TAG_NAME, "span")
    SOCIAL_LINKS = (By.CSS_SELECTOR, ".ast-header-social-1-wrap a")
    SKYPE_LINK = (By.CSS_SELECTOR, "a[href*='skype']")
    EMAIL_LINK = (By.CSS_SELECTOR, "a[href*='mailto']")
    NAVIGATION_BLOCK = (By.TAG_NAME, "nav")
    REGISTER_BUTTON_I = (By.LINK_TEXT, "Register Now")
    COURSES_SECTION = (By.XPATH, "//h1[contains(text(),'Best Selenium')]")
    FOOTER = (By.TAG_NAME, "footer")
    FOOTER_ADDRESS = (By.CLASS_NAME, "elementor-icon-list-text")
    FOOTER_PHONES = (By.TAG_NAME, "span")
    FOOTER_EMAILS = (By.CSS_SELECTOR, "a[href*='mailto']")
    COURSE_SLIDER_NEXT = (By.CSS_SELECTOR, ".elementor-swiper-button-next")
    COURSE_SLIDER_PREV = (By.CSS_SELECTOR, ".elementor-swiper-button-prev")
    COURSE_SLIDES = (
        By.CSS_SELECTOR,
        ".pp-info-box-container .swiper-wrapper > .swiper-slide",
    )
    STICKY_NAV = (By.TAG_NAME, "nav")
    ALL_COURSES_MENU = (By.LINK_TEXT, "All Courses")
    LIFETIME_MEMBERSHIP_SUBMENU = (By.LINK_TEXT, "Lifetime Membership")
    POPULAR_COURSES_SECTION = (
        By.XPATH,
        "//h2[contains(text(), 'Most Popular Software Testing Courses')]",
    )
