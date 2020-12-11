from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import logger
from . import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# util functions
def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


# crud operations


def get_user(db: Session, user_id: int) -> schemas.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> schemas.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    hashed_password = get_password_hash(user.password)
    userrole = db.query(models.Role).filter(models.Role.title == "User").first()
    user_in_db = models.User(username=user.username, hashed_password=hashed_password, is_active=False, role_id=userrole.id)
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db


def authenticate_user(db: Session, username: str, password: str) -> schemas.User:
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
