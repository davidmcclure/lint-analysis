

from joblib import Memory
import pandas as pd

from lint_analysis.bin_counts.models import BinCount


memory = Memory('cache')


cached_token_counts = memory.cache(BinCount.token_counts)


@memory.cache
def build_variance_df(depth=10000):
    """Compute token -> (count, variance)

    Returns: DataFrame
    """
    tokens = cached_token_counts(depth)

    data = []

    for i, (token, count) in enumerate(tokens.items()):

        series = BinCount.token_series(token)

        data.append((count, series.var()))

        if i % 100 == 0:
            print(i)

    return pd.DataFrame(
        data,
        columns=('count', 'variance'),
        index=tokens.keys()
    )
