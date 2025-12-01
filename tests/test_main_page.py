from locators.locators import CursesLocators


class TestMainPage:
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

    def test_header_contact_info(self, main_page):
        """Проверка хедера с контактной информацией"""
        main_page.open()

        assert main_page.get_phone_numbers_count(), "Номера телефонов не найдены"
        assert main_page.is_skype_link_present(), "Ссылка на Skype не найдена"
        assert main_page.is_email_link_present(), "Ссылка на email не найдена"
        assert main_page.get_social_links_count(), "Ссылки на соцсети не найдены"

    def test_courses_slider_navigation(self, main_page):
        """Проверка кнопок навигации слайдера курсов"""
        main_page.open()

        main_page.scroll_to_element_el(CursesLocators.POPULAR_COURSES_SECTION)

        initial_slides = main_page.get_active_course_slides()

        assert initial_slides, "Не найдено ни одного слайда"

        main_page.click_course_slider_next()

        slides_after_next = main_page.get_active_course_slides()

        assert (
            initial_slides != slides_after_next
        ), "Слайды не изменились после клика 'вперед'"

        main_page.click_course_slider_prev()

        slides_after_prev = main_page.get_active_course_slides()

        assert (
            initial_slides != slides_after_prev
        ), "Слайды не изменились после клика 'вперед'"

    def test_courses_slider_navigation_click_only(self, main_page):
        """Проверка, что кнопки навигации слайдера кликабельны и не вызывают ошибок"""
        main_page.open()
        main_page.scroll_to_element(CursesLocators.POPULAR_COURSES_SECTION)

        main_page.click_course_slider_next()

        main_page.click_course_slider_prev()

        assert True

    def test_footer_content(self, main_page):
        """Проверка содержания футера"""
        main_page.open()

        main_page.scroll()

        assert main_page.get_footer_address() != "", "Адрес в футере не отображается"
        assert (
            main_page.get_footer_phones_count()
        ), "Номера телефонов в футере не найдены"
        assert main_page.get_footer_emails_count(), "Email в футере не найдены"
