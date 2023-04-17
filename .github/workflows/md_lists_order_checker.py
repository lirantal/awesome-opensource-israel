#!/usr/bin/env python3
"""
Check that the "*" lists are ordered in alphabetical order.
Assumptions:
- Each item spans a single line - no two lines or more per item.
- Lists starting with "-" should not be ordered, only "*" lists.
"""
import re


ZPAD = 3


# returns true if items are ordered or if any of the items is None
def is_ordered_items(previous_item: str | None, current_item: str | None) -> bool:
    if None in [previous_item, current_item]:
        return True
    return current_item.lower() > previous_item.lower()


# returns just the project name,
# i.e. `* [my project name](https://my.project.url) my project description`
# will return `my project name` or None if regex didn't match the above example
def extract_project_name(line: str) -> str | None:
    match = re.search("^\* \[(.*?)\]", line, flags=re.IGNORECASE)
    return match.group(1) if match else None


def check_lists_in_file(filename: str) -> None:
    previous_item: str | None = None

    with open(filename) as fp:
        for idx, line in enumerate(fp, 1):
            current_item = extract_project_name(line)
            if not is_ordered_items(previous_item, current_item):
                raise ValueError(
                    f"The alphabetical order is violated at line {idx} in the "
                    f"file {filename}:\n"
                    f"L{str(idx - 1).zfill(ZPAD)}: {previous_item.strip()}\n"
                    f"L{str(idx).zfill(ZPAD)}: {current_item.strip()}\n"
                    "Please reorder the list alphabetically and avoid duplicates."
                )
            previous_item = current_item


if __name__ == "__main__":
    import sys

    if len(sys.argv) <= 1:
        raise ValueError("Missing input files(s)")

    for filename in sys.argv[1:]:
        check_lists_in_file(filename)
