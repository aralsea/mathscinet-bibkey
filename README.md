# mathscinet-bibkey

This script converts citation keys in a specified BibTeX file from MathSciNet's MRxxxxxxx format to a more readable authorYYYYtitle format.

e.g. MR0463157 (= Robin Hartshorne, `Algebraic geometry`) -> hartshorne1977algebraic

It processes the input .bib file and generates a new file in the same directory with the prefix 'converted\_', containing the transformed keys while preserving all other bibliographic information.

e.g. my_file.bib -> my_file.bib converted_my_file.bib

## Installation

### via rye (see https://rye.astral.sh/guide/tools/)

```shell
rye install --git https://github.com/aralsea/mathscinet-bibkey
```

### via pip

```shell
pip install git+https://github.com/aralsea/mathscinet-bibkey
```

## Usage

```shell
mathscinet-bibkey my_project/my_file.bib
```
