from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_dir = "../biological_samples.sqlite"

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
    pathwest_id   = Column(String)
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class VirusIsolation (Base):
    __tablename__ = "virus_isolation"
    pathwest_id   = Column(String)
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    batch_number = Column(Integer)
    passage_number = Column(String)
    media   = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class VirusCulture (Base):
    __tablename__ = "virus_culture"
    pathwest_id   = Column(String)
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    batch_number = Column(Integer)
    passage_number = Column(Integer)
    media   = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Plasma (Base):
    __tablename__ = "plasma"
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    visit_number = Column(Integer)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Pbmc (Base):
    __tablename__ = "pbmc"
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    visit_number = Column(Integer)
    volume  = Column(Integer)
    patient_code = Column(String)
    initials = Column(String)
    other   = Column(String)

class CellLine (Base):
    __tablename__ = "cell_line"
    id      = Column(String, primary_key=True)
    type    = Column(String)
    date    = Column(Date)
    passage_number = Column(Integer)
    cell_count = Column(Integer)
    media   = Column(String)
    vial_source  = Column(String)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Mosquito (Base):
    __tablename__ = "mosquito"
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    volumn  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Antigen (Base):
    __tablename__ = "antigen"
    pathwest_id   = Column(String)
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    batch_number = Column(Integer)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class RNA (Base):
    __tablename__ = "rna"
    pathwest_id   = Column(String)
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    batch_number = Column(Integer)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Peptide (Base):
    __tablename__ = "peptide"
    id      = Column(String, primary_key=True)
    type    = Column(String)
    date    = Column(Date)
    batch_number = Column(Integer)
    vial_source  = Column(String)
    lot_number = Column(String)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Supernatant (Base):
    __tablename__ = "supernatant"
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)

class Other (Base):
    __tablename__ = "other"
    id      = Column(String, primary_key=True)
    date    = Column(Date)
    volume  = Column(Integer)
    initials = Column(String)
    other   = Column(String)
