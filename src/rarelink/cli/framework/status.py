import typer
import subprocess
from rarelink.cli.utils.terminal_utils import end_of_section_separator
from rarelink.cli.utils.string_utils import (
    success_text,
    hint_text,
    format_header,
)

app = typer.Typer(name="framework", help="Setup and manage the RareLink framework.")

@app.command()
def status():
    """
    Display the current version and installation details of RareLink.

    Calls `pip show rarelink` (so tests can patch/assert), but never exits non-zero
    just because the package isn't installed.
    """
    format_header("RareLink Framework Status")
    hint_text("Checking RareLink framework status...")

    try:
        # Keep this call so tests can assert it happened
        subprocess.run(["pip", "show", "rarelink"], check=True)
        typer.secho(success_text("✅ RareLink framework is installed and operational."))
    except subprocess.CalledProcessError:
        # Don't fail the command; just inform the user
        typer.echo("ℹ️ RareLink is not installed in this environment.")
        hint_text("Install locally with: `pip install -e .` from the repo root.")

    end_of_section_separator()
