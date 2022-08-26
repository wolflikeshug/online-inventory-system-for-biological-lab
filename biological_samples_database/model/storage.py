"""
Model

Holds the database ORM structures for SQL Alchemy

"""

import uuid

from sqlalchemy import Column, String  # , Table
from sqlalchemy.orm import backref, relationship

from ..model import Base


class Box(Base):
    """ORM Model for the physical box vials are stored in."""

    __tablename__ = "box"

    id = Column('id', String, primary_key=True, default=uuid.uuid4())

