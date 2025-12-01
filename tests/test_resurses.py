class TestResurses:
    def test_resurses(self, resurses_page):
        """Проверка перехода по меню навигации на страницу PRACTICE_SITE_1"""
        resurses_page.open()

        resurses_page.navigate_to_resurses()

        page_title = resurses_page.driver.title
        assert "Welcome to the Test Site", f"Заголовок не содержит {page_title}"
