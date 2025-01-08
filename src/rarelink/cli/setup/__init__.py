from .redcap_project import app as redcap_project_app
from .data_dictionary import app as data_dictionary_app
from .api_keys import app as api_keys_app

import typer

app = typer.Typer()


 # , manage API keys, and
 #    ensure your environment is properly set up for RareLink CLI commands.
 
 
@app.callback(invoke_without_command=True)
def setup():
    """
    Setup all components of the RareLink framework in your local environment.
    """
 
app.command(name="redcap-project")(redcap_project_app) 
app.command(name="api-keys")(api_keys_app)
app.command(name="data-dictionary")(data_dictionary_app)
