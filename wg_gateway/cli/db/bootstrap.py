"""
Module to work with bootstrapping the wg-gateway database
"""

import click

from wg_gateway.cli.db import parse_db_options
from wg_gateway.db import get_and_init_db


@click.command
@click.option("-t", "--database-type", type=str, default="dynamodb")
@click.option("-d", "--database-config", type=str, multiple=True)
def bootstrap(database_type: str, database_config: list[str] | str) -> None:
    """
    CLI command to bootstrap a database from scratch
    """
    database_config = parse_db_options(
        database_config if isinstance(database_config, tuple) else (database_config,)
    )
    database_obj = get_and_init_db(database_type, database_config)
    database_obj.bootstrap()

    print("Ready to bootstrap? Let's go!")
