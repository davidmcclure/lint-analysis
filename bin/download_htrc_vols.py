

import click
import pandas as pd

from tqdm import tqdm
from htrc_features.utils import download_file
from boltons.iterutils import chunked


@click.command()
@click.argument('df_path', type=click.Path())
@click.argument('out_dir', type=click.Path())
def download(df_path, out_dir):
    """Download HTRC features vols.
    """
    df = pd.read_json(df_path)

    for htids in tqdm(chunked(list(df.htid), 100)):

        try:
            download_file(htids, outdir=out_dir)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    download()
