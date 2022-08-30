"""
Model

User model for SqlAlchemy

"""
from sqlalchemy import Column, Integer, String  # , Table
from flask_login import UserMixin
from biological_samples_database import data, login_man

@login_man.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(data.Model, UserMixin):
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