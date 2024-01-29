from fastapi import FastAPI
from uvicorn import Config, Server


APP = FastAPI()


@APP.get("/")
async def root():
    return {"message": "Hello World, its me, again!"}


def start_server(
    host: str = "127.0.0.1",
    port: int = 5000,
    log_level: str = "info",
    reload: bool = False,
) -> None:
    """
    Starts uvicorn server with the API
    """
    config = Config(APP, host=host, port=port, log_level=log_level, reload=reload)
    server = Server(config)
    server.run()
