"""
Package init for working with DBs on the CLI
"""

from typing import Any


def parse_db_options(db_options: tuple | None) -> dict[str, Any]:
    """
    Takes a list of options and converts to a dict
    """
    options = {}

    if db_options:
        for value in db_options:
            k, v = value.split("=")
            options[k] = v

    return options
