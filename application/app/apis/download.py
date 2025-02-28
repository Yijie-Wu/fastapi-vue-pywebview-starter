import os

from fastapi.responses import FileResponse
from fastapi import APIRouter, HTTPException, status

from app.settings import load_app_settings

settings = load_app_settings()

router = APIRouter()


@router.get('/{file_type}/{file_name}', status_code=200, description='下载文件')
def download(file_type: str, file_name: str):
    file_path = ''

    if file_type == 'file':
        file_path = os.path.join(settings.APP.ALUMNUS_AVATARS_DIR, file_name)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{file_name} not found",
        )

    else:
        return FileResponse(file_path)


@router.get('/stream/{file_type}/{file_name}/{download_name}', status_code=200, description='download stream file')
def stream_download(file_type: str, file_name: str, download_name: str):
    file_path = ''

    if file_type == 'blog_image':
        file_path = os.path.join(settings.APP.BLOG_IMAGE_DIR, file_name)

    elif file_type == 'blog_video':
        file_path = os.path.join(settings.APP.BLOG_VIDEO_DIR, file_name)

    elif file_type == 'avatar_image':
        file_path = os.path.join(settings.APP.AVATAR_UPLOAD_DIR, file_name)

    elif file_type == 'video':
        file_path = os.path.join(settings.APP.STORE_FILE_DIR, file_name)

    elif file_type == 'music':
        file_path = os.path.join(settings.APP.STORE_MUSIC_DIR, file_name)

    elif file_type == 'app':
        file_path = os.path.join(settings.APP.STORE_APPS_DIR, file_name)

    elif file_type == 'picture':
        file_path = os.path.join(settings.APP.STORE_PICTURES_DIR, file_name)

    elif file_type == 'file':
        file_path = os.path.join(settings.APP.STORE_FILE_DIR, file_name)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{file_name} not found",
        )

    else:
        return FileResponse(file_path, filename=download_name, content_disposition_type='attachment')
