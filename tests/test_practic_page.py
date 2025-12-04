import allure


@allure.epic("Практические сайты")
@allure.feature("Навигация по виджету Resizable")
class TestPractic:
    @allure.story("Пользователь переходит на страницу Resizable через меню Resources")
    @allure.severity(allure.severity_level.NORMAL)
    def test_practic(self, practic_page):
        """Проверка на странице практики RESIZABLE"""
        practic_page.open()

        practic_page.practic_test()

        page_title = practic_page.driver.title
        assert "Welcom", f"Заголовок не содержит {page_title}"
