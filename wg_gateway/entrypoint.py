#!/usr/bin/env -S python3 -u
"""Application entrypoint if invoked as an executable OR via console
scripts."""

from wg_gateway.cli import cli
from wg_gateway.lib.exe import execute_module_as_script


def main(*args, **kwargs) -> None:
    """Main application starting function."""
    cli(*args, **kwargs)


execute_module_as_script(__name__, main)
