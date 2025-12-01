from locators.locators import CursesLocators


class TestNavigation:
    def test_sticky_navigation_on_scroll(self, main_page):
        """Проверка отображения меню при скроллинге"""
        main_page.open()

        assert main_page.is_sticky_nav_visible(), "Sticky навигация не видна до скролла"

        main_page.scroll_to_element(CursesLocators.POPULAR_COURSES_SECTION)

        assert (
            main_page.is_sticky_nav_visible()
        ), "Sticky навигация не видна после скролла"

    def test_navigation_to_lifetime_membership(self, main_page):
        """Проверка перехода по меню навигации"""
        main_page.open()

        main_page.navigate_to_lifetime_membership()

        assert (
            "lifetime-membership-club" in main_page.driver.current_url
        ), f"Неверный URL после перехода: {main_page.driver.current_url}"

        page_title = main_page.driver.title
        assert (
            "LIFETIME MEMBERSHIP CLUB" in page_title.upper()
        ), f"Заголовок не содержит 'LIFETIME MEMBERSHIP CLUB': {page_title}"
