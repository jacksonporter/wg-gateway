"""Package init for the wg-gateway CLI."""

import click

from wg_gateway.api import api
from wg_gateway.ui import ui


@click.group()
def cli():
    """Main entry point for the wg-gateway CLI."""
    click.echo("Welcome to the wg-gateway CLI!")


cli.add_command(api)
cli.add_command(ui)
