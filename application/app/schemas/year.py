from typing import Optional

from pydantic import BaseModel


class YearBase(BaseModel):
    year_name: str


class CreateYear(YearBase):
    pass


class UpdateYear(YearBase):
    pass


class UpdateYearPhoto(BaseModel):
    original_name: str
