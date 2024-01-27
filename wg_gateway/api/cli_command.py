"""
CLI entrypoint for the API
"""

import click

from fastapi import FastAPI
from uvicorn import Config, Server


def get_api_app() -> FastAPI:
    """
    Returns the API object to run with an ASGI server
    """
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app


@click.command()
@click.option("-h", "--host", type=str, default="127.0.0.1")
@click.option("-p", "--port", type=int, default=5000)
@click.option("-l", "--log-level", type=str, default="info")
def api(host: str, port: int, log_level: str) -> None:
    """
    Click command to start the API app from the command line
    """
    config = Config(get_api_app(), host=host, port=port, log_level=log_level)
    server = Server(config)
    server.run()
