""" Model Base class for pygameweb.
"""

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata
