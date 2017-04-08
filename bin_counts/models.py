

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from bin_counts.db import session


Base = declarative_base()

Base.query = session.query_property()


class Bucket(Base):

    __tablename__ = 'bucket'

    __table_args__ = (
        PrimaryKeyConstraint(
            'corpus',
            'year',
            'token',
            'pos',
            'bin',
        ),
    )

    corpus = Column(String, nullable=False)

    year = Column(Integer, nullable=False)

    token = Column(String, nullable=False)

    pos = Column(String, nullable=False)

    offset = Column(Integer, nullable=False)

    bin = Column(Integer, nullable=False)

    @classmethod
    def load(cls):
        pass
