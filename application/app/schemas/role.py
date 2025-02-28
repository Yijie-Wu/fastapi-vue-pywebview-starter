from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app.settings import load_app_settings

router = APIRouter()
settings = load_app_settings()