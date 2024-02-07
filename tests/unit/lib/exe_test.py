# pylint: disable=missing-module-docstring

from unittest.mock import MagicMock
from wg_gateway.lib.exe import execute_module_as_script


def test_execute_module_as_script() -> None:
    """Tests using function to execute a module as an executable script and
    otherwise does nothing if not the executed module."""
    mock = MagicMock(return_value=("3", {"four": "four"}))

    result = execute_module_as_script("__test__", mock, "1", two="two")
    mock.assert_not_called()
    assert result is None

    result = execute_module_as_script("__main__", mock, "1", two="two")
    mock.assert_called_once_with("1", two="two")
    assert result[0] == "3"
    assert result[1] == {"four": "four"}
