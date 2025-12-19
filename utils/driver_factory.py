from selenium import webdriver

def create_driver(browser="chrome", remote=False):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError("Browser must be 'chrome' or 'firefox'")

    if remote:
        return webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
    else:
        return webdriver.Chrome(options=options) if browser == "chrome" else webdriver.Firefox(options=options)