"""
CLI entrypoint for the CLI
"""

import click

from wg_gateway.cli.db.cli_command import get_db_group


def get_cli_group(*args, **kwargs) -> click.Command | click.Group:
    """
    Run on application start/starts application
    """

    @click.group()
    def cli() -> None:
        """
        CLI entrypoint to start the CLI group
        """
        pass

    cli.add_command(get_db_group())

    return cli
