from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.settings import load_app_settings
from app.cores.user import get_admin_user
from app.schemas.user import User as UserSchema
from app.schemas.year import CreateYear, UpdateYear, UpdateYearPhoto
from app.cores.year import createYear, deleteYear, getAllYears, updateYear
from app.extensions import get_rdbms
from app.models import OldPhotos, Year
from app.responses import ResponseException

router = APIRouter()
settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有年份')
def years(db: Session = Depends(get_rdbms)):
    return getAllYears(db)


@router.post('/create', status_code=200, description='创建年份')
def create_year(
        year: CreateYear,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return createYear(year, db)


@router.get('/all', status_code=200, description='获取所有年份')
def years(db: Session = Depends(get_rdbms)):
    return getAllYears(db)


@router.delete('/delete/{id}', status_code=200, description='删除年份')
def delete_year(
        id: int,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return deleteYear(id, db)


@router.patch('/update/{id}', status_code=200, description='更新年份')
def update_year(
        id: int,
        year: UpdateYear,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    return updateYear(id, year, db)


@router.patch('/update/photo/{id}', status_code=200, description='更新年份照片信息')
def update_year_photo(
        id: int,
        photo: UpdateYearPhoto,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    item = db.query(OldPhotos).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    item.original_name = photo.original_name
    db.commit()

    year = db.query(Year).filter_by(id=item.year_id).first()

    data = {
        'id': year.id,
        'year_name': year.year_name,
        'old_photos': [
            {
                'id': p.id,
                'original_name': p.original_name,
                'store_name': p.store_name
            } for p in year.old_photos
        ]
    }

    return data


@router.delete('/delete/photo/{id}', status_code=200, description='删除年份照片')
def delete_year_photo(
        id: int,
        db: Session = Depends(get_rdbms),
        user: UserSchema = Depends(get_admin_user)
):
    item = db.query(OldPhotos).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    year = db.query(Year).filter_by(id=item.year_id).first()

    db.delete(item)
    db.commit()


    data = {
        'id': year.id,
        'year_name': year.year_name,
        'old_photos': [
            {
                'id': p.id,
                'original_name': p.original_name,
                'store_name': p.store_name
            } for p in year.old_photos
        ]
    }

    return data
