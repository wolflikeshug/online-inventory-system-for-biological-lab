"""
Demo Setup
"""

# Standard Imports
import datetime
import os
import random
import uuid

# Local Imports
from database import create_new_session, engine, SQLITE_PATH
from model import Base, CellLine


def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""

    if not os.path.exists(SQLITE_PATH):
        Base.metadata.create_all(engine)


def create_dummy_data():
    """Insert a single dummy dataset into the SQLite database"""

    cell_line = CellLine()

    cell_line.id = str(uuid.uuid4())
    cell_line.sample_id = f"TEST SAMPLE ID: {random.randint(0, 100)}"
    cell_line.sample_date = datetime.datetime.now()
    cell_line.cell_type = 'UNKNOWN TYPE'

    session = create_new_session()

    session.add(
        cell_line
    )

    session.commit()


if __name__ == '__main__':
    initialise_sqlite_database()
    create_dummy_data()
