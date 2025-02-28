from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.cores.money import getMoneyPages, deleteMoney, deleteAllMoney

router = APIRouter()
settings = load_app_settings()


@router.get('/pages', status_code=200, description='分页获取所有点钞记录')
def alumnus(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0), db: Session = Depends(get_rdbms)):
    return getMoneyPages(skip, limit, db)


@router.delete('/delete/{id}', status_code=200, description='删除点钞记录')
def delete_money(id: int, db: Session = Depends(get_rdbms)):
    return deleteMoney(id, db)


@router.delete('/delete/all', status_code=200, description='删除所有点钞记录')
def delete_money(db: Session = Depends(get_rdbms)):
    return deleteAllMoney(db)
