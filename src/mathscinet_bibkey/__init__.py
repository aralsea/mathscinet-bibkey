from pathlib import Path

import click

from mathscinet_bibkey.lib import create_converted_file


@click.command()
@click.argument("path", type=click.Path(exists=True))
def main(path: click.Path) -> None:
    path = Path(path)
    create_converted_file(bibtex_file_path=path)
