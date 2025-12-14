import json
import os

from selenium.webdriver.remote.webdriver import WebDriver

from config import COOKIES_PAGE_URL

COOKIE_FILE = "cookies.json"


def save_cookies(driver: WebDriver, filename: str = COOKIE_FILE):
    """Сохраняет куки текущей сессии в файл"""
    cookies = driver.get_cookies()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=2)
    print(f"Куки сохранены в {filename}")


def load_cookies(driver: WebDriver, filename: str = COOKIE_FILE):
    """Загружает куки из файла и добавляет их в браузер"""
    if not os.path.exists(filename):
        print(f"Файл куков {filename} не найден, загрузка проаускается")
        return False

    with open(filename, "r", encoding="utf-8") as f:
        cookies = json.load(f)

    driver.get(f"{COOKIES_PAGE_URL}")
    for cookie in cookies:
        if "expiry" in cookie:
            del cookie["expiry"]
        if "sameSite" in cookie:
            del cookie["sameSite"]
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Не удалось добавить куки {cookie.get('name')}: {e}")

    print(f"Куки загружены из {filename}")
    return True
