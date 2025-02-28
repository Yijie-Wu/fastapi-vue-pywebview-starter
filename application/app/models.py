from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Text

from app.extensions import Base


class Money(Base):
    __tablename__ = 'money'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    description = Column('description', Text, default='')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)


class Settings(Base):
    __tablename__ = 'settings'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(20))
    content = Column('content', Text, default='{}')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)
