import json
import os
import logging

from selenium.webdriver.remote.webdriver import WebDriver

from config import COOKIES_PAGE_URL

COOKIE_FILE = "cookies.json"

logger = logging.getLogger(__name__)


def save_cookies(driver: WebDriver, filename: str = COOKIE_FILE):
    """Сохраняет куки текущей сессии в файл"""
    try:
        cookies = driver.get_cookies()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=2, ensure_ascii=False)
        logger.info("Куки сохранены в %s", filename)
    except Exception as e:
        logger.error("Ошибка при сохранении куков в %s: %s", filename, e)
        raise


def clean_cookie(cookie: dict) -> dict:
    """Очищает куки от полей, вызывающих проблемы в Selenium"""

    cleaned_cookie = cookie.copy()

    problematic_fields = ["expiry", "sameSite"]

    for field in problematic_fields:
        cleaned_cookie.pop(field, None)

    return cleaned_cookie


def load_cookies(driver: WebDriver, filename: str = COOKIE_FILE) -> bool:
    """Загружает куки из файла и добавляет их в браузер"""
    if not os.path.exists(filename):
        logger.warning("Файл куков %s не найден, загрузка пропущена", filename)
        return False

    try:
        with open(filename, "r", encoding="utf-8") as f:
            cookies = json.load(f)
    except json.JSONDecodeError as e:
        logger.error("Ошибка формата JSON в файле %s: %s", filename, e)
        return False
    except Exception as e:
        logger.error("Ошибка чтения файла куков %s: %s", filename, e)
        return False

    driver.get(COOKIES_PAGE_URL)

    success_count = 0
    total_count = len(cookies)

    for cookie in cookies:
        cleaned_cookie = clean_cookie(cookie)

        try:
            driver.add_cookie(cleaned_cookie)
            success_count += 1
        except Exception as e:
            logger.warning("Не удалось добавить куку '%s': %s",
                           cookie.get("name", "unknown"), e)

    logger.info("Загружено %d/%d кук(и) из %s",
                success_count, total_count, filename)

    if success_count == 0 and total_count > 0:
        logger.error("Не удалось загрузить ни одну куку из %s", filename)
        return False

    return True