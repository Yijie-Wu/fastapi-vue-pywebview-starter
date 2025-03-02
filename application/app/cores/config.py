import json

from sqlalchemy.orm import Session

from app.models import Config
from app.schemas.config import UpdateSchema
from app.responses import ResponseException


def getSetting(db: Session):
    item = db.query(Config).filter_by(name='base').first()

    data = json.loads(item.content)
    return data


def updateSetting(data: UpdateSchema, db: Session):
    item = db.query(Config).filter_by(name='base').first()
    if not item:
        raise ResponseException.HTTP_404_NOT_FOUND


    newValue = {
        'port': data.port,
        'baudrate': data.baudrate,
        'bytesize': data.bytesize,
        'parity': data.parity,
        'stopbits': data.stopbits,
        'timeout': data.timeout,
        'xonxoff': data.xonxoff,
        'rtscts': data.rtscts,
        'dsrdtr': data.dsrdtr,
    }

    item.content = json.dumps(newValue)
    db.commit()


    return newValue

