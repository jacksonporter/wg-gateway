"""
CLI entrypoint for the CLI
"""

import click

from wg_gateway.cli.db.bootstrap import bootstrap


def get_db_group(*args, **kwargs) -> click.Command | click.Group:
    """
    Run on application start/starts application
    """

    @click.group()
    def db() -> None:
        """
        Work with the wg-gateway database
        """
        pass

    db.add_command(bootstrap)

    return db
