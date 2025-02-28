import json

from sqlalchemy.orm import Session

from app.models import Alumnus
from app.schemas.alumnus import CreateAlumnus, UpdateAlumnus
from app.responses import ResponseException


def getAllAlumnus(skip: int, limit: int, db: Session):
    data = db.query(Alumnus).offset(skip).limit(limit).all()
    count = db.query(Alumnus).count()

    return {"data": data, "total": count}


def getAllShowAlumnus(db: Session):
    data = db.query(Alumnus).all()

    return data


def createAlumnus(alumnus: CreateAlumnus, db: Session):
    item = db.query(Alumnus).filter_by(alumnus_id=alumnus.alumnus_id.strip()).first()
    if item:
        return ResponseException.HTTP_400_BAD_REQUEST

    alumnus_dict = alumnus.dict()
    alumnus_db = Alumnus(**alumnus_dict)
    db.add(alumnus_db)
    db.commit()
    db.refresh(alumnus_db)

    return alumnus_db


def updateAlumnus(id: int, alumnus: UpdateAlumnus, db: Session):
    item = db.query(Alumnus).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    item.alumnus_id = alumnus.alumnus_id  # 校友ID
    item.alumnus_name = alumnus.alumnus_name  # 姓名
    item.alumnus_gender = alumnus.alumnus_gender  # 性别
    item.birthday = alumnus.birthday  # 出生日期
    item.nationality = alumnus.nationality  # 国籍
    item.native_place = alumnus.native_place  # 籍贯
    item.nation = alumnus.nation  # 民族
    item.politics_status = alumnus.politics_status  # 政治面貌
    item.address = alumnus.address  # 政治面貌
    item.enrollment_year = alumnus.enrollment_year  # 入学年份
    item.graduation_year = alumnus.graduation_year  # 毕业年份
    item.student_number = alumnus.student_number  # 学号
    item.department = alumnus.department  # 院系
    item.major = alumnus.major  # 专业
    item.class_name = alumnus.class_name  # 班级
    item.school_name = alumnus.school_name  # 学校
    item.photo = alumnus.photo  # 证件照
    item.description = alumnus.description  # 个人介绍

    db.commit()
    db.refresh(item)

    return item


def deleteAlumnus(id: int, db: Session):
    item = db.query(Alumnus).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    db.delete(item)
    db.commit()

    return {'detail': '删除成功'}
