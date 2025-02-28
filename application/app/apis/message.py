import os

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response, FileResponse

from app.models import User, Alumnus, Year, Carousel, OldPhotos
from app.extensions import get_rdbms
from app.schemas.user import User as UserSchema
from app.settings import load_app_settings
from app.cores.user import get_admin_user
from app.responses import ResponseException

router = APIRouter()
settings = load_app_settings()


@router.get('/admin', status_code=200, description='获取后台首页信息')
def admin_message(user: UserSchema = Depends(get_admin_user), db: Session = Depends(get_rdbms)):
    alumnus_count = db.query(Alumnus).count()
    year_count = db.query(Year).count()
    carousel_count = db.query(Carousel).count()
    photo_count = db.query(OldPhotos).count()
    user_count = db.query(User).filter_by(role_id=2).count()
    admin_count = db.query(User).filter_by(role_id=1).count()

    years = db.query(Year).all()

    years_list = [y.year_name for y in years]
    photo_list = [len(y.old_photos) for y in years]

    return {
        'alumnus_count': alumnus_count, 'admin_count': admin_count, 'photo_count': photo_count,
        'user_count': user_count, 'year_count': year_count, 'carousel_count': carousel_count,
        'years_list': years_list, 'photo_list': photo_list
    }


@router.get('/years-photos', status_code=200, description='获取年份照片信息')
def year_photo_message(db: Session = Depends(get_rdbms)):
    years = db.query(Year).all()

    return [
        {
            'year_id': year.id,
            'year_name': year.year_name,
            'old_photos_count': len(year.old_photos)
        } for year in years
    ]


@router.get('/year_photos/{id}', status_code=200, description='获取年份照片信息')
def year_photo_message(id: int, db: Session = Depends(get_rdbms)):
    year = db.query(Year).filter_by(id=id).first()
    if not year:
        return ResponseException.HTTP_404_NOT_FOUND

    return {
        'year_id': year.id,
        'year_name': year.year_name,
        'old_photos': [
            {
                'id': p.id,
                'original_name': p.original_name,
                'store_name': p.store_name
            } for p in year.old_photos
        ]
    }


@router.get('/photos/search', status_code=200, description='搜索照片信息')
def search(q: str, db: Session = Depends(get_rdbms)):
    photos = db.query(OldPhotos).filter(OldPhotos.original_name.like(f'%{q}%')).all()

    return {
        'old_photos': [
            {
                'id': p.id,
                'original_name': p.original_name,
                'store_name': p.store_name
            } for p in photos
        ]
    }
