import typer
import subprocess
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator
)
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    hint_text,
    format_header,
)

app = typer.Typer(name="framework", help="Setup and manage the \
                                            RareLink framework.")

@app.command()
def reset():
    """
    Reset RareLink by uninstalling and reinstalling the local package.
    """
    from pathlib import Path

    format_header("Reset RareLink Framework")
    hint_text("Starting reset process...")

    # Start searching for the project root
    current_path = Path(__file__).resolve().parent
    for parent in current_path.parents:
        if (parent / "pyproject.toml").exists():
            project_path = parent
            break
    else:
        typer.secho(
            error_text(
                "❌ Could not find the project directory. Make sure the repository "
                "was cloned correctly and you are running this command from inside it."
            )
        )
        raise typer.Exit(1)

    typer.secho(f"Detected project directory: {hint_text(str(project_path))}")


    try:
        subprocess.run(["pip", "uninstall", "rarelink", "-y"], check=True)
        typer.secho(success_text("✅ RareLink has been uninstalled."))
        between_section_separator()
        subprocess.run(["pip", "install", "-e", str(project_path)], check=True)
        typer.secho(success_text("✅ RareLink has been reinstalled from the local source."))
    except subprocess.CalledProcessError as e:
        typer.secho(error_text(f"❌ An error occurred during the reset process: {e}"))
        raise typer.Exit(1)

    end_of_section_separator()
