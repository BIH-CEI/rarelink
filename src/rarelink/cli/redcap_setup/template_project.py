import typer
# import requests
# import json
# from pathlib import Path
from rarelink.cli.utils.string_utils import (
    format_header,
    #error_text,
    #success_text,
    hint_text,
    format_command,
)
# from rarelink.cli.utils.terminal_utils import (
#     confirm_action,
#     end_of_section_separator,
#     between_section_separator,
# )
from rarelink.cli.utils.file_utils import read_json

app = typer.Typer(name="template-project") 

DOCS_TEMPLATE_PROJECT = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"
DOWNLOAD_TEMPLATE_URL = "https://rarelink.readthedocs.io/en/latest/resources/rarelink_template_project.xml"

@app.command()
def info():
    """
    Information on downloading the RareLink template project.
    """
    format_header("RareLink Template Project Information")
    typer.secho(
        "⚠️ The 'template-project' feature is not implemented in the current RareLink version v2.0.0.",
        fg=typer.colors.YELLOW,
    )
    typer.echo(
        hint_text(
            "If you are a REDCap admin, you can download the RareLink template project here:"
        )
    )
    typer.secho(format_command(DOWNLOAD_TEMPLATE_URL), fg=typer.colors.CYAN)
    typer.echo(
        hint_text(
            "For detailed instructions, visit the documentation:"
        )
    )
    typer.secho(format_command(DOCS_TEMPLATE_PROJECT), fg=typer.colors.CYAN)



# def load_config(config_file: Path):
#     """
#     Load REDCap API configuration from the specified config file.
#     """
#     if not config_file.exists():
#         typer.secho(error_text(f"Configuration file not found at {config_file}. Please configure your REDCap API."))
#         raise typer.Exit(code=2)

#     try:
#         config = read_json(config_file)
#         if "api_super_token" not in config or not config["api_super_token"]:
#             typer.secho(error_text("API super token not found in your configuration."))
#             raise typer.Exit(code=2)
#         return config
#     except json.JSONDecodeError:
#         typer.secho(error_text("Configuration file is not valid JSON."))
#         raise typer.Exit(code=2)

# @app.command()
# def upload():
#     """
#     Upload the RareLink REDCap template project XML to the project.
#     """
#     format_header("RareLink Template Project Upload")

#     # Ask if the user has an API super token
#     if not confirm_action(
#         "Do you have an API super token? (Only accessible for REDCap ADMINS!)"
#     ):
#         # Provide instructions for setting up with the administrator
#         typer.secho(hint_text("⚠️ REDCap API Super Token is required for this operation."))
#         typer.echo(f"📖 Documentation for setting up a RareLink project: {DOCS_TEMPLATE_PROJECT}")
#         typer.echo("👉 Please follow the instructions with your local REDCap administrator.")
#         raise typer.Exit(code=2)

#     typer.secho(success_text("API Super Token detected. Proceeding with project creation..."))

#     # Prompt user for the configuration file path
#     config_file = Path(typer.prompt("Enter the path to your REDCap API configuration file"))

#     # Load configuration
#     config = load_config(config_file)

#     # Path to the RareLink project XML file
#     project_xml_path = Path("res/rarelink_v2_0_0_redcap_project.xml")
#     if not project_xml_path.exists():
#         typer.secho(error_text(f"Template XML file not found at {project_xml_path}."))
#         raise typer.Exit(code=2)

#     try:
#         # Read the XML file content
#         with open(project_xml_path, "r") as xml_file:
#             xml_content = xml_file.read()

#         # API fields for uploading the XML
#         fields = {
#             "token": config["api_super_token"],
#             "content": "project_xml",
#             "format": "xml",
#             "data": xml_content,
#         }

#         # Make the API request
#         response = requests.post(config["api_url"], data=fields)
#         between_section_separator()
#         typer.echo(hint_text(f"HTTP Status: {response.status_code}"))
#         typer.echo(response.text)

#         if response.status_code == 200:
#             typer.secho(success_text("RareLink template project uploaded successfully."))
#         else:
#             typer.secho(error_text("Failed to upload the RareLink template project. Check your configuration and API permissions."))
#             raise typer.Exit(code=2)

#     except requests.RequestException as e:
#         typer.secho(error_text(f"Error during API request: {e}"))
#         raise typer.Exit(code=2)

#     end_of_section_separator()
