import json

from sqlalchemy.orm import Session

from app.models import Carousel
from app.schemas.carousel import CreateCarousels, UpdateCarousels
from app.responses import ResponseException


def getAllCarousels(db: Session):
    data = db.query(Carousel).all()

    return data


def getAllShowCarousel(db: Session):
    data = db.query(Carousel).filter(Carousel.show == True).all()

    return data


def createCarousel(carousel: CreateCarousels, db: Session):
    carousel_dict = carousel.dict()
    carousel_db = Carousel(**carousel_dict)

    db.add(carousel_db)
    db.commit()
    db.refresh(carousel_db)

    return carousel_db


def updateCarousel(id: int, carousel: UpdateCarousels, db: Session):
    item = db.query(Carousel).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    item.store_name = carousel.store_name
    item.desc = carousel.desc
    item.show = carousel.show

    db.commit()
    db.refresh(item)

    return item


def deleteCarousel(id: int, db: Session):
    item = db.query(Carousel).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    db.delete(item)
    db.commit()

    return {'detail': '删除成功'}
