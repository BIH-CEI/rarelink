import click
from pathlib import Path
from .sync import sync_and_generate

@click.group()
def main():
    pass

@main.command("sync-auto")
@click.option("--dest", type=click.Path(file_okay=False, dir_okay=True, path_type=Path), default=Path("rarelink_cdm"))
def sync_auto(dest):
    path = sync_and_generate(dest)
    click.echo(f"Synced and regenerated schema/classes for {path}")