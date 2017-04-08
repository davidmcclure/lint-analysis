

import os

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL


# Database file path.
db_path = os.path.join(os.path.dirname(__file__), 'bin-counts.db')

# Connection URL.
url = URL(drivername='sqlite', database=db_path)

engine = create_engine(url)

build_session = sessionmaker(bind=engine)

session = scoped_session(build_session())
