import os

from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter, File, UploadFile, Depends

from app.settings import load_app_settings
from app.utils.common import rename_file
from app.cores.user import get_current_user
from app.schemas.user import User as UserSchema
from app.responses import ResponseException
from app.extensions import get_rdbms
from app.models import User, Year, OldPhotos

settings = load_app_settings()

router = APIRouter()


@router.post('/file', status_code=200, description='上传文件')
async def upload_file(file: UploadFile = File(...)):
    alien_name = rename_file(file.filename)
    file_path = os.path.join(settings.APP.ALUMNUS_AVATARS_DIR, alien_name)
    contents = await file.read()

    with open(file_path, 'wb') as f:
        f.write(contents)

    return {
        'url': f'{settings.APP.BACKEND_SERVER}/download/file/{alien_name}',
        'filename': alien_name,
        'name': file.filename,
        'content_type': file.content_type
    }


@router.post('/user/avatar', status_code=200, description='上传用户头像')
async def upload_user_avatar(file: UploadFile = File(...), db: Session = Depends(get_rdbms)):
    alien_name = rename_file(file.filename)
    file_path = os.path.join(settings.APP.AVATARS_DIR, alien_name)
    contents = await file.read()

    with open(file_path, 'wb') as f:
        f.write(contents)

    return {'avatar': alien_name}


@router.post('/old-photo/{year_id}', status_code=200, description='上传老照片文件')
async def upload_old_photo(year_id: int, file: UploadFile = File(...), db: Session = Depends(get_rdbms)):
    alien_name = rename_file(file.filename)
    file_path = os.path.join(settings.APP.ALUMNUS_AVATARS_DIR, alien_name)
    contents = await file.read()

    with open(file_path, 'wb') as f:
        f.write(contents)

    year = db.query(Year).filter_by(id=year_id).first()
    if not year:
        return ResponseException.HTTP_400_BAD_REQUEST

    new_old_photo = OldPhotos(
        original_name=file.filename,
        store_name=alien_name,
        year_id=year.id
    )
    db.add(new_old_photo)
    db.commit()
    db.refresh(new_old_photo)

    return {
        'url': f'{settings.APP.BACKEND_SERVER}/download/file/{alien_name}',
        'filename': alien_name,
        'name': file.filename,
        'content_type': file.content_type,
        'id': new_old_photo.id
    }
