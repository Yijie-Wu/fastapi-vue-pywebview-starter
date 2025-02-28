from pydantic import BaseModel


class User(BaseModel):
    id: int
    role: str
    avatar: str
    username: str


class UserProfile(BaseModel):
    user_id: int
    username: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str


class ChangeAvatar(BaseModel):
    avatar: str


class UserAdd(BaseModel):
    username: str
    role_id: int


class UserEdit(BaseModel):
    avatar: str
    username: str
    role_id: int
