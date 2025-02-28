from fastapi import Depends
from sqlalchemy.orm import Session

from app.models import Roles


def get_roles(db: Session):
    roles = db.query(Roles).all()
    return [{'id': role.id, 'name': role.name, 'users': role.users} for role in roles]
