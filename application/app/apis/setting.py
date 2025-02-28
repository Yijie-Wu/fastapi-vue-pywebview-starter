from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.cores.money import getMoneyPages, deleteMoney

router = APIRouter()
settings = load_app_settings()


@router.get('/setting', status_code=200, description='分页获取所有点钞记录')
def get_setting(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0), db: Session = Depends(get_rdbms)):
    return getMoneyPages(skip, limit, db)


@router.put('/setting', status_code=200, description='删除点钞记录')
def update_setting(id: int, db: Session = Depends(get_rdbms)):
    return deleteMoney(id, db)


