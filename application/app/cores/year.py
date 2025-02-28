from sqlalchemy.orm import Session

from app.schemas.year import CreateYear, UpdateYear
from app.models import Year
from app.responses import ResponseException


def createYear(year: CreateYear, db: Session):
    year_dict = year.dict()
    year_db = Year(**year_dict)
    db.add(year_db)
    db.commit()
    db.refresh(year_db)

    return year_db


def getAllYears(db: Session):
    years = db.query(Year).all()

    data = [
        {
            'id': year.id,
            'year_name': year.year_name,
            'old_photos': [
                {
                    'id': p.id,
                    'original_name': p.original_name,
                    'store_name': p.store_name
                } for p in year.old_photos
            ]
        } for year in years
    ]

    return data


def deleteYear(id: int, db: Session):
    item = db.query(Year).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND


    for photo in item.old_photos:
        db.delete(photo)
    
    db.delete(item)
    db.commit()

    return {'detail': '删除成功'}


def updateYear(id: int, year: UpdateYear, db: Session):
    item = db.query(Year).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    item.year_name = year.year_name
    db.commit()

    data = {
        'id': item.id,
        'year_name': item.year_name,
        'old_photos': [
            {
                'id': p.id,
                'original_name': p.original_name,
                'store_name': p.store_name
            } for p in item.old_photos
        ]
    }

    return data
