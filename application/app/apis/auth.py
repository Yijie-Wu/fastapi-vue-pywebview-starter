from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app.models import User
from app.schemas.user import User as UserSchema
from app.utils.token import create_token
from app.cores.user import get_current_user
from app.utils.password import hash_password, verify_password
from app.schemas.auth import BaseLoginSchema
from app.extensions import get_rdbms
from app.settings import load_app_settings

router = APIRouter()
settings = load_app_settings()


@router.post('/login', status_code=200, description='登录')
def login(auth: BaseLoginSchema, db: Session = Depends(get_rdbms)):
    user = db.query(User).filter_by(username=auth.username.strip()).first()
    if user is None:
        user = db.query(User).filter_by(email=auth.nt.strip()).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名/密码错误",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not verify_password(user.password_hash, auth.password.strip()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名/密码错误",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user.last_login = datetime.now()
    user.last_login_by = 'basic'
    db.commit()

    return {'token': create_token(data={'username': user.username})}
