from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.schemas.search import SearchSchema
from app.cores.search import searchAlumnus

router = APIRouter()
settings = load_app_settings()


@router.post('/alumnus/all', status_code=200, description='搜索校友')
def search_alumnus(
        data: SearchSchema,
        db: Session = Depends(get_rdbms)

):
    return searchAlumnus(data, db)
