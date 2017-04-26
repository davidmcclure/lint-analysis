

import ujson
import numpy as np

from datetime import datetime as dt
from collections import OrderedDict

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.schema import Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from lint_analysis.core.utils import scan_paths
from lint_analysis.bin_counts.db import session, engine


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
        print(col_names)

    @classmethod
    def add_indexes(cls):
        """Add indexes.
        """
        cls.add_index(cls.corpus)
        cls.add_index(cls.year)
        cls.add_index(cls.token)
        cls.add_index(cls.pos)

    @classmethod
    def token_counts(cls, min_count=0):
        """Get total (un-bucketed) token counts.

        Args:
            min_count (int)

        Returns: OrderedDict
        """
        query = (
            session
            .query(cls.token, func.sum(cls.count))
            .group_by(cls.token)
            .having(func.sum(cls.count) > min_count)
            .order_by(func.sum(cls.count).desc())
        )

        return OrderedDict(query.all())

    @classmethod
    def token_series(cls, token, corpus=None, year1=None, year2=None):
        """Get an offset -> count series for a word.

        Args:
            token (str)
            corpus (str)
            year1 (int)
            year2 (int)

        Returns: OrderedDict
        """
        query = (
            session
            .query(cls.bin, func.sum(cls.count))
            .filter(cls.token == token)
            .group_by(cls.bin)
            .order_by(cls.bin)
        )

        if corpus:
            query = query.filter(cls.corpus == corpus)

        if year1:
            query = query.filter(cls.year >= year1)

        if year2:
            query = query.filter(cls.year <= year2)

        series = np.zeros(100)

        for offset, count in query:
            series[offset] = count

        return series