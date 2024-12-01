from .install import install
from .update import update
from .status import status
from .reset import reset
from .redcap_api_setup import app as redcap_api_setup_app
from .redcap_project_setup import app as redcap_project_setup_app


import typer
app = typer.Typer()

app.command(name="install")(install)
app.command(name="update")(update)
app.command(name="reset")(reset)
app.command(name="status")(status)
app.add_typer(redcap_api_setup_app, name="redcap-api-setup")
app.add_typer(redcap_project_setup_app, name="redcap-project-setup")

