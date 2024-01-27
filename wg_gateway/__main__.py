#!/usr/bin/env -S python3 -u
"""
Top level code environment (entrypoint to package)
"""
from wg_gateway import init_for_exe_module
from wg_gateway.app import main


init_for_exe_module(__name__, main)
