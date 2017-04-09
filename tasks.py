

from invoke import task

from bin_counts.db import engine
from bin_counts.models import Base, BinCount


@task
def reset_bin_counts_db(ctx):
    """Recreate the bin counts database.
    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@task
def index_bin_counts_db(ctx):
    """Create indexes on bin counts database.
    """
    BinCount.add_indexes()
