"""
Model.

Holds the Base for the model types
"""

import uuid

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def generate_uuid():
    """Create a UUID and return to string for use in SQLite"""
    return str(uuid.uuid4())
