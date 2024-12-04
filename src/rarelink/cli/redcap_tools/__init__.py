from .download_records import app as download_records_app
from .upload_records import app as upload_records_app
from .fetch_metadata import app as fetch_metadata_app

import typer

app = typer.Typer()

# REDCap tools commands
app.add_typer(download_records_app, name="download-records")
app.add_typer(upload_records_app, name="upload-records")
app.add_typer(fetch_metadata_app, name="fetch-metadata")