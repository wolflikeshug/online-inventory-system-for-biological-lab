"""
Model

Holds the database ORM structures for SQL Alchemy

"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from . import Base, generate_uuid


class Box(Base):
    """ORM Model for the physical box vials are stored in."""

    __tablename__ = "box"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    label = Column('label', String, unique=True, nullable=False)
    box_type = Column(
        'box_type',
        ForeignKey('box_type.id'),
        nullable=False)
    box_obj = relationship('BoxType')
    freezer_id = Column('freezer_id', ForeignKey('freezer.id'), nullable=False)
    freezer = relationship('Freezer')
    # link to shelf/tower: (potentially remove freezer? box must be shelved)
    shelf_id = Column('shelf_id', ForeignKey('shelf.id'), nullable=False)
    owner = Column('owner', String)


class Shelf(Base):
    """ORM Model for the Shelf that boxes are stored in."""

    __tablename__ = "shelf"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, unique=False, nullable=False)
    freezer_id = Column('freezer_id', ForeignKey('freezer.id'), nullable=False)
    boxes = relationship('Box', backref="shelf")


class BoxType(Base):
    """ORM Model to hold information on dimensions of the box types"""

    __tablename__ = "box_type"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, nullable=False, unique=True)
    height = Column("height", Integer)
    width = Column("width", Integer)


class Freezer(Base):
    """ORM Model for the freezer that boxes are stored in."""

    __tablename__ = "freezer"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, unique=True, nullable=False)
    freezer_type = Column(
        'freezer_type',
        ForeignKey('freezer_type.id'),
        nullable=False)
    freezer_obj = relationship('FreezerType')
    room_id = Column('room_id', ForeignKey('room.id'), nullable=False)
    room = relationship('Room')
    shelves = relationship('Shelf', backref='freezer')


class FreezerType(Base):
    """ORM Model to hold information on the design specs of a freezer"""

    __tablename__ = "freezer_type"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    name = Column('name', String, nullable=False, unique=True)
    description = Column("description", String)


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
