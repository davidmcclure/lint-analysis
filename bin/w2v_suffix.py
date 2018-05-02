

import click

from tqdm import tqdm


@click.command()
@click.argument('src', type=click.File())
@click.argument('dest', type=click.File(mode='w'))
@click.argument('suffix', type=str)
@click.argument('tokens', type=str, nargs=-1)
def main(src, dest, suffix, tokens):
    """Add suffix to tokens in a space-tokenized line corpus.
    """
    tokens = set(tokens)

    for line in tqdm(src):

        suffixed = [
            f'{token}{suffix}' if token in tokens else token
            for token in line.split()
        ]

        print(' '.join(suffixed), file=dest)


if __name__ == '__main__':
    main()
