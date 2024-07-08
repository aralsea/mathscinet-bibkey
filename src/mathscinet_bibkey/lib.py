from pathlib import Path

from bibtexparser.entrypoint import parse_file, write_file
from bibtexparser.library import Library
from bibtexparser.model import Entry

PLAIN_TITLE_MIN_LENGTH = 7


def extract_lowercase_alphabet(text: str) -> str:
    return "".join(char.lower() for char in text if char.isalpha())


def get_plain_authors_name(author: str) -> str:
    names = author.split("and")
    family_names = [name.split(",")[0] for name in names]
    plain_family_names = [
        extract_lowercase_alphabet(text=name) for name in family_names
    ]
    return "".join(plain_family_names)


def get_plain_title(title: str) -> str:
    plain_word_list = [
        extract_lowercase_alphabet(text=word) for word in title.split(" ")
    ]
    plain_title = ""
    for word in plain_word_list:
        plain_title += word
        if len(plain_title) >= PLAIN_TITLE_MIN_LENGTH:
            break
    return plain_title


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

    return get_plain_authors_name(author=author) + year + get_plain_title(title=title)


def convert_library(library: Library) -> None:
    for entry in library.entries:
        if entry.key.startswith("MR") and entry.key[2:].isdigit():
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
