from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///test.db')
session = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Базовый класс для создания моделей и миграций"""
    pass
