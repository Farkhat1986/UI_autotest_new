import allure

from locators.main_page_locator import MainPageLocators


@allure.epic("Навигация")
@allure.feature("Меню и Lifetime Membership")
class TestNavigation:
    @allure.story("Меню остаётся видимым при прокрутке")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sticky_navigation_on_scroll(self, main_page):
        """Проверка отображения меню при скроллинге"""
        main_page.open()

        self.locator = MainPageLocators()

        with allure.step("Проверить, что навигация видна до прокрутки"):
            assert (
                main_page.is_sticky_nav_visible()
            ), "Sticky навигация не видна до скролла"

        with allure.step(f"Прокрутить до {self.locator.POPULAR_COURSES_SECTION}"):
            main_page.scroll_to_element(self.locator.POPULAR_COURSES_SECTION)

        with allure.step("Проверить, что навигация видна после прокрутки"):
            assert (
                main_page.is_sticky_nav_visible()
            ), "Sticky навигация не видна после скролла"

    @allure.story("Переход на страницу Lifetime Membership через меню All Courses")
    @allure.severity(allure.severity_level.CRITICAL)
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
