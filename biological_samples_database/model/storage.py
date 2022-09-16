"""
Model

Holds the database ORM structures for SQL Alchemy

"""

from sqlalchemy import Column, ForeignKey, String

from . import Base, generate_uuid


class Box(Base):
    """ORM Model for the physical box vials are stored in."""

    __tablename__ = "box"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    label = Column('label', String, unique=True, nullable=False)
    freezer_id = Column('freezer_id', ForeignKey('freezer.id'), nullable=False)
    owner = Column('owner', String)

class Shelf(Base):
    """ORM Model for the Shelf that boxes are stored in."""

    __tablename__ = "shelf"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, unique=True, nullable=False)
    freezer_id = Column('freezer_id', ForeignKey('freezer.id'), nullable=False)

class Freezer(Base):
    """ORM Model for the freezer that boxes are stored in."""

    __tablename__ = "freezer"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, unique=True, nullable=False)
    room_id = Column('room_id', ForeignKey('room.id'), nullable=False)


class Room(Base):
    """ORM Model for the room that freezer is located in."""

    __tablename__ = "room"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, unique=True, nullable=False)
    building_id = Column(
        'building_id',
        ForeignKey('building.id'),
        nullable=False)


class Building(Base):
    """ORM Model for the building that room is located in."""

    __tablename__ = "building"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, unique=True, nullable=False)
