"""Module to work with executables."""

from typing import Any, Callable


def execute_module_as_script(
    script_name: str, function: Callable, *args, **kwargs
) -> Any:
    """Executes a module as a script/executable."""
    if script_name == "__main__":
        return function(*args, **kwargs)
    return None
