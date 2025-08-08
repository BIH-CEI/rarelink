import typer
from importlib import metadata as ilm

from rarelink.cli.utils.terminal_utils import end_of_section_separator
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    hint_text,
    format_header,
)

app = typer.Typer(name="framework", help="Setup and manage the RareLink framework.")

@app.command()
def status() -> None:
    """
    Display the current version and installation details of RareLink.
    Never exits with error just because the package isn't installed.
    """
    format_header("RareLink Framework Status")
    hint_text("Checking RareLink framework status...")

    try:
        v = ilm.version("rarelink")
        typer.secho(success_text(f"✅ RareLink is installed: {v}"))
    except ilm.PackageNotFoundError:
        typer.secho(error_text("ℹ️ RareLink is not installed in this environment."))
        hint_text("You can install it with: `pip install -e .` from the repo root.")

    end_of_section_separator()

@app.command(name="version")
def version_cmd() -> None:
    """
    Display only the installed version of RareLink.
    Prints 'unknown' if not installed, but does not error.
    """
    format_header("RareLink Version")
    hint_text("Fetching RareLink version...")

    try:
        v = ilm.version("rarelink")
        typer.secho(success_text(v))
    except ilm.PackageNotFoundError:
        typer.secho(error_text("unknown"))

    end_of_section_separator()