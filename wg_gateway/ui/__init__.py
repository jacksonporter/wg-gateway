"""Package init for the wg-gateway UI."""

from typing import Optional

import click
from nicegui import Client, app, ui as nicegui_ui
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
import httpx

unrestricted_page_routes = {"/login"}


@click.group()
def ui():
    """Main entry point for the wg-gateway API."""
    # pylint: disable=unnecessary-pass
    pass


class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get("authenticated", False):
            if (
                request.url.path in Client.page_routes.values()
                and request.url.path not in unrestricted_page_routes
            ):
                app.storage.user["referrer_path"] = (
                    request.url.path
                )  # remember where the user wanted to go
                return RedirectResponse("/login")
        return await call_next(request)


app.add_middleware(AuthMiddleware)


@nicegui_ui.page("/")
def main_page() -> None:
    with nicegui_ui.column().classes("absolute-center items-center"):
        nicegui_ui.label(f'Hello {app.storage.user["username"]}!').classes("text-2xl")
        nicegui_ui.button(
            on_click=lambda: (app.storage.user.clear(), nicegui_ui.open("/login")),
            icon="logout",
        ).props("outline round")


@nicegui_ui.page("/subpage")
def test_page() -> None:
    nicegui_ui.label("This is a sub page.")


@nicegui_ui.page("/login")
def login() -> Optional[RedirectResponse]:
    def try_login() -> (
        None
    ):  # local function to avoid passing username and password as arguments
        async with httpx.AsyncClient() as client:
            await client.post("http://localhost:8000")

        
        if passwords.get(username.value) == password.value:  # this is where I need to talk to the API, and attempt to get a bearer token
            app.storage.user.update({"bearer_token": token})
            nicegui_ui.open(
                app.storage.user.get("referrer_path", "/")
            )  # go back to where the user wanted to go
        else:
            nicegui_ui.notify("Wrong username or password", color="negative")

    if app.storage.user.get("bearer_token"):
        return RedirectResponse("/")
    with nicegui_ui.card().classes("absolute-center"):
        username = nicegui_ui.input("Username").on("keydown.enter", try_login)
        password = nicegui_ui.input(
            "Password", password=True, password_toggle_button=True
        ).on("keydown.enter", try_login)
        nicegui_ui.button("Log in", on_click=try_login)
    return None


@ui.command()
def start():
    """
    Starts the UI
    """
    nicegui_ui.run(storage_secret="THIS_NEEDS_TO_BE_CHANGED", reload=False)
