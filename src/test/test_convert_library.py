from pathlib import Path

import pytest
from bibtexparser.entrypoint import parse_file
from readable_bibkey.lib import convert_library

TEST_TARGET_PATH_STR = ["src/input/hartshorne.bib", "src/input/evans_lekili.bib"]


@pytest.mark.parametrize(
    ("path"), [Path(path_str) for path_str in TEST_TARGET_PATH_STR]
)
def test_convert_library(path: Path) -> None:
    library = parse_file(path=str(path))
    convert_library(library=library)
    expected_library = parse_file(path=str(path.parent / f"expected_{path.name}"))
    assert [entry.key for entry in library.entries] == [
        entry.key for entry in expected_library.entries
    ]


if __name__ == "__main__":
    for path in TEST_TARGET_PATH_STR:
        test_convert_library(Path(path))
