from .db import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# from actions import

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme)):
    pass
