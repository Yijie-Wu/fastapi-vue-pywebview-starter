from datetime import datetime, timedelta

from jose import jwt

from app.settings import load_app_settings

settings = load_app_settings()


def create_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=settings.APP.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.APP.JWT_SECRET_KEY, algorithm=settings.APP.JWT_ALGORITHM)
    return encoded_jwt


def extract_token(token: str):
    payload = jwt.decode(token, settings.APP.JWT_SECRET_KEY, algorithms=[settings.APP.JWT_ALGORITHM])
    return payload.get("username")
