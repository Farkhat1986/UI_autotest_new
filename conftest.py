import allure
import pytest

from utils.driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="chrome или firefox"
    )
    parser.addoption("--remote", action="store_true", help="Запуск через Selenium Grid")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_call", rep)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    remote = request.config.getoption("--remote")

    driver = create_driver(browser=browser, remote=remote)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")

    driver.quit()
