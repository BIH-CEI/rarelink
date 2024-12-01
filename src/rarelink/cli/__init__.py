import typer
from rarelink.cli.framework import app as framework_setup

app = typer.Typer()

# Add framework setup commands
app.add_typer(framework_setup, name="framework-setup")

if __name__ == "__main__":
    app()
    
