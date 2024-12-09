import typer

app = typer.Typer(name="framework-setup", help="Setup and manage the RareLink framework.")

@app.command()
def status():
    """
    Display the current version and installation details of RareLink.
    """
    typer.echo("To check the RareLink framework status, run:")
    typer.secho("    pip show rarelink", fg=typer.colors.CYAN)
    typer.secho("or:", fg=typer.colors.BRIGHT_BLACK)
    typer.secho("    python -m rarelink --version", fg=typer.colors.CYAN)

@app.command()
def update():
    """
    Update RareLink to the latest version.
    """
    typer.echo("To update the RareLink framework, run:")
    typer.secho("    pip install --upgrade rarelink", fg=typer.colors.CYAN)

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
        typer.secho(f"❌ An error occurred during the reset process: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)
