"""

Vial.

Holds vial sample structures for various sample types

"""

import uuid

from sqlalchemy import Column, Date, Integer, String, ForeignKey  # , Table
from sqlalchemy.ext.declarative import declared_attr

from ..model import Base


class Sample(Base):
    """Sample class from which all other classes reference their data"""

    __tablename__ = "sample"

    id = Column('id', String, primary_key=True)
    lab_id = Column('lab_id', String, unique=True)
    notes = Column('notes', String)


class Vial(Base):
    """Master table holding baseline data for all vials in the database."""
    __tablename__ = 'vial'

    id = Column(
        'id',
        String,
        default=uuid.uuid4(),
        primary_key=True)
    lab_id = Column('lab_id', String)
    box_id = Column('box_id', ForeignKey('box.id'))
    position = Column('position', String)
    sample_date = Column('sample_date', Date)
    volume_ml = Column('volume_ul', Integer)  # TODO - Confirm microlitres okay
    sample_processor = Column('sample_processor', String)  # TODO - FK to User
    notes = Column('notes', String)

    @declared_attr
    def sample_id(self):
        """Shared declared attribute for SQL Alchemy"""
        return Column('sample_id', ForeignKey('sample.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'vial'
    }


class CellLine(Vial):
    """ORM Model for the Cell Line table."""
    __tablename__ = 'cell_line'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)
    cell_type = Column('cell_type', String, nullable=False)
    passage_number = Column('passage_number', Integer)
    cell_count = Column('cell_count', Integer)
    growth_media = Column('growth_media', String)
    vial_source = Column('vial_source', String)
    lot_number = Column('lot_number', String)

    __mapper_args__ = {
        'polymorphic_identity': 'cell_line'
    }


class Mosquito(Vial):
    """ORM Model for the Mosquito table."""
    __tablename__ = 'mosquito'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)
    lab_id = Column('primary_id', String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'mosquito'
    }


class Pbmc(Vial):
    """ORM Model for the PBMC table."""
    __tablename__ = 'pbmc'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'pbmc'
    }


class Plasma(Vial):
    """ORM Model for the Plasma table."""
    __tablename__ = 'plasma'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)

    # New Variables
    visit_number = Column('visit_number', String)

    __mapper_args__ = {
        'polymorphic_identity': 'plasma'
    }


class Serum(Vial):
    """ORM Model for the Serum table."""
    __tablename__ = 'serum'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'serum'
    }


class VirusCulture(Vial):
    """ORM Model for the Virus Culture table."""
    __tablename__ = 'virus_culture'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)

    # New Variables
    batch_number = Column('batch_number', String)
    passage_number = Column('passage_number', Integer)
    growth_media = Column('growth_media', String)

    __mapper_args__ = {
        'polymorphic_identity': 'virus_culture'
    }


class VirusIsolation(Vial):
    """ORM Model for the Virus Isolation table."""
    __tablename__ = 'virus_isolation'

    id = Column('id', ForeignKey('vial.id'), primary_key=True)

    # New Variables
    batch_number = Column('batch_number', String)
    passage_number = Column('passage_number', Integer, nullable=False)
    growth_media = Column('growth_media', String)

    __mapper_args__ = {
        'polymorphic_identity': 'virus_isolation'
    }
