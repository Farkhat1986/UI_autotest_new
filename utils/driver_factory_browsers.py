from selenium import webdriver
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


class DriverFactory:
    @staticmethod
    def create_driver(browser: str, remote: bool = False, remote_url: str = "http://localhost:4444"):
        """
        Создаёт WebDriver для указанного браузера

        Args:
            browser (str): 'chrome', 'firefox', 'edge', 'ie'
            remote (bool): использовать Selenium Grid
            remote_url (str): URL Grid (по умолчанию http://localhost:4444)
        """
        browser = browser.lower()

        if remote:
            return DriverFactory.create_remote_driver(browser, remote_url)
        else:
            return DriverFactory.create_local_driver(browser)

    @staticmethod
    def create_local_driver(browser: str):
        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(service=service, options=options)

        elif browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            options = webdriver.EdgeOptions()
            return webdriver.Edge(service=service, options=options)

        elif browser == "ie":
            service = IEService(IEDriverManager().install())
            options = IEOptions()
            options.add_argument("--ignore-protected-mode-settings")
            options.add_argument("--ignore-zoom-level")
            options.add_argument("--disable-features=EnableEphemeralFlashPermission")
            return webdriver.Ie(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def create_remote_driver(browser: str, remote_url: str):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from selenium.webdriver.edge.options import Options as EdgeOptions
        from selenium.webdriver.ie.options import Options as IEOptions

        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        elif browser == "edge":
            options = EdgeOptions()
        elif browser == "ie":
            options = IEOptions()
            options.add_argument("--ignore-protected-mode-settings")
            options.add_argument("--ignore-zoom-level")
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return webdriver.Remote(
            command_executor=f"{remote_url}/wd/hub",
            options=options
        )