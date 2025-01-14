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
def update():
    """
    Updates RareLink and all modules to the latest version.
    """
    format_header("Update RareLink")
    hint_text("🔄Updating RareLink to the latest version...")
    try:
        # Execute `pip install --upgrade rarelink`
        subprocess.run(["pip", "install", "--upgrade", "rarelink"], check=True)
        typer.secho(success_text("✅ RareLink has been successfully updated."))
    except subprocess.CalledProcessError as e:
        typer.secho(error_text("❌ Error updating RareLink."))
        typer.secho(error_text(str(e)))
        raise typer.Exit(code=1)

    hint_text("🔄...updating all RareLink Submodules")
    subprocess.run(["git", "submodule", "update", "--init", "--recursive"], 
                   check=True)
    subprocess.run(["git", "submodule", "update", "--remote", "--merge"], 
                   check=True)
    
    hint_text("🔄...updating all toFHIR Docker Engine")
    subprocess.run(["docker", "pull", "srdc/tofhir-engine:latest"], check=True)
    success_text("✅ ToFHIR engine has been successfully updated.")
    end_of_section_separator()