import allure


@allure.epic("Навигация")
@allure.feature("Меню Resources")
class TestSiteTest:
    @allure.story("Пользователь переходит в Practice Site 2 (AngularJS Banking App)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_resurses(self, site_test_page):
        """Проверка перехода по меню навигации на страницу PRACTICE_SITE_2"""
        site_test_page.open()

        site_test_page.form_test()

        page_title = site_test_page.driver.title
        assert (
            "Protractor and AngularJS practice-sample website"
        ), f"Заголовок не содержит {page_title}"
