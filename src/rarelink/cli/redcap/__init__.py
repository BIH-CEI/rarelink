from .download_records import app as download_records_app
# from .upload_records import app as upload_records_app
from .fetch_metadata import app as fetch_metadata_app

import typer

app = typer.Typer(help="Tools for interacting with REDCap projects.")

# REDCap tools commands
app.command(name="download-records")(download_records_app)
# app.add_typer(upload_records_app, name="upload-records")
app.command(name="fetch-metadata")(fetch_metadata_app)