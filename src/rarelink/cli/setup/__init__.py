import typer
from .redcap_project import app as redcap_project_app
from .data_dictionary import app as data_dictionary_app
from .keys import app as keys_app
from .view import app as view_app
from .reset import app as reset_app

app = typer.Typer()

@app.callback(invoke_without_command=True)
def setup():
    """
    Setup all components of the RareLink framework in your local environment.
    """

app.command(name="redcap-project")(redcap_project_app)
app.command(name="keys")(keys_app)
app.command(name="data-dictionary")(data_dictionary_app)
app.command(name="view")(view_app)
app.command(name="reset")(reset_app)


