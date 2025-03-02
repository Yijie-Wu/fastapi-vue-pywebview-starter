from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Text

from app.extensions import Base


class Money(Base):
    __tablename__ = 'money'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    description = Column('description', Text, default='')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)


class Config(Base):
    __tablename__ = 'config'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(20))
    content = Column('content', Text, default='{}')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)





class Result(Base):
    __tablename__ = 'result'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    date = Column('date', String(20))
    time = Column('time', String(20))
    tf_flag = Column('tf_flag', String(20))
    currency_value = Column('currency_value', String(20))
    fsn_count = Column('fsn_count', String(20))
    money_flag = Column('money_flag', String(20))
    ver = Column('ver', String(20))
    undefine = Column('undefine', String(20))
    char_num = Column('char_num', String(20))
    sno = Column('sno', String(200))
    machine_number = Column('machine_number', String(200))
    reserve1 = Column('reserve1', String(200))
    image_data = Column('image_data', Text)
    currency_name = Column('currency_name', String(50))
    create_at = Column('create_at', DateTime, default=datetime.now)