from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.schemas.config import UpdateSchema
from app.cores.config import getSetting, updateSetting

router = APIRouter()
settings = load_app_settings()


@router.get('/setting', status_code=200, description='获取设置')
def get_setting(db: Session = Depends(get_rdbms)):
    return getSetting(db)


@router.put('/setting', status_code=200, description='更新设置')
def update_setting(data: UpdateSchema, db: Session = Depends(get_rdbms)):
    return updateSetting(data, db)


