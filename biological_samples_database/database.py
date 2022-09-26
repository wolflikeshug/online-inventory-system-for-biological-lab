"""
Database

Instantiates the connection for the database and sets up
engine.
"""

# Flask Imports
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

db = SQLAlchemy()

IRPD_PATH = './biological_samples.sqlite'
SQLITE_PATH = f"sqlite:///{IRPD_PATH}"

engine = sqlalchemy.create_engine(
    SQLITE_PATH,
    poolclass=NullPool,
    connect_args={'check_same_thread': False}
)

create_new_session = sessionmaker()
create_new_session.configure(bind=engine)
