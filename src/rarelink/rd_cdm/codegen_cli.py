import click
from pathlib import Path
from .codegen import scaffold_version_package, _versions_from_schema, update_data_dictionary_csv

@click.group()
def main():
    """Generate `rarelink_cdm/{version}` from installed rd-cdm resources."""

@main.command("generate")
@click.option("--version", required=True, help="target rarelink_cdm version, e.g., v2_0_2")
@click.option("--dest", type=click.Path(file_okay=False, dir_okay=True, path_type=Path), default=Path("src/rarelink_cdm"))
@click.option("--from-version", "from_version", required=False, help="previous rarelink_cdm version to clone, e.g., v2_0_2")
@click.option("--res-dir", type=click.Path(file_okay=False, dir_okay=True, path_type=Path), default=Path("res"))
@click.option("--update-dictionary/--no-update-dictionary", default=True, help="Update & rename the data dictionary CSV")
@click.option("--force/--no-force", default=False, help="Delete the target version folder before copying")
def generate(version, dest, from_version, res_dir, update_dictionary, force):
    res = scaffold_version_package(version, dest, from_version=from_version, force=force)
    click.echo(f"Generated LinkML + Python at: {res['version_dir']}")

    if update_dictionary:
        versions = _versions_from_schema(res["schema_path"])
        src_ver = from_version or "v2_0_2"  # fallback if auto-detected
        csv_path = update_data_dictionary_csv(res_dir, from_version=src_ver, to_version=version, versions=versions)
        click.echo(f"Updated data dictionary: {csv_path}")
