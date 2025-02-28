import os
import sys
from typing import List
from pathlib import Path

USER_HOME = os.path.expanduser("~")
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
DATA_STORE_DIR = os.path.join(USER_HOME, 'alumnus_data')


class Settings:
    class APP:
        APP_TITLE: str = 'Alumnus'
        APP_VERSION: str = '1.0.0'
        APP_DESCRIPTION: str = '[Alumnus] 校友管理系统.'
        BACKEND_SERVER: str = 'http://127.0.0.1:8000'

        GLOBAL_API_PREFIX: str = ''

        ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 60 * 3650
        JWT_SECRET_KEY: str = 'JWT_SECRET_KEY'
        JWT_ALGORITHM: str = 'HS256'
        ADMIN_USERNAME: str = 'root'
        AVATARS_DIR: str = os.path.join(DATA_STORE_DIR, 'avatars')
        ALUMNUS_AVATARS_DIR: str = os.path.join(DATA_STORE_DIR, 'alumnus-avatars')

    class LOGGING:
        LEVEL: str = 'INFO'
        FORMAT: str = '{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{file}:{function}():{line} -> {message}'
        ENQUEUE: bool = True
        DIAGNOSE: bool = True
        TRACEBACK: bool = True
        LOG_NAME: str = 'alumnus.log'

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
