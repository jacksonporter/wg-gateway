"""Package init for the wg-gateway API."""

import click


@click.group()
def api():
    """Main entry point for the wg-gateway API."""
    # pylint: disable=unnecessary-pass
    pass
