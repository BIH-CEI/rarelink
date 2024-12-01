# src/rarelink/cli/framework/redcap_project_setup.py
import typer

app = typer.Typer()

@app.command()
def start():
    """
    Start the REDCap Project Setup process.
    """
    typer.echo("🚀 Welcome to the REDCap Project Setup!")
    
    typer.secho(
        "👉 For more information on REDCap, visit our documentation",
        fg=typer.colors.BRIGHT_GREEN,
        bold=True,
    )
    typer.echo("📖 Documentation: https://rarelink.readthedocs.io/en/latest/1_background/1_6_redcap.html")

    # Provide guidance
    typer.secho(
        "To create a REDCap project, please follow these steps:", fg=typer.colors.BLUE, bold=True
    )
    typer.echo("0. Check if your instituion hase a REDCap instance - if not read\
        above documentation.")
    typer.echo("1. Contact your local REDCap administrator to create your REDCap\
        project")
    typer.echo("2. Name your REDCap project, e.g.: 'RareLink - NameofyourInstitution'")
    typer.echo("3. Once the project is created, ask your local REDCap administrator\
                to add your institutional accound and provide you API access for\
                    the project.")
    typer.echo("4. Follow the instructions given to you by your REDCap \
        administator to further set up your project.")
    typer.secho("👉 Important: Be aware that there are development and \
        production mode. Read the docs and discuss with your REDCap admin for \
            more info!", fg=typer.colors.RED, bold=True)
    typer.echo("5. Copy the API token for the project and keep it secure.")

    # Reference documentation
    typer.secho(
        "👉 For detailed instructions, visit our documentation:",
        fg=typer.colors.YELLOW,
        bold=True,
    )
    typer.echo("📖 Documentation: https://rarelink.readthedocs.io/en/latest/3_installation/3_0_install_file.html")
