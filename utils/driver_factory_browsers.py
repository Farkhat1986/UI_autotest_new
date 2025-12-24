from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


class DriverFactory:
    def __init__(self, remote_url: str = "http://localhost:4444"):
        self.remote_url = remote_url

    def create_driver(self, browser: str, remote: bool = False):
        browser = browser.lower()
        if remote:
            return self.create_remote_driver(browser)
        else:
            return self.create_local_driver(browser)

    def create_local_driver(self, browser: str):
        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            options = ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            options = FirefoxOptions()
            return webdriver.Firefox(service=service, options=options)

        elif browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            options = EdgeOptions()
            return webdriver.Edge(service=service, options=options)

        elif browser == "ie":
            service = IEService(IEDriverManager().install())
            options = IEOptions()
            options.ignore_protected_mode_settings = True
            options.ignore_zoom_level = True
            return webdriver.Ie(service=service, options=options)

        else:
            raise ValueError(f"Нерабочий browser: {browser}")

    def create_remote_driver(self, browser: str):
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--headless=new")
        elif browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
        elif browser == "edge":
            options = EdgeOptions()
            options.add_argument("--headless")
        elif browser == "ie":
            options = IEOptions()
        else:
            raise ValueError(f"Нерабочий browser: {browser}")

        return webdriver.Remote(
            command_executor=f"{self.remote_url}/wd/hub",
            options=options
        )