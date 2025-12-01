from locators.locators import (
    CursesLocators,
    FooterLocators,
    HeaderLocators,
    NavigationLocators,
    NavigationMenuLocators,
)

from .base_page import BasePage


class MainPage(BasePage):

    URL = "https://www.way2automation.com/"

    def open(self):
        self.driver.get(self.URL)
        return self

    def is_header_contact_visible(self):
        return self.is_element_visible(HeaderLocators.HEADER_CONTACT)

    def get_phone_numbers_count(self):
        return len(self.driver.find_elements(*HeaderLocators.PHONE_NUMBERS))

    def get_social_links_count(self):
        return len(self.driver.find_elements(*HeaderLocators.SOCIAL_LINKS))

    def is_skype_link_present(self):
        return self.is_element_present(HeaderLocators.SKYPE_LINK)

    def is_email_link_present(self):
        return self.is_element_present(HeaderLocators.EMAIL_LINK)

    def is_navigation_block_visible(self):
        return self.is_element_visible(NavigationLocators.NAVIGATION_BLOCK)

    def is_register_button_visible(self):
        return self.is_element_visible(NavigationLocators.REGISTER_BUTTON_I)

    def is_courses_section_visible(self):
        return self.is_element_visible(CursesLocators.COURSES_SECTION)

    def is_footer_visible(self):
        return self.is_element_visible(FooterLocators.FOOTER)

    def get_footer_address(self):
        return self.get_text(FooterLocators.FOOTER_ADDRESS)

    def get_footer_phones_count(self):
        return len(self.driver.find_elements(*FooterLocators.FOOTER_PHONES))

    def get_footer_emails_count(self):
        return len(self.driver.find_elements(*FooterLocators.FOOTER_EMAILS))

    def click_course_slider_next(self):
        self.click(CursesLocators.COURSE_SLIDER_NEXT)

    def click_course_slider_prev(self):
        self.click(CursesLocators.COURSE_SLIDER_PREV)

    def get_active_course_slides(self):
        slides = self.driver.find_elements(*CursesLocators.COURSE_SLIDES)
        if not slides:
            return []
        return [slide.text.strip() for slide in slides]

    def scroll_down(self):
        self.scroll_to_bottom()

    def is_sticky_nav_visible(self):
        return self.is_element_visible(NavigationMenuLocators.STICKY_NAV)

    def navigate_to_lifetime_membership(self):

        all_courses = self.find_element(NavigationMenuLocators.ALL_COURSES_MENU)
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            all_courses,
        )

        self.click(NavigationMenuLocators.LIFETIME_MEMBERSHIP_SUBMENU)
