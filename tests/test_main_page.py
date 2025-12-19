import allure

from locators.main_page_locator import MainPageLocators


@allure.epic("Главная страница сайта")
@allure.feature("Проверка UI-элементов")
class TestMainPage:

    @allure.story(
        "Проверка видимости основных структурных элементов при загрузке страницы"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_main_page_elements_visibility(self, main_page):
        """Проверка открытия страницы и отображения основных элементов"""
        main_page.open()

        assert (
            main_page.is_header_contact_visible()
        ), "Хедер с контактной информацией не отображается"
        assert main_page.is_navigation_block_visible(), "Блок навигации не отображается"
        assert (
            main_page.is_register_button_visible()
        ), "Кнопка регистрации не отображается"
        assert main_page.is_courses_section_visible(), "Секция курсов не отображается"
        assert main_page.is_footer_visible(), "Футер не отображается"

    @allure.story(
        "Проверка контактной информации в шапке (телефоны, email, Skype, ссылки на соцсети)"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_header_contact_info(self, main_page):
        """Проверка хедера с контактной информацией"""
        main_page.open()

        assert main_page.is_visible(main_page.locators.HEADER_CONTACT)
        assert main_page.is_visible(
            main_page.locators.SKYPE_LINK
        ), "Ссылка на Skype не найдена"
        assert main_page.is_visible(
            main_page.locators.EMAIL_LINK
        ), "Ссылка на email не найдена"

        assert (
            main_page.count_elements(main_page.locators.PHONE_NUMBERS) > 0
        ), "Номера телефонов не найдены"
        assert (
            main_page.count_elements(main_page.locators.SOCIAL_LINKS) == 5
        ), "Ссылки на соцсети не найдены"

    @allure.story("Проверка навигации в слайдере курсов: переключение слайдов работает")
    @allure.severity(allure.severity_level.NORMAL)
    def test_courses_slider_navigation(self, main_page):
        """Проверка кнопок навигации слайдера курсов"""

        main_page.open()
        self.locators = MainPageLocators()

        main_page.scroll_to_element_el(self.locators.POPULAR_COURSES_SECTION)

        initial_slides = main_page.get_active_course_slides()
        assert initial_slides, "Не найдено ни одного слайда"

        with allure.step("Нажать кнопку 'Next' в слайдере курсов"):
            main_page.click_course_slider("next")

        slides_after_next = main_page.get_active_course_slides()
        assert (
            initial_slides != slides_after_next
        ), "Слайды не изменились после клика 'вперед'"

        with allure.step("Нажать кнопку 'Prev' в слайдере курсов"):
            main_page.click_course_slider("prev")

        slides_after_prev = main_page.get_active_course_slides()
        assert (
            initial_slides != slides_after_prev
        ), "Слайды не изменились после клика 'вперед'"

    @allure.story("Проверка кликабельности кнопок слайдера курсов без ошибок")
    @allure.severity(allure.severity_level.MINOR)
    def test_courses_slider_navigation_click_only(self, main_page):
        """Проверка, что кнопки навигации слайдера кликабельны и не вызывают ошибок"""
        main_page.open()
        main_page.scroll_to_element(self.locators.POPULAR_COURSES_SECTION)

        main_page.click_course_slider("next")

        main_page.click_course_slider("prev")

        assert True

    @allure.story("Проверка содержимого футера (адрес, телефоны, email-адреса)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_footer_content(self, main_page):
        """Проверка содержания футера"""
        main_page.open()

        main_page.scroll()

        assert main_page.get_footer_address() != "", "Адрес в футере не отображается"
        assert (
            main_page.get_footer_phones_count()
        ), "Номера телефонов в футере не найдены"
        assert main_page.get_footer_emails_count(), "Email в футере не найдены"
