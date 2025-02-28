import os
import sys
from typing import List

USER_HOME = os.path.expanduser("~")
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
DATA_STORE_DIR = os.path.join(USER_HOME, 'money_data')


class Settings:
    class APP:
        APP_TITLE: str = 'Alumnus'
        APP_VERSION: str = '1.0.0'
        APP_DESCRIPTION: str = '[Money] 点钞数据记录.'
        BACKEND_SERVER: str = 'http://127.0.0.1:8000'

        GLOBAL_API_PREFIX: str = ''

    class DB:
        AUTO_FLASH: bool = True
        PREFIX: str = 'sqlite:///' if sys.platform.startswith('win') else 'sqlite:////'
        DATABASE_URL: str = PREFIX + os.path.join(DATA_STORE_DIR, 'data.db')

    class CORS_MIDDLEWARE:
        ALLOW_METHODS: List[str] = ["*"]
        ALLOW_HEADERS: List[str] = ["*"]
        ALLOW_ORIGINS: List[str] = ["*", ""]
        ALLOW_CREDENTIALS: bool = True


def load_app_settings() -> Settings:
    settings = Settings()
    return settings
