"""
Package init
"""

from typing import Callable as _Callable


def init_for_exe_module(module_name: str, exe_func: _Callable) -> None:
    """
    Runs on module import, executes an "executable" function if
    module was invoked as entrypoint
    """
    if module_name == "__main__":
        exe_func()
