"""
Model.

Holds the Base for the model types
"""

import uuid

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_uuid():
    """Creates a string formatted UUID suitable for SQLite"""

    return str(uuid.uuid4())
