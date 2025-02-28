from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.utils.common import split_list
from app.settings import load_app_settings
from app.schemas.user import User as UserSchema
from app.schemas.carousel import CreateCarousels, UpdateCarousels
from app.cores.carousel import getAllCarousels, createCarousel, updateCarousel, deleteCarousel, getAllShowCarousel
from app.cores.user import get_current_user, get_admin_user

router = APIRouter()
settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有轮播')
def carousels(db: Session = Depends(get_rdbms)):
    return getAllCarousels(db)


@router.get('/all/show', status_code=200, description='获取所有要展示在首页的轮播')
def carousels_show(db: Session = Depends(get_rdbms)):
    items = getAllShowCarousel(db)
    return items


@router.post('/create', status_code=200, description='创建轮播')
def create_carousels(
        carousels: CreateCarousels,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return createCarousel(carousels, db)


@router.patch('/update/{id}', status_code=200, description='更新轮播')
def update_carousels(
        id: int,
        carousels: UpdateCarousels,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return updateCarousel(id, carousels, db)


@router.delete('/delete/{id}', status_code=200, description='删除轮播')
def delete_carousels(
        id: int,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return deleteCarousel(id, db)
