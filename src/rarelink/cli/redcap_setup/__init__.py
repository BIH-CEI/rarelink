from .download import app as download_app
from .api_config import app as api_config_app
from .start import app as start_app
from .data_dictionary import app as data_dictionary_app
from .template_project import app as template_project_app

import typer

app = typer.Typer()

# REDCap setup commands
app.add_typer(download_app, name="download", help="+ `--help`: Download the\
 current RareLink-CDM data dictionary, instruments, or the REDCap template\
 project.")
app.add_typer(api_config_app, name="api-config", help="+ `--help`: Set up and view the REDCap\
API configuration for your local REDCap project.")
app.command(name="start")(start_app) 
app.add_typer(data_dictionary_app, name="data-dictionary", help="+ `upload`:\
 Upload the most current RareLink-CDM Data Dictionary into an existing REDCap project.")
app.add_typer(template_project_app, name="template-project", help="+ `--help`:\
 Setup the RareLink template project in your local REDCap instance. This\
 is only possible for REDCap administrators.")