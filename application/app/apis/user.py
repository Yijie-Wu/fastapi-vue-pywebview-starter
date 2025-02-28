import os

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response, FileResponse

from app.models import User
from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.schemas.user import ChangePassword, UserProfile
from app.schemas.user import User as UserSchema, UserAdd, UserEdit, ChangePassword, ChangeAvatar
from app.cores.user import get_current_user, get_users, addNewUser, changePassword, get_admin_user, updateUserProfile, changeAvatar, editUser

router = APIRouter()
settings = load_app_settings()


@router.get('/current_user/info', status_code=200, description='获取当前用户信息')
def current_user_info(user: UserSchema = Depends(get_current_user)):
    return user


@router.get('/avatar/id/{user_id}')
def get_avatar_by_user_id(user_id: int, db: Session = Depends(get_rdbms)):
    user_db = db.query(User).filter_by(id=user_id).first()
    if not user_db:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content='用户不存在')

    file_path = os.path.join(settings.APP.AVATARS_DIR, user_db.avatar)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)


@router.get('/info/id/{user_id}')
def get_user_by_id(user_id: int, db: Session = Depends(get_rdbms)):
    user_db = db.query(User).filter_by(id=user_id).first()
    if not user_db:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content='用户不存在')

    return user_db


@router.get('/avatar/{avatar}')
def get_user_avatar(avatar: str):
    file_path = os.path.join(settings.APP.AVATARS_DIR, avatar)

    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)

    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content='头像不存在')


@router.get('/all')
def get_all_users(users=Depends(get_users)):
    return users


@router.post('/add')
def add_new_user(
        user: UserAdd,
        admin: UserSchema = Depends(get_admin_user),
        db: Session = Depends(get_rdbms)
):
    return addNewUser(user, db)


@router.post('/update/profile')
def update_user_profile(
        user: UserProfile,
        user_schema: UserSchema = Depends(get_current_user),
        db: Session = Depends(get_rdbms)
):
    return updateUserProfile(user, user_schema, db)


@router.post('/change-password')
def change_password(
        cp: ChangePassword,
        user_schema: UserSchema = Depends(get_current_user),
        db: Session = Depends(get_rdbms)
):
    return changePassword(cp, user_schema, db)


@router.post('/change-avatar')
def change_avatar(
        cp: ChangeAvatar,
        user_schema: UserSchema = Depends(get_current_user),
        db: Session = Depends(get_rdbms)
):
    return changeAvatar(cp, user_schema, db)


@router.patch('/update/{id}')
def edit_user(
        id: int,
        cp: UserEdit,
        user_schema: UserSchema = Depends(get_admin_user),
        db: Session = Depends(get_rdbms)
):
    return editUser(id, cp, user_schema, db)


@router.delete('/delete/{id}')
def delete_user(
        id: int,
        user_schema: UserSchema = Depends(get_admin_user),
        db: Session = Depends(get_rdbms)
):
    user_db = db.query(User).filter_by(id=id).first()
    if not user_db:
        raise HTTPException(status_code=400, detail='用户不存在')
    if user_db.username == 'root':
        raise HTTPException(status_code=400, detail='用户root不能删除!')

    db.delete(user_db)
    db.commit()
    return {'detail': '删除成功'}
