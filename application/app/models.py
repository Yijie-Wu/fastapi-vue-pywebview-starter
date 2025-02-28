from datetime import datetime

from sqlalchemy.orm import relationship, Session
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Text

from app.extensions import Base
from app.settings import Settings

settings = Settings()


class Roles(Base):
    __tablename__ = 'roles'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column(String(60), unique=True)
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)
    users = relationship('User', back_populates='role')


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    username = Column('username', String(254), default='')
    password_hash = Column('password_hash', String(200), default='')
    avatar = Column('avatar', String(200), default='avatar.png')
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)
    role_id = Column('role_id', Integer, ForeignKey('roles.id'))
    role = relationship('Roles', back_populates='users')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)

    def init_role(self, db: Session):
        if self.role is None:
            if self.username.lower() == settings.APP.ADMIN_USERNAME.lower():
                self.role = db.query(Roles).filter_by(name='超级管理员').first()
            else:
                self.role = db.query(Roles).filter_by(name='普通用户').first()
            db.commit()


class Alumnus(Base):
    __tablename__ = 'alumnus'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    # 校友ID
    alumnus_id = Column('alumnus_id', String(30))
    # 姓名
    alumnus_name = Column('alumnus_name', String(50))
    # 性别
    alumnus_gender = Column('alumnus_gender', String(1))
    # 出生日期 1990-01-01
    birthday = Column('birthday', String(10))
    # 国籍
    nationality = Column('nationality', String(20))
    # 籍贯
    native_place = Column('native_place', String(100))
    # 民族
    nation = Column('nation', String(10))
    # 政治面貌
    politics_status = Column('politics_status', String(10))
    # 通讯地址
    address = Column('address', String(100))
    # 入学年份
    enrollment_year = Column('enrollment_year', String(5))
    # 毕业年份
    graduation_year = Column('graduation_year', String(5))
    # 学号
    student_number = Column('student_number', String(30))
    # 院系
    department = Column('department', String(30))
    # 专业
    major = Column('major', String(30))
    # 班级
    class_name = Column('class_name', String(30))
    # 学校名称
    school_name = Column('school_name', String(30))
    # 证件照
    photo = Column('photo', String(100))
    # 个人简介
    description = Column('description', Text, default='')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)


class Year(Base):
    __tablename__ = 'year'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    year_name = Column('year_name', String(10))
    old_photos = relationship('OldPhotos', back_populates='year')


class OldPhotos(Base):
    __tablename__ = 'old_photos'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    original_name = Column('original_name', String(200))
    store_name = Column('store_name', String(100))
    year_id = Column('year_id', Integer, ForeignKey('year.id'))
    year = relationship('Year', back_populates='old_photos')


class Carousel(Base):
    __tablename__ = 'carousel'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    store_name = Column('store_name', String(100))
    desc = Column('desc', String(100))
    show = Column('show', Boolean, default=False)
