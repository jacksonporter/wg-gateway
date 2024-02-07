#!/usr/bin/env -S python3 -u
"""Package entrypoint if invoked from `python -m`"""

from wg_gateway.entrypoint import main
from wg_gateway.lib.exe import execute_module_as_script


execute_module_as_script(__name__, main)
