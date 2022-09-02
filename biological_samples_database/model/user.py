"""
Model

User model for SqlAlchemy

"""
from sqlalchemy import Column, Integer, String  # , Table
from flask_login import UserMixin
from biological_samples_database import db, login_man
from enum import Enum
from . import Base
"""User Groups"""
class Group(Enum):

    Admin       = 1
    Staff       = 2
    PhD         = 3
    Student     = 4
    Guest       = 5  
    New         = 6




@login_man.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(Base, db.Model, UserMixin):
    """User class for session authentication and login"""
    __tablename__ = "user"
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(20), unique=True, nullable=False)
    first = Column('first', String(20), nullable=False)
    last = Column('last', String(20), nullable=False)
    email = Column('email', String(50), unique=True, nullable=False)
    password = Column('password', String(20), nullable=False)
    gid = Column('gid', Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.first}', '{self.last}', '{self.username}')"
    
    def group(self):
        return self.gid

    def groupName(self):
        return Group(self.gid).name