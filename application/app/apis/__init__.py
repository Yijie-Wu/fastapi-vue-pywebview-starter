from fastapi import APIRouter

from app.apis.auth import router as auth_router
from app.apis.user import router as user_router
from app.apis.role import router as role_router
from app.apis.upload import router as upload_router
from app.apis.search import router as search_router
from app.apis.alumnus import router as alumnus_router
from app.apis.message import router as message_router
from app.apis.download import router as download_router
from app.apis.photos import router as photos_router
from app.apis.carousel import router as carousel_router
from app.apis.year import router as year_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=['认证'])
router.include_router(user_router, prefix='/user', tags=['用户'])
router.include_router(role_router, prefix='/role', tags=['角色'])
router.include_router(upload_router, prefix='/upload', tags=['上传'])
router.include_router(search_router, prefix='/search', tags=['搜索'])
router.include_router(alumnus_router, prefix='/alumnus', tags=['校友'])
router.include_router(message_router, prefix='/message', tags=['信息'])
router.include_router(download_router, prefix='/download', tags=['下载'])
router.include_router(photos_router, prefix='/photos', tags=['照片'])
router.include_router(carousel_router, prefix='/carousels', tags=['轮播'])
router.include_router(year_router, prefix='/year', tags=['年份'])
