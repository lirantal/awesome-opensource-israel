#!/usr/bin/env python3
"""
Check that the "*" lists are ordered in alphabetical order.
Assumptions:
- Each item spans a single line - no two lines or more per item.
- Lists starting with "-" should not be ordered, only "*" lists.
"""
ZPAD = 3
ORDERED_LIST_PREFIX = "* "


def check_lists_in_file(filename: str) -> None:
    previous_item: str | None = None

    with open(filename) as fp:
        for i, line in enumerate(fp):
            if line.startswith(ORDERED_LIST_PREFIX):
                current_item = line
                if (previous_item is not None) and (
                    previous_item.lower() >= current_item.lower()
                ):
                    raise ValueError(
                        f"The alphabetical order is violated at line {i + 1} in the "
                        f"file {filename}:\n"
                        f"L{str(i).zfill(ZPAD)}: {previous_item.strip()}\n"
                        f"L{str(i + 1).zfill(ZPAD)}: {current_item.strip()}\n"
                        "Please reorder the list alphabetically and avoid duplicates."
                    )
                previous_item = current_item
            else:
                previous_item = None


if __name__ == "__main__":
    import sys

    if len(sys.argv) <= 1:
        raise ValueError("Missing input files(s)")

    for filename in sys.argv[1:]:
        check_lists_in_file(filename)
