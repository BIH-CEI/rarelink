import typer
import subprocess
from rarelink.cli.utils.terminal_utils import end_of_section_separator
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    hint_text,
    format_header,
)

app = typer.Typer()

@app.command()
def status():
    """
    Display the current version and installation details of RareLink.
    """
    format_header("RareLink Framework Status")
    hint_text("Checking RareLink framework status...")
    try:
        # Execute `pip show rarelink`
        subprocess.run(["pip", "show", "rarelink"], check=True)
        typer.secho(success_text("✅ RareLink framework is installed and operational."))
    except subprocess.CalledProcessError as e:
        typer.secho(error_text("❌ Error executing pip show rarelink."))
        typer.secho(error_text(str(e)))
        raise typer.Exit(code=1)

    end_of_section_separator()
