

import ujson

from datetime import datetime as dt

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.schema import Index

from bin_counts.db import session, engine
from bin_counts.utils import scan_paths


Base = declarative_base()

Base.query = session.query_property()


class BinCount(Base):

    __tablename__ = 'bin_count'

    __table_args__ = dict(sqlite_autoincrement=True)

    id = Column(Integer, primary_key=True)

    corpus = Column(String, nullable=False)

    year = Column(Integer, nullable=False)

    token = Column(String, nullable=False)

    pos = Column(String, nullable=False)

    bin = Column(Integer, nullable=False)

    count = Column(Integer, nullable=False)

    @classmethod
    def load(cls, root):
        """Bulk-insert rows from CSVs.
        """
        for path in scan_paths(root, '\.json$'):
            with open(path) as fh:

                segment = [ujson.loads(line) for line in fh]
                session.bulk_insert_mappings(cls, segment)

                session.commit()
                print(dt.now(), path)

    # TODO: Move to base class.
    @classmethod
    def add_index(cls, *cols, **kwargs):
        """Add an index to the table.
        """
        # Make slug from column names.
        col_names = '_'.join([c.name for c in cols])

        # Build the index name.
        name = 'idx_{}_{}'.format(cls.__tablename__, col_names)

        idx = Index(name, *cols, **kwargs)

        # Render the index.
        idx.create(bind=engine)

    @classmethod
    def add_indexes(cls):
        """Add indexes.
        """
        cls.add_index(cls.corpus)
        cls.add_index(cls.year)
        cls.add_index(cls.token)
        cls.add_index(cls.pos)
