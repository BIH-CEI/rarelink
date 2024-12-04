# src/rarelink/cli/framework/redcap_project_setup.py
import typer

app = typer.Typer()

@app.command()
def start():
    """
    Start the REDCap Project Setup process.
    """
    typer.echo("🚀 Welcome to the REDCap Project Setup!")
    
    typer.secho("=" * 120, fg=typer.colors.BRIGHT_BLACK) 
    
    typer.secho(
        "👉 For more information on REDCap, visit our documentation:",
        fg=typer.colors.CYAN,
        bold=True,
    )
    typer.echo("📖 Documentation: https://rarelink.readthedocs.io/en/latest/1_background/1_6_redcap.html")
    
    typer.secho("-" * 120, fg=typer.colors.BRIGHT_BLACK) 

    # Provide guidance
    typer.secho(
        "To create a REDCap project, please follow these steps:", fg=typer.colors.GREEN, bold=True
    )
    typer.echo("0. Check if your instituion hase a REDCap instance - if not read above documentation.")
    typer.echo("1. Contact your local REDCap administrator to create your REDCap project.")
    typer.echo("2. Name your REDCap project, e.g.: 'RareLink - NameofyourInstitution'.")
    typer.echo("3. Let your institutional account be added and provide you API access for the project.")
    typer.echo("4. Follow the instructions given to you by your REDCap administator to further set up your project.")
    typer.secho("👉 Be aware of development and production mode. Read the docs and discuss this with your REDCap admin!", fg=typer.colors.RED)
    typer.echo("5. Copy the API token for the project and keep it secure.")
    typer.echo("6. Run 'rarelink redcap-api-setup start' to set up the REDCap API access.")

    typer.secho("-" * 120, fg=typer.colors.BRIGHT_BLACK) 
        
    # Reference documentation
    typer.secho(
        "👉 For detailed instructions, visit our documentation:",
        fg=typer.colors.CYAN,
        bold=True,
    )
   # typer.echo("📖 Documentation: https://rarelink.readthedocs.io/en/latest/3_installation/3_1_setup_redcap_project.html")
