import allure


@allure.epic("Навигация")
@allure.feature("Меню Resources")
class TestResurses:
    @allure.story(
        "Пользователь переходит в Practice Site 1 из выпадающего меню Resources"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_resurses(self, resurses_page):
        """Проверка перехода по меню навигации на страницу PRACTICE_SITE_1"""
        resurses_page.open()

        resurses_page.navigate_to_resurses()

        page_title = resurses_page.driver.title
        assert "Welcome to the Test Site Mo INFORMATION", f"Заголовок не содержит {page_title}"
