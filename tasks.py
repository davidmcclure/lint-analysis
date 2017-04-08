

from invoke import task

from bin_counts.db import engine
from bin_counts.models import Base


@task
def init_bin_counts_db(ctx):
    """Create the bin-counts database.
    """
    Base.metadata.create_all(engine)
