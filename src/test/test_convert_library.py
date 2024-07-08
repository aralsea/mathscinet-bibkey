from pathlib import Path

import pytest
from bibtexparser.library import Library

TEST_TARGET_PATH_STR = ["../input/hartshorne.bib"]


@pytest.mark.parametrize(
    ("path"), [Path(path_str) for path_str in TEST_TARGET_PATH_STR]
)
def test_convert_library(path: Path) -> None:
    library = Library(str(path))
    expected_library = Library(str(path.parent / f"expected_{path.name}"))
    assert library.entries_dict == expected_library.entries_dict
