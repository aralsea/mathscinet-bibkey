# readable-bibkey

This script converts citation keys in a specified BibTeX file to a readable author_YYYY_title format.

e.g. MR0463157 (= Robin Hartshorne, "Algebraic geometry" in MathSciNet format) -> hartshorne_1977_algebraic_geometry

It processes the input .bib file and generates a new file in the same directory with the prefix 'converted\_', containing the transformed keys while preserving all other bibliographic information.

e.g. my_file.bib -> my_file.bib converted_my_file.bib

Additionally, this script adds a prefix "book\_" (resp. "preprint\_") for @book entries (resp. @misc that have archiveprefix = {arXiv} entries).

## Installation

### via rye (see https://rye.astral.sh/guide/tools/)

```shell
rye install readable-bibkey --git https://github.com/aralsea/readable-bibkey
```

### via pip

```shell
pip install readable-bibkey git+https://github.com/aralsea/readable-bibkey
```

## Usage

```shell
readable-bibkey my_project/my_file.bib
```
