from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.settings import load_app_settings

config = load_app_settings()

engine = create_engine(config.DB.DATABASE_URL)

SessionLocal = sessionmaker(autoflush=config.DB.AUTO_FLASH, bind=engine)
Base = declarative_base()


def get_rdbms():
    rdbms = SessionLocal()
    try:
        yield rdbms
    finally:
        rdbms.close()


def get_rdbms_sync():
    rdbms = SessionLocal()
    return rdbms


def generate_tables():
    Base.metadata.create_all(bind=engine)
