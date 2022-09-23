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
