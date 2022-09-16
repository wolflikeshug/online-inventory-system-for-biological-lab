from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_dir = "biological_samples.sqlite"

# create engine
engine = create_engine( "sqlite:///"+database_dir )
# base modle
Base = declarative_base(engine)

# create session
Session = sessionmaker( bind=engine )
session = Session()

# this is simple model that only serves for searching, this can be deleted after the /model/sample.py is done
class Serum (Base):
    __tablename__ = "serum"
    pw_id   = Column(String)
    id      = Column(String)
    date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class VirusIsolation (Base):
    __tablename__ = "virus_isolation"
    pw_id   = Column(String)
    id      = Column(String)
    date    = Column(Date)
    batch_number = Column(Integer)
    passage_number = Column(String)
    media   = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class VirusCulture (Base):
    _tablename_ = "virus_culture"
    pw_id   = Column(String)
    id      = Column(String)
    date    = Column(Date)
    batch_number = Column(Integer)
    passage_number = Column(Integer)
    media   = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Plasma (Base):
    __tablename__ = "plasma"
    id      = Column(String)
    date    = Column(Date)
    visit_number = Column(Integer)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Pbmc (Base):
    __tablename__ = "pbmc"
    id      = Column(String)
    date    = Column(Date)
    visit_number = Column(Integer)
    volume  = Column(Integer)
    patient_code = Column(String)
    initials = Column(String)
    other   = Column(String)

class CellLine (Base):
    _tablename_ = "cell_line"
    id      = Column(String)
    type    = Column(String)
    date    = Column(Date)
    passage_number = Column(Integer)
    total_count = Column(Integer)
    media   = Column(String)
    source  = Column(String)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Mosquito (Base):
    _tablename_ = "mosquito"
    id      = Column(String)
    date    = Column(Date)
    volumn  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Antigen (Base):
    _tablename_ = "antigen"
    pw_id   = Column(String)
    id      = Column(String)
    date    = Column(Date)
    batch_number = Column(Integer)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class RNA (Base):
    _tablename_ = "rna"
    pw_id   = Column(String)
    id      = Column(String)
    date    = Column(Date)
    batch_number = Column(Integer)
    lot_number = Column(String)
    initials = Column(String)
    other   = Column(String)

class Peptide (Base):
    _tablename_ = "peptide"
    id      = Column(String)
    type    = Column(String)
    date    = Column(Date)
    batch_number = Column(Integer)
    source  = Column(String)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Supernatant (Base):
    _tablename_ = "supernatant"
    id      = Column(String)
    date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Other (Base):
    _tablename_ = "other"
    id      = Column(String)
    date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)