from pathlib import Path

import click

from readable_bibkey.lib import create_converted_file


@click.command()
@click.argument("bibtex_file_path", type=click.Path(exists=True))
def main(bibtex_file_path: click.Path) -> None:
    """
    This script converts citation keys in a specified BibTeX file to a readable author_YYYY_title format.
    e.g. MR0463157 (= Robin Hartshorne, "Algebraic geometry" in MathSciNet format) -> hartshorne_1977_algebraic_geometry

    It processes the input .bib file and generates a new file in the same directory with the prefix 'converted_', containing the transformed keys while preserving all other bibliographic information.
    e.g. my_file.bib -> my_file.bib converted_my_file.bib
    """
    path = Path(str(bibtex_file_path))
    create_converted_file(bibtex_file_path=path)
