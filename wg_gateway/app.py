#!/usr/bin/env -S python3 -u
"""
Main application entrypoint module
"""
import click
from click_default_group import DefaultGroup

from wg_gateway import init_for_exe_module
from wg_gateway.api.cli_command import api
from wg_gateway.cli.cli_command import get_cli_group


def main(*args, **kwargs) -> None:
    """
    Run on application start/starts application
    """

    @click.group(cls=DefaultGroup, default="cli", default_if_no_args=True)
    def main_cli_command_group() -> None:
        pass

    main_cli_command_group.add_command(api)
    main_cli_command_group.add_command(get_cli_group())

    main_cli_command_group(*args, **kwargs)


init_for_exe_module(__name__, main)
