from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.utils.common import split_list
from app.settings import load_app_settings
from app.schemas.user import User as UserSchema
from app.schemas.alumnus import CreateAlumnus, UpdateAlumnus
from app.cores.alumnus import getAllAlumnus, createAlumnus, updateAlumnus, deleteAlumnus, getAllShowAlumnus
from app.cores.user import get_current_user, get_admin_user

router = APIRouter()
settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有校友')
def alumnus(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0), db: Session = Depends(get_rdbms)):
    return getAllAlumnus(skip, limit, db)


@router.get('/all/show', status_code=200, description='获取所有要展示在首页的校友')
def alumnus_show(db: Session = Depends(get_rdbms)):
    items = getAllShowAlumnus(db)
    if items:
        return split_list(items, 6)
    else:
        return []


@router.post('/create', status_code=200, description='创建校友')
def create_alumnus(
        alumnus: CreateAlumnus,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return createAlumnus(alumnus, db)


@router.patch('/update/{id}', status_code=200, description='更新校友')
def update_Alumnus(
        id: int,
        Alumnus: UpdateAlumnus,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return updateAlumnus(id, Alumnus, db)


@router.delete('/delete/{id}', status_code=200, description='删除校友')
def delete_Alumnus(
        id: int,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return deleteAlumnus(id, db)
