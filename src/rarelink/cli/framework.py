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

app = typer.Typer(name="framework-setup", help="Setup and manage the RareLink framework.")

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


@app.command()
def update():
    """
    Update RareLink to the latest version.
    """
    format_header("Update RareLink")
    hint_text("Updating RareLink to the latest version...")
    try:
        # Execute `pip install --upgrade rarelink`
        subprocess.run(["pip", "install", "--upgrade", "rarelink"], check=True)
        typer.secho(success_text("✅ RareLink has been successfully updated."))
    except subprocess.CalledProcessError as e:
        typer.secho(error_text("❌ Error updating RareLink."))
        typer.secho(error_text(str(e)))
        raise typer.Exit(code=1)

    end_of_section_separator()


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
