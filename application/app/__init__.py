import json
import os.path
from fastapi import FastAPI

from app.apis import router
from app.models import Config
from app.middlewares import add_cors_middleware
from app.settings import Settings, load_app_settings, DATA_STORE_DIR
from app.extensions import generate_tables, SessionLocal


def create_app() -> FastAPI:
    settings = load_app_settings()
    app = FastAPI(
        title=settings.APP.APP_TITLE,
        version=settings.APP.APP_VERSION,
        description=settings.APP.APP_DESCRIPTION
    )

    register_router(app, settings)
    init_dirs()
    register_middlewares(app, settings)
    register_databases()

    return app


def register_router(app: FastAPI, sett: Settings):
    app.include_router(router, prefix=sett.APP.GLOBAL_API_PREFIX)


def register_middlewares(app: FastAPI, sett: Settings):
    add_cors_middleware(app, sett)


def init_setting():
    base_settings = {
        'port': '',
        'baudrate': 9600,
        'bytesize': 8,
        'parity': 'N',
        'stopbits': 1,
        'timeout': 1.0,
        'xonxoff': False,
        'rtscts': False,
        'dsrdtr': False
    }

    db = SessionLocal()
    check = db.query(Config).filter_by(name='base').first()
    if not check:
        new_setting = Config(
            name='base',
            content=json.dumps(base_settings),
        )
        db.add(new_setting)
        db.commit()

    db.close()


def register_databases():
    generate_tables()
    init_setting()


def init_dirs():
    if not os.path.exists(DATA_STORE_DIR):
        os.makedirs(DATA_STORE_DIR, exist_ok=True)
