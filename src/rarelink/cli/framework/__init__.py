from .install import install
from .update import update
from .status import status
from .reset import reset

import typer
app = typer.Typer()

app.command(name="install")(install)
app.command(name="update")(update)
app.command(name="reset")(reset)
app.command(name="status")(status)

