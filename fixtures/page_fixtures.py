import pytest

from pages.banking_page import BankingPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.practic_page import PracticPage
from pages.resurses_page import ResursesPage
from pages.site_test_page import SiteTestPage


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def banking_page(driver):
    return BankingPage(driver)


@pytest.fixture
def resurses_page(driver):
    return ResursesPage(driver)


@pytest.fixture
def site_test_page(driver):
    return SiteTestPage(driver)


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def practic_page(driver):
    return PracticPage(driver)
