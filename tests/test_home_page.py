class TestHome:
    def test_resurses(self, home_page):
        """Проверка перехода по меню навигации на страницу Home"""
        home_page.open()

        home_page.form_test()

        page_title = home_page.driver.title
        assert (
            "Get Online Selenium Certification Course | Way2Automation"
        ), f"Заголовок не содержит {page_title}"
