from typing import Optional

from pydantic import BaseModel


class AlumnusBase(BaseModel):
    alumnus_id: str  # 校友ID
    alumnus_name: str  # 姓名
    alumnus_gender: str  # 性别
    birthday: str  # 出生日期
    nationality: str  # 国籍
    native_place: str  # 籍贯
    nation: str  # 民族
    politics_status: str  # 政治面貌
    address: str  # 通讯地址
    enrollment_year: str  # 入学年份
    graduation_year: str  # 毕业年份
    student_number: str  # 学号
    department: str  # 院系
    major: str  # 专业
    class_name: str  # 班级
    school_name: str  # 学校名称
    photo: str  # 证件照
    description: Optional[str] = ""


class CreateAlumnus(AlumnusBase):
    pass


class UpdateAlumnus(AlumnusBase):
    pass
