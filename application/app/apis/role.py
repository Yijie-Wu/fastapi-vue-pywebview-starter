from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app.settings import load_app_settings
from app.cores.user import get_current_user
from app.schemas.user import User as UserSchema
from app.cores.role import get_roles
from app.extensions import get_rdbms

router = APIRouter()
settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有角色')
def roles(
        user: UserSchema = Depends(get_current_user),
        db: Session = Depends(get_rdbms)

):
    roles = get_roles(db)

    return roles
