#!/usr/bin/env -S python3 -u
"""
CLI entrypoint for the API
"""

import click

from wg_gateway import init_for_exe_module
from wg_gateway.api.app import start_server


@click.command()
@click.option("-h", "--host", type=str, default="127.0.0.1")
@click.option("-p", "--port", type=int, default=5000)
@click.option("-l", "--log-level", type=str, default="info")
@click.option("-r", "--reload", is_flag=True, show_default=True, default=False)
def api(*args, **kwargs) -> None:
    """
    Click command to start the API app from the command line
    """
    start_server(*args, **kwargs)


init_for_exe_module(__name__, api)
