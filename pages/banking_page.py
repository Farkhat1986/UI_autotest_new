from locators.locators import PageLocators

from .base_page import BasePage


class BankingPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login"

    def open(self):
        self.driver.get(self.URL)
        return self

    def navigate_to_sample_form(self):
        self.click(PageLocators.SAMPLE_FORM_TAB)

    def fill_personal_info(self, first_name, last_name, email, password):
        self.send_keys(PageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(PageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(PageLocators.EMAIL_INPUT, email)
        self.send_keys(PageLocators.PASSWORD, password)

    def select_gender_male(self):
        self.click(PageLocators.GENDER_MALE_RADIO)

    def select_hobby_sports(self):
        self.click(PageLocators.HOBBIES_SPORTS_CHECKBOX)

    def get_hobbies_options(self):
        hobbies = []

        hobbies.append(("Sports", len("Sports")))
        hobbies.append(("Reading", len("Reading")))
        hobbies.append(("Traveling", len("Traveling")))

        return hobbies

    def get_longest_hobby_word(self):
        hobbies = self.get_hobbies_options()
        longest_hobby = max(hobbies, key=lambda x: x[1])
        return longest_hobby[0]

    def fill_about_yourself(self, text):
        self.send_keys(PageLocators.ABOUT_TEXTAREA, text)

    def click_register(self):
        self.click(PageLocators.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(PageLocators.SUCCESS_MESSAGE)

    def register_user(self, user_data):
        self.navigate_to_sample_form()
        self.fill_personal_info(
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["password"],
        )
        self.select_gender_male()
        self.select_hobby_sports()

        longest_hobby = self.get_longest_hobby_word()
        about_text = f"{longest_hobby}"
        self.fill_about_yourself(about_text)

        self.click_register()
