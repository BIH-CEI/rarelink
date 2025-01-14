import typer
import subprocess
from rarelink.cli.utils.terminal_utils import end_of_section_separator
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    hint_text,
    format_header,
)

app = typer.Typer(name="framework", help="Setup and manage the \
                                            RareLink framework.")

@app.command()
def version():
    """
    Display only the installed version of RareLink.
    """
    format_header("RareLink Version")
    hint_text("Fetching RareLink version...")
    try:
        # Execute `pip show rarelink` and filter the version line
        result = subprocess.run(
            ["pip", "show", "rarelink"],
            capture_output=True,
            text=True,
            check=True,
        )
        for line in result.stdout.splitlines():
            if line.startswith("Version:"):
                typer.secho(success_text(line))
                break
    except subprocess.CalledProcessError as e:
        typer.secho(error_text("❌ Error fetching RareLink version."))
        typer.secho(error_text(str(e)))
        raise typer.Exit(code=1)

    end_of_section_separator()