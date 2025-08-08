import pathlib as Path
import typer
import requests
import json

def download_file(url: str, output_file: Path):
    """
    Generic function to download a file from a URL and save it locally.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        typer.secho(f"✅ File successfully downloaded to {output_file}")
    except Exception as e:
        typer.secho(f"❌ Failed to download the file: {e}", 
                    fg=typer.colors.RED)
        raise typer.Exit(code=1)
    

def ensure_directory_exists(directory: Path):
    """
    Ensure a directory exists; create it if it does not.
    """
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        typer.secho(f"❌ Failed to create directory {directory}: {e}",
                    fg=typer.colors.RED)
        raise

def read_json(file_path: Path) -> dict:
    """
    Read and parse a JSON file.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        typer.secho(f"❌ Failed to read JSON file {file_path}: {e}",
                    fg=typer.colors.RED)
        raise

def write_json(data: dict, file_path: Path):
    """
    Write a dictionary to a JSON file.
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        typer.secho(f"✅ Successfully wrote JSON to {file_path}")
    except Exception as e:
        typer.secho(f"❌ Failed to write JSON file {file_path}: {e}",
                    fg=typer.colors.RED)
        raise