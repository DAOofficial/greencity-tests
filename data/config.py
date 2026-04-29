import os
from dotenv import load_dotenv

# Завантажуємо змінні з файлу .env, якщо він є
load_dotenv()


class Config:
    # URL сторінки (можна взяти з .env або залишити дефолт)
    BASE_UI_URL = os.getenv("BASE_UI_URL", "https://www.greencity.cx.ua/#/greenCity/events")

    # Налаштування браузера
    BROWSER_LANG = os.getenv("BROWSER_LANG", "en")
    HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() == "true"

    # Тайм-аути
    IMPLICIT_WAIT_TIMEOUT = int(os.getenv("IMPLICIT_WAIT_TIMEOUT", 10))
    EXPLICIT_WAIT_TIMEOUT = int(os.getenv("EXPLICIT_WAIT_TIMEOUT", 20))