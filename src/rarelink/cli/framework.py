import typer
import subprocess

app = typer.Typer(name="framework-setup", help="Setup and manage the RareLink framework.")

@app.command()
def status():
    """
    Display the current version and installation details of RareLink.
    """
    typer.echo("Checking RareLink framework status...")
    try:
        # Execute `pip show rarelink`
        subprocess.run(["pip", "show", "rarelink"], check=True)
    except subprocess.CalledProcessError as e:
        typer.secho("❌ Error executing pip show rarelink.", fg=typer.colors.RED)
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)

@app.command()
def update():
    """
    Update RareLink to the latest version.
    """
    typer.echo("Updating RareLink to the latest version...")
    try:
        # Execute `pip install --upgrade rarelink`
        subprocess.run(["pip", "install", "--upgrade", "rarelink"], check=True)
        typer.secho("✅ RareLink has been successfully updated.", fg=typer.colors.GREEN)
    except subprocess.CalledProcessError as e:
        typer.secho("❌ Error updating RareLink.", fg=typer.colors.RED)
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)

@app.command()
def version():
    """
    Display only the installed version of RareLink.
    """
    typer.echo("Fetching RareLink version...")
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
                typer.secho(line, fg=typer.colors.GREEN)
                break
    except subprocess.CalledProcessError as e:
        typer.secho("❌ Error fetching RareLink version.", fg=typer.colors.RED)
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)

@app.command()
def reset():
    """
    Reset RareLink by uninstalling and reinstalling the local package.
    """
    import os
    import subprocess
    from pathlib import Path

    typer.echo("Resetting the RareLink framework...")

    # Start searching for the project root
    current_path = Path(__file__).resolve().parent
    for parent in current_path.parents:
        if (parent / "pyproject.toml").exists():
            project_path = parent
            break
    else:
        typer.secho(
            "❌ Could not find the project directory. Make sure the repository "
            "was cloned correctly and you are running this command from inside it.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    typer.echo(f"Detected project directory: {project_path}")

    try:
        subprocess.run(["pip", "uninstall", "rarelink", "-y"], check=True)
        typer.echo("✅ RareLink has been uninstalled.")
        subprocess.run(["pip", "install", "-e", str(project_path)], check=True)
        typer.echo("✅ RareLink has been reinstalled from the local source.")
    except subprocess.CalledProcessError as e:
        typer.secho(f"❌ An error occurred during the reset process: {e}",
                    fg=typer.colors.RED)
        raise typer.Exit(1)
