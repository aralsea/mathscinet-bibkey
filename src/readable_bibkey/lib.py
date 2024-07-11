from pathlib import Path

from bibtexparser.entrypoint import parse_file, write_file
from bibtexparser.library import Library
from bibtexparser.model import Entry


def extract_lowercase_alphabet_num(text: str) -> str:
    return "".join(char.lower() for char in text if char.isalnum())


def get_plain_authors_name(author: str, is_arxiv: bool) -> str:
    names = author.split(" and ")
    if is_arxiv:  # return full name for arxiv papers
        return "_".join(
            [
                extract_lowercase_alphabet_num(text=name)
                for full_name in names
                for name in full_name.split()
            ]
        )
    family_names = [name.split()[0] for name in names]
    plain_family_names = [
        extract_lowercase_alphabet_num(text=name) for name in family_names
    ]
    return "_".join(plain_family_names)


def get_plain_title(title: str) -> str:
    plain_word_list = [
        extract_lowercase_alphabet_num(text=word) for word in title.split()
    ]

    return "_".join(plain_word_list)


def get_new_key(entry: Entry) -> str:
    if "author" not in entry:
        raise ValueError("Author field is missing")
    else:
        author: str = entry["author"]
    if "year" not in entry:
        raise ValueError("Year field is missing")
    else:
        year: str = entry["year"]
    if "title" not in entry:
        raise ValueError("Title field is missing")
    else:
        title = entry["title"]

    match entry.entry_type:
        case "misc":
            prefix = "preprint_"
        case "book":
            prefix = "book_"
        case _:
            prefix = ""

    is_arxiv = (
        entry.entry_type == "misc"
        and "archiveprefix" in entry
        and entry["archiveprefix"] == "arXiv"
    )

    return (
        prefix
        + get_plain_authors_name(author=author, is_arxiv=is_arxiv)
        + "_"
        + year
        + "_"
        + get_plain_title(title=title)
    )


def convert_library(library: Library) -> None:
    for entry in library.entries:
        try:
            entry.key = get_new_key(entry=entry)
        except Exception as error:
            print(f"Skipped {entry.key}: {error}")


def create_converted_file(bibtex_file_path: Path) -> None:
    library = parse_file(path=str(bibtex_file_path))
    convert_library(library=library)
    new_bibtex_file_path = (
        bibtex_file_path.parent / f"converted_{bibtex_file_path.name}"
    )
    write_file(file=str(new_bibtex_file_path), library=library)
    print(f"Created {new_bibtex_file_path}")
