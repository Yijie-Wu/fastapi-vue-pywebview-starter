from pydantic import BaseModel


class SettingBase(BaseModel):
    alumnus_id: str
    alumnus_name: str
    alumnus_gender: str
    birthday: str
    nationality: str
    native_place: str
    nation: str