from fastapi import Depends
from sqlalchemy.orm import Session

from app.models import Alumnus
from app.responses import ResponseException
from app.schemas.search import SearchSchema


def searchAlumnus(data: SearchSchema, db: Session):
    if data.search_by == '姓名':
        db_items = db.query(Alumnus).filter(Alumnus.alumnus_name.ilike(f'%{data.q.strip()}%')).all()
        return db_items

    elif data.search_by == '学号':
        db_items = db.query(Alumnus).filter(Alumnus.student_number.ilike(f'%{data.q.strip()}%')).all()
        return db_items

    else:
        return ResponseException.HTTP_400_BAD_REQUEST
