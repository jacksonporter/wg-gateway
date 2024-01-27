#!/usr/bin/env -S python3 -u
"""
Main application entrypoint module
"""
from wg_gateway import init_for_exe_module


def main() -> None:
    """
    Run on application start/starts application
    """
    print("Hello world!")


init_for_exe_module(__name__, main)
