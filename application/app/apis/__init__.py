from fastapi import APIRouter

from app.apis.money import router as money_router

router = APIRouter()

router.include_router(money_router, prefix='/money', tags=['钱币'])

