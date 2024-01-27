# pylint: disable=missing-module-docstring,missing-function-docstring

from unittest.mock import MagicMock, call

from wg_gateway import init_for_exe_module


def test_init_for_exe_module() -> None:
    module_name = "test"
    exec_func = MagicMock()

    # "not" the executed module
    init_for_exe_module(module_name=module_name, exe_func=exec_func)
    init_for_exe_module(module_name, exec_func)
    exec_func.assert_not_called()

    # "IS" the executed module
    module_name = "__main__"
    exec_func = MagicMock()
    init_for_exe_module(module_name=module_name, exe_func=exec_func)
    init_for_exe_module(module_name, exec_func)
    exec_func.assert_has_calls(
        [
            call(),
            call(),
        ]
    )
