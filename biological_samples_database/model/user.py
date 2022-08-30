"""
Model

User model for SqlAlchemy

"""
from sqlalchemy import Column, Integer, String  # , Table
from sqlalchemy.ext.declarative import declared_attr

from . import Base


class User(Base):
    """User class for session authentication and login"""

    __tablename__ = "user"

    id = Column('id', String, primary_key=True)
    username = Column('username', String(20), unique=True, nullable=False)
    first = Column('first', String(20), nullable=False)
    last = Column('last', String(20), nullable=False)
    email = Column('email', String(50), unique=True, nullable=False)
    password = Column('password', String(20), nullable=False)
    gid = Column('gid', Integer, nullable=False)
