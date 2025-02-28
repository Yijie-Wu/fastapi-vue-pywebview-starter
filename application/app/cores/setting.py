import json

from sqlalchemy.orm import Session

from app.models import Settings
from app.responses import ResponseException


def getSetting(db: Session):
    item = db.query(Settings).filter_by(name='base').first()

    data = json.loads(item.content)
    return data


def updateSetting(db: Session):
    item = db.query(Settings).filter_by(name='base').first()
    if not item:
        raise ResponseException.HTTP_404_NOT_FOUND

    db.commit()

    return {'detail': '更新成功'}

