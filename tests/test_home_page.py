import allure


@allure.epic("Навигация")
@allure.feature("Главное меню")
@allure.story(
    "Пользователь переходит в Practice Site через Resources в Practice Site 2 потом Home"
)
class TestHome:
    @allure.severity(allure.severity_level.NORMAL)
    def test_resurses(self, home_page):
        """Проверка перехода по меню навигации на страницу Home"""
        home_page.open()

        home_page.form_test()

        page_title = home_page.driver.title
        expected_title = "Get Online Selenium Certification Course | Way2Automation"
        assert (
            expected_title in page_title
        ), f"Заголовок не содержит '{expected_title}', фактический заголовок '{page_title}'"
