

import os

from joblib import Memory

from lint_analysis.bin_counts.models import BinCount


cache_dir = os.path.join(os.path.dirname(__file__), 'cache')
memory = Memory(cache_dir)


token_counts = memory.cache(BinCount.token_counts)
token_series = memory.cache(BinCount.token_series)
pos_series = memory.cache(BinCount.pos_series)
