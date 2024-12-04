import typer
from rarelink.cli.framework import app as framework_app
from rarelink.cli.redcap_setup import app as redcap_setup_app
from rarelink.cli.redcap_tools import app as redcap_tools_app

app = typer.Typer()

# Add command groups
app.add_typer(framework_app, name="framework-setup")
app.add_typer(redcap_setup_app, name="redcap-setup")
app.add_typer(redcap_tools_app, name="redcap-tools")

if __name__ == "__main__":
    app()