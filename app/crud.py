from sqlalchemy.orm import Session
from .models import User
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user(db: Session, user_id: int):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

def get_users(db: Session):
    return db.query(User).all()

def upddate_user(db: Session, user_id: int, name: str):
    user = get_user(db, user_id)

    if user:
        user.name = name
        db.commit()
        db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)

    if user:
        db.delete(user)
        db.commit()

    return user