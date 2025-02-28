from pydantic import BaseModel


class AddSettings(BaseModel):
    name: str
    content: str


class UpdateSettings(BaseModel):
    name: str
    content: str
