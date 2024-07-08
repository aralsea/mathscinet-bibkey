from pathlib import Path

import click

from mathscinet_bibkey.lib import create_converted_file


@click.command()
@click.argument("bibtex_file_path", type=click.Path(exists=True))
def main(bibtex_file_path: click.Path) -> None:
    """
    This script converts citation keys in a specified BibTeX file from MathSciNet's MRxxxxxxx format to a more readable authorYYYYtitle format.
    e.g. MR0463157 (= Robin Hartshorne, `Algebraic geometry`) -> hartshorne1977algebraic
    """
    path = Path(bibtex_file_path)
    create_converted_file(bibtex_file_path=path)
