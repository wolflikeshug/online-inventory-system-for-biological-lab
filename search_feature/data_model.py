from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_dir = "./biological_samples.sqlite"

# create engine
engine = create_engine( "sqlite:///"+database_dir )
# base modle
Base = declarative_base()

# create session
Session = sessionmaker( bind=engine )
session = Session()

# this is simple model that only serves for searching, this can be deleted after the /model/sample.py is done
class Serum (Base):
    __tablename__ = "serum"
    pw_id   = Column(String)
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class VirusIsolation (Base):
    __tablename__ = "virus_isolation"
    pw_id   = Column(String)
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    batch_number = Column(Integer)
    passage_number = Column(String)
    growth_media   = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class VirusCulture (Base):
    __tablename__ = "virus_culture"
    pw_id   = Column(String)
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    batch_number = Column(Integer)
    passage_number = Column(Integer)
    growth_media   = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Plasma (Base):
    __tablename__ = "plasma"
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    visit_number = Column(Integer)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Pbmc (Base):
    __tablename__ = "pbmc"
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    visit_number = Column(Integer)
    volume  = Column(Integer)
    patient_code = Column(String)
    initials = Column(String)
    other   = Column(String)

class CellLine (Base):
    __tablename__ = "cell_line"
    id      = Column(String, primary_key=True)
    type    = Column(String)
    sample_date    = Column(Date)
    passage_number = Column(Integer)
    total_count = Column(Integer)
    growth_media   = Column(String)
    source  = Column(String)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Mosquito (Base):
    __tablename__ = "mosquito"
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    volumn  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Antigen (Base):
    __tablename__ = "antigen"
    pw_id   = Column(String)
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    batch_number = Column(Integer)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class RNA (Base):
    __tablename__ = "rna"
    pw_id   = Column(String)
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    batch_number = Column(Integer)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Peptide (Base):
    __tablename__ = "peptide"
    id      = Column(String, primary_key=True)
    type    = Column(String)
    sample_date    = Column(Date)
    batch_number = Column(Integer)
    source  = Column(String)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Supernatant (Base):
    __tablename__ = "supernatant"
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Other (Base):
    __tablename__ = "other"
    id      = Column(String, primary_key=True)
    sample_date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class RNA (Vial):
    """ORM Model for the RNA table."""
    __tablename__   = "rna"

    id              = Column('id', ForeignKey('vial.id'), primary_key=True, default=generate_uuid)

    pathwest_id     = Column('pathwest_id', String, default='UNKNOWN')
    batch_number    = Column('batch_number', Integer, default=-1)
    lot_number      = Column('lot_number', String, default='UNKNOWN')

    __mapper_args__ = { 
        'polymorphic_identity': 'rna'
    }

class Peptide (Vial):
    """ORM Model for the Peptide table."""
    __tablename__   = "peptide"

    id              = Column('id', ForeignKey('vial.id'), primary_key=True, default=generate_uuid)
    
    cell_type       = Column('cell_type', String, default='-')
    batch_number    = Column('batch_number', Integer, default=-1)
    vial_source     = Column('vial_source', String, default='UNKNOWN')
    lot_number      = Column('lot_number', String, default='UNKNOWN')

    __mapper_args__ = {
        'polymorphic_identity': 'peptide'
    }

class Supernatant (Vial):
    """ORM Model for the Supernatant table."""
    __tablename__   = "supernatant"

    id              = Column('id', ForeignKey('vial.id'), primary_key=True, default=generate_uuid)

    __mapper_args__ = {
        'polymorphic_identity': 'supernatant'
    }

class Other (Vial):
    """ORM Model for the Other table."""
    __tablename__   = "other"

    id              = Column('id', ForeignKey('vial.id'), primary_key=True, default=generate_uuid)
    
    __mapper_args__ = {
        'polymorphic_identity': 'other'
    }


# Sorry  I need to add this into your sample file, for search purposes
class Search_Result(Base):
    """A class contains all the information of a search result."""
    __tablename__   = 'search_result'
    sample_type     = Column('sample_type', String, default='-')
    pathwest_id     = Column('pathwest_id', String, default='-')
    id              = Column('id', String, primary_key=True, default='-')
    cell_type       = Column('cell_type', String, default='-')
    sample_date     = Column('sample_date', Date, default=date(1900, 1, 1))
    vist_number     = Column('vist_number', Integer, default=-1)
    batch_number    = Column('batch_number', Integer, default=-1)
    passage_number  = Column('passage_number', Integer, default=-1)
    cell_count      = Column('cell_count', Integer, default=-1)
    growth_media    = Column('growth_media', String, default='-')
    vial_source     = Column('vial_source', String, default='-')
    lot_number      = Column('lot_number', String, default='-')
    volume_ml       = Column('volumn', Float, default=0.0)
    patient_code    = Column('patient_code', String, default='-')
    initials        = Column('initials', String, default='-')
    other           = Column('other', String, default='-')


# remember to delete all the lines below, this is for testing only
Base.metadata.create_all(engine)
serum1 = Serum(pw_id="Hello" , id="1", sample_date=date(2020, 1, 1), volume=1, initials="testSerum", other="testSerum")
serum2 = Serum(pw_id="good", id="2", sample_date=date(2020, 3, 1), volume=2, initials="jack", other="jack")
serum3 = Serum(pw_id="World", id="3", sample_date=date(2020, 3, 3), volume=2, initials="test", other="jack")
RNA1 = RNA(pw_id="Hello" , id="4", sample_date=date(2020, 3, 1), batch_number=5, volume=2, lot_number="testRNA", initials="testRNA", other="testRNA")
session.add(serum1)
session.add(serum2)
session.add(serum3)
session.add(RNA1)
session.commit()
