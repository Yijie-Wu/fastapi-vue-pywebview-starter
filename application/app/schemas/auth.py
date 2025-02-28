from pydantic import BaseModel


class BaseLoginSchema(BaseModel):
    username: str
    password: str

