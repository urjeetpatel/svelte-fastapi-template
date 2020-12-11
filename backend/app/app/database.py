import databases
import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from .config import settings

database = databases.Database(settings.SQLALCHEMY_DATABASE_URI)
engine = sqlalchemy.create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Base: DeclarativeMeta = declarative_base()
