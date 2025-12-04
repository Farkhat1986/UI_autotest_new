import allure
import pytest

from utils.driver_factory import create_driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Определения статуса теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_call", rep)


@pytest.fixture
def driver(request):
    """Фикстура WebDriver с автоматическим скриншотом при падении"""
    driver = create_driver()
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
