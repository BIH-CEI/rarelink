from .download import app as download_app
from .redcap_api_setup import app as redcap_api_setup_app
from .redcap_project_setup import app as redcap_project_setup_app
from .upload_data_dictionary import app as upload_data_dictionary_app
from .rarelink_template_project import app as rarelink_template_project_app

import typer

app = typer.Typer()

# REDCap setup commands
app.add_typer(download_app, name="download")
app.add_typer(redcap_api_setup_app, name="redcap-api-setup")
app.add_typer(redcap_project_setup_app, name="start")
app.add_typer(upload_data_dictionary_app, name="upload-data-dictionary")
app.add_typer(rarelink_template_project_app, name="rarelink-template-project")