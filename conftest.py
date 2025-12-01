import pytest

from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    # attachment = driver.get_screenshot_as_png()
    # allure.attach(attachment, name="screenshot", attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage

    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage

    return LoginPage(driver)


@pytest.fixture
def banking_page(driver):
    from pages.banking_page import BankingPage

    return BankingPage(driver)


@pytest.fixture
def resurses_page(driver):
    from pages.resurses_page import ResursesPage

    return ResursesPage(driver)


@pytest.fixture
def site_test_page(driver):
    from pages.site_test_page import SiteTestPage

    return SiteTestPage(driver)


@pytest.fixture
def home_page(driver):
    from pages.home_page import HomePage

    return HomePage(driver)


@pytest.fixture
def practic_page(driver):
    from pages.practic_page import PracticPage

    return PracticPage(driver)
