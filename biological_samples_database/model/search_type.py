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
    sample_type     = Column('sample_type', String, default='-')
    pathwest_id     = Column('pathwest_id', String, default='-')
    id              = Column('id', String, primary_key=True, default='-')
    cell_type       = Column('cell_type', String, default='-')
    sample_date     = Column('sample_date', Date, default=datetime.strptime('01-01-1900', '%d-%M-%Y'))
    vist_number     = Column('vist_number', Integer, default=-9999)
    batch_number    = Column('batch_number', Integer, default=-9999)
    passage_number  = Column('passage_number', Integer, default=-9999)
    cell_count      = Column('cell_count', Integer, default=-9999)
    growth_media    = Column('growth_media', String, default='-')
    vial_source     = Column('vial_source', String, default='-')
    lot_number      = Column('lot_number', String, default='-')
    volume_ml       = Column('volumn', Float, default=0.0)
    patient_code    = Column('patient_code', String, default='-')
    user_id        = Column('user_id', String, default='-')
    notes           = Column('notes', String, default='-')