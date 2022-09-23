from datetime import datetime
from . import Base

from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    String,
)

class Search_Result(Base):
    """A class contains all the information of a search result."""
    __tablename__ = 'search_result'
    sample_type     = Column('sample_type', String, default='N/A')
    lab_id          = Column('lab_id', String, default='N/A')
    box_id          = Column('box_id', String, default='N/A')
    position        = Column('position', String, default='N/A')
    pathwest_id     = Column('pathwest_id', String, default='N/A')
    id              = Column('id', String, primary_key=True, default='N/A')
    cell_type       = Column('cell_type', String, default='N/A')
    sample_date     = Column('sample_date', Date, default=datetime.strptime('01-01-1900', '%d-%M-%Y'))
    visit_number    = Column('visit_number', Integer, default=-9999)
    batch_number    = Column('batch_number', Integer, default=-9999)
    passage_number  = Column('passage_number', Integer, default=-9999)
    cell_count      = Column('cell_count', Integer, default=-9999)
    growth_media    = Column('growth_media', String, default='N/A')
    vial_source     = Column('vial_source', String, default='N/A')
    lot_number      = Column('lot_number', String, default='N/A')
    volume_ml       = Column('volumn', Float, default=0.0)
    patient_code    = Column('patient_code', String, default='N/A')
    user_id        = Column('user_id', String, default='N/A')
    notes           = Column('notes', String, default='N/A')