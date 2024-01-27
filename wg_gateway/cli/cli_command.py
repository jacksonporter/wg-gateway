"""
CLI entrypoint for the CLI
"""

import click


@click.command()
def cli() -> None:
    """
    CLI entrypoint to start the CLI
    """
    print("I am here!")
