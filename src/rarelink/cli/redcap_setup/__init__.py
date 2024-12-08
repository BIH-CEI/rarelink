from .download import app as download_app
from .api_setup import app as api_setup_app
from .project_setup import app as project_setup_app
from .data_dictionary import app as data_dictionary_app
from .template_project import app as template_project_app

import typer

app = typer.Typer()

# REDCap setup commands
app.add_typer(download_app, name="download")
app.add_typer(api_setup_app, name="api-setup")
app.add_typer(project_setup_app, name="start")
app.add_typer(data_dictionary_app, name="data-dictionary")
app.add_typer(template_project_app, name="template_project")