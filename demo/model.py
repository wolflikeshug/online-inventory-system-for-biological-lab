"""
Model

Holds the database ORM structures for SQL Alchemy


Sample Table Shared Column Format

    id = Column('id', String, primary_key=True)  # Needs auto-generation
    pathwest_id = Column('pathwest_id', String)
    sample_id = Column('primary_id', String)
    cell_type = Column('cell_type', String)
    sample_date = Column('sample_date', Date)
    visit_number = Column('visit_number', String)
    batch_number = Column('batch_number', String)
    passage_number = Column('passage_number', Integer)
    cell_count = Column('cell_count', Integer)
    growth_media = Column('growth_media', String)
    vial_source = Column('vial_source', String)
    lot_number = Column('lot_number', String)
    volume_ml = Column('volume_ml', Integer)
    patient_code = Column('patient_code', String)  # FK to User table
    sample_processor = Column('sample_processor', String)  # FK to User table
    notes = Column('notes', String)
"""

from sqlalchemy import Column, Date, Integer, String  # , ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Sample(Base):
    """Base Model for all Sample tables."""
    __abstract__ = True

    id = Column('id', String, primary_key=True)  # TODO - auto-generation
    sample_id = Column('primary_id', String)
    sample_date = Column('sample_date', Date)
    volume_ml = Column('volume_ml', Integer)
    sample_processor = Column('sample_processor', String)  # TODO - FK to User
    notes = Column('notes', String)


class Plasma(Sample):
    """ORM Model for the Plasma table."""
    __tablename__ = 'plasma'

    # Overridden Variables
    sample_date = Column('sample_date', Date, nullable=False)
    sample_id = Column('primary_id', String, nullable=False)

    # New Variables
    visit_number = Column('visit_number', String)
    volume_ml = Column('volume_ml', Integer)
    notes = Column('notes', String)


class CellLine(Sample):
    """ORM Model for the Cell Line table."""
    __tablename__ = 'cell_line'

    cell_type = Column('cell_type', String, nullable=False)
    passage_number = Column('passage_number', Integer)
    cell_count = Column('cell_count', Integer)
    growth_media = Column('growth_media', String)
    vial_source = Column('vial_source', String)
    lot_number = Column('lot_number', String)
