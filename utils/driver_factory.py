from selenium import webdriver


def create_driver(browser="chrome", remote=False):
    """
    Фабрика WebDriver
    Поддержка локального запуска и Selenium Grid
    """

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")

    else:
        raise ValueError("Browser must be chrome or firefox")

    if remote:
        return webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub", options=options
        )

    if browser == "chrome":
        return webdriver.Chrome(options=options)

    else:
        return webdriver.Firefox(options=options)
