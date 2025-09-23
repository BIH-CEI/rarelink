"""RareLink CLI package init.

Do NOT import subcommand modules at import time to avoid circular imports.
We expose a lazy `app` so `from rarelink.cli import app` keeps working.
"""

from typing import Optional

__all__ = ["app", "get_app"]

_APP: Optional[object] = None


def get_app():
    """Build and return the Typer application lazily."""
    import typer
    from rarelink.cli.utils.string_utils import format_command

    # Import subcommands lazily here (safe now)
    from rarelink.cli.framework import app as framework
    from rarelink.cli.setup import app as redcap_setup_app
    from rarelink.cli.redcap import app as redcap_tools_app
    from rarelink.cli.fhir import app as fhir_app
    from rarelink.cli.phenopackets import app as phenopackets_app

    app = typer.Typer()

    app.add_typer(
        framework,
        name="framework",
        help=f"Configure global settings of the RareLink framework - {format_command('rarelink framework --help')}",
    )
    app.add_typer(
        redcap_setup_app,
        name="setup",
        help=f"Setup the RareLink framework locally - {format_command('rarelink setup --help')}",
    )
    app.add_typer(
        redcap_tools_app,
        name="redcap",
        help=f"Interact with a REDCap project: {format_command('rarelink redcap --help')} for more information.",
    )
    app.add_typer(
        fhir_app,
        name="fhir",
        help=f"Setup, manage, and execute the REDCap-FHIR module: {format_command('rarelink fhir --help')} for more information.",
    )
    app.add_typer(
        phenopackets_app,
        name="phenopackets",
        help=f"Setup, manage, and execute the Phenopackets module: {format_command('rarelink phenopackets --help')} for more information.",
    )

    def _version_callback(value: bool):
        if value:
            from rarelink import __version__
            typer.echo(f"RareLink version {__version__}")
            raise typer.Exit()

    @app.callback()
    def main(
        version: bool = typer.Option(
            None,
            "--version",
            "-V",
            callback=_version_callback,
            is_eager=True,
            help="Show RareLink version and exit.",
        )
    ):
        pass

    return app


def __getattr__(name: str):
    """Provide lazy `app` so `from rarelink.cli import app` works."""
    global _APP
    if name == "app":
        if _APP is None:
            _APP = get_app()
        return _APP
    raise AttributeError(name)


def _show_version_and_exit():
    import typer
    from rarelink import __version__
    typer.echo(f"RareLink version {__version__}")
    raise typer.Exit()