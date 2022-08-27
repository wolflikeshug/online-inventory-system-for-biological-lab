"""
Model

Holds the database ORM structures for SQL Alchemy

"""

from sqlalchemy import Column, ForeignKey, String

from . import create_uuid, Base


class Box(Base):
    """ORM Model for the physical box vials are stored in."""

    __tablename__ = "box"

    id = Column('id', String, primary_key=True, default=create_uuid())
    label = Column('label', String, unique=True)
    freezer_id = Column('freezer_id', ForeignKey('freezer.id'))
    owner = Column('owner', String)


class Freezer(Base):
    """ORM Model for the freezer that boxes are stored in."""

    __tablename__ = "freezer"

    id = Column('id', String, primary_key=True, default=create_uuid())
    name = Column('name', String, unique=True)
    building_id = Column('building_id', ForeignKey('building.id'))


class Building(Base):
    """ORM Model for the building that freezer is located in."""

    __tablename__ = "building"

    id = Column('id', String, primary_key=True, default=create_uuid())
    name = Column('name', String, unique=True)
