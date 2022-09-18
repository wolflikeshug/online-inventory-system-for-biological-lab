"""

Vial.

Holds vial sample structures for various sample types

"""

from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    Integer,
    String,
    ForeignKey
)

from . import Base, generate_uuid


class Sample(Base):
    """Sample class from which all other classes reference their data"""

    __tablename__ = "sample"

    id = Column('id', String, primary_key=True, default=generate_uuid)
    lab_id = Column('lab_id', String, unique=True)
    notes = Column('notes', String)


class Vial(Base):
    """Master table holding baseline data for all vials in the database."""
    __tablename__ = 'vial'

    id = Column(
        'id',
        String,
        primary_key=True,
        default=generate_uuid)
    lab_id = Column('lab_id', String, default='UNKNOWN')
    box_id = Column('box_id', ForeignKey('box.id'))
    position = Column('position', String, default='UNKNOWN')
    sample_date = Column(
        'sample_date',
        Date,
        default=datetime.strptime('01-01-1900', '%d-%M-%Y'))
    volume_ml = Column('volume_ml', Float, default=-9999)
    user_id = Column('user_id', String, default='UNKKNOWN')
    notes = Column('notes', String)
    used = Column('used', Boolean, default=False)
    sample_type = Column('sample_type', String)

    __mapper_args__ = {
        'polymorphic_identity': 'vial',
        'polymorphic_on': sample_type
    }


class Antigen(Vial):
    """ORM Model for the Antigen table."""
    __tablename__ = 'antigen'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    # New Variables
    pathwest_id = Column('pathwest_id', String, default='UNKNOWN')
    batch_number = Column('batch_number', Integer, default=-9999)
    passage_number = Column('passage_number', Integer, default=-9999)
    growth_media = Column('growth_media', String, default='UNKNOWN')

    __mapper_args__ = {
        'polymorphic_identity': 'antigen'
    }


class CellLine(Vial):
    """ORM Model for the Cell Line table."""
    __tablename__ = 'cell_line'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)
    cell_type = Column('cell_type', String, default='UNKNOWN', nullable=False)
    passage_number = Column('passage_number', Integer, default=-9999)
    cell_count = Column('cell_count', Integer, default=-9999)
    growth_media = Column('growth_media', String, default='UNKNOWN')
    vial_source = Column('vial_source', String, default='UNKNOWN')
    lot_number = Column('lot_number', String, default='UNKNOWN')

    __mapper_args__ = {
        'polymorphic_identity': 'cell_line'
    }


class Mosquito(Vial):
    """ORM Model for the Mosquito table."""
    __tablename__ = 'mosquito'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    __mapper_args__ = {
        'polymorphic_identity': 'mosquito'
    }


class Pbmc(Vial):
    """ORM Model for the PBMC table."""
    __tablename__ = 'pbmc'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    # New Variables
    visit_number = Column('visit_number', Integer, default=-9999)
    cell_count = Column('cell_count', Integer, default=-9999)
    patient_code = Column('patient_code', String)

    __mapper_args__ = {
        'polymorphic_identity': 'pbmc'
    }


class Plasma(Vial):
    """ORM Model for the Plasma table."""
    __tablename__ = 'plasma'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    # New Variables
    visit_number = Column('visit_number', Integer, default=-9999)

    __mapper_args__ = {
        'polymorphic_identity': 'plasma'
    }


class Serum(Vial):
    """ORM Model for the Serum table."""
    __tablename__ = 'serum'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    # New Variables
    pathwest_id = Column('pathwest_id', String, default='UNKNOWN')

    __mapper_args__ = {
        'polymorphic_identity': 'serum'
    }


class VirusCulture(Vial):
    """ORM Model for the Virus Culture table."""
    __tablename__ = 'virus_culture'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    # New Variables
    pathwest_id = Column('pathwest_id', String, default='UNKNOWN')
    batch_number = Column('batch_number', Integer, default=-9999)
    passage_number = Column('passage_number', Integer, default=-9999)
    growth_media = Column('growth_media', String, default='UNKNOWN')

    __mapper_args__ = {
        'polymorphic_identity': 'virus_culture'
    }


class VirusIsolation(Vial):
    """ORM Model for the Virus Isolation table."""
    __tablename__ = 'virus_isolation'

    id = Column(
        'id',
        ForeignKey('vial.id'),
        primary_key=True,
        default=generate_uuid)

    # New Variables
    pathwest_id = Column('pathwest_id', String, default='UNKNOWN')
    batch_number = Column('batch_number', Integer, default=-9999)
    passage_number = Column('passage_number', Integer, default=-9999)
    growth_media = Column('growth_media', String, default='UNKNOWN')

    __mapper_args__ = {
        'polymorphic_identity': 'virus_isolation'
    }
