import json
import typer
import os
from pathlib import Path
from rarelink.cli.utils.terminal_utils import (
    between_section_separator,
    end_of_section_separator
)
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    format_command,
    format_header
)
from rarelink.cli.utils.validation_utils import (
    validate_env
)
from rarelink.phenopackets import phenopacket_pipeline
from rarelink_cdm.v2_0_0_dev1.mappings.phenopackets import create_rarelink_phenopacket_mappings

app = typer.Typer()

ENV_PATH = Path(".env")
DEFAULT_INPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads"

@app.command()
def export(
    input_path: Path = None,
    output_dir: Path = None,
    mappings: Path = None
):
    """
    CLI command to export data to a cohort of Phenopackets.

    Args:
        input_path (Path, optional): Path to the input LinkML JSON file.
        output_dir (Path, optional): Directory to save Phenopackets.
        mappings (Path, optional): Path to custom mapping configuration.
    """
    format_header("REDCap to Phenopackets Export")
    
    # Step 1: Validate setup files
    typer.echo("🔄 Validating setup files...")
    typer.echo("🔄 Validating the .env file...")
    try:
        validate_env([
            "BIOPORTAL_API_TOKEN",
            "REDCAP_URL",
            "REDCAP_PROJECT_ID",
            "REDCAP_API_TOKEN",
            "REDCAP_PROJECT_NAME",
            "CREATED_BY"
        ])
        typer.secho(success_text("✅ Everything is set up - let's proceed.")) 
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation of .env file failed: {str(e)}. "
                       f"Please run {format_command('rarelink setup api-keys')} "
                       "to configure the required keys."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    
    between_section_separator()

    # Fetch required environment variables
    project_name = os.getenv("REDCAP_PROJECT_NAME")
    created_by = os.getenv("CREATED_BY")
    if not project_name or not created_by:
        typer.secho(
            error_text("❌ Missing required environment variables: "
                       "REDCAP_PROJECT_NAME or CREATED_BY."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Handle spaces in project name by replacing them with underscores
    sanitized_project_name = project_name.replace(" ", "_")

    # Step 2: Determine input file path
    if input_path is None:
        # Generate dynamic paths based on REDCAP_PROJECT_NAME
        input_file_name = f"{sanitized_project_name}-linkml-records.json"
        input_path = DEFAULT_INPUT_DIR / input_file_name

        typer.echo(f"📂 Default input file location: {input_path}")
        is_correct_path = typer.confirm("Is this the correct input file path?")
        if not is_correct_path:
            custom_input_path = typer.prompt(
                "Enter the path to the validated linkml-json file",
                type=Path
            )
            input_path = custom_input_path

    if not input_path.exists():
        typer.secho(
            error_text(f"❌ Input file not found: {input_path}. "
                       "Ensure the records have been validated using "
                       f"{format_command('rarelink redcap download records')}."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    
    between_section_separator()

    # Step 3: Determine output directory
    if output_dir is None:
        output_dir_name = f"{sanitized_project_name}_phenopackets"
        output_dir = DEFAULT_OUTPUT_DIR / output_dir_name

        typer.echo(f"📂 Default output directory: {output_dir}")
        is_correct_output_dir = typer.confirm("Do you want to use this directory?")
        if not is_correct_output_dir:
            custom_output_dir = typer.prompt(
                "Enter the path to save Phenopackets",
                type=Path
            )
            output_dir = custom_output_dir

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    between_section_separator()

    # Step 4: Determine mapping configuration
    mapping_configs = None
    if mappings:
        try:
            # Attempt to load custom mappings if provided
            import importlib.util
            spec = importlib.util.spec_from_file_location("custom_mappings", mappings)
            custom_mappings_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(custom_mappings_module)
            
            # Attempt to find a function that returns mappings
            if hasattr(custom_mappings_module, 'create_phenopacket_mappings'):
                mapping_configs = custom_mappings_module.create_phenopacket_mappings()
            else:
                typer.secho(
                    error_text("❌ No create_phenopacket_mappings function found in the custom mappings file."),
                    fg=typer.colors.YELLOW
                )
        except Exception as e:
            typer.secho(
                error_text(f"❌ Failed to load custom mappings: {str(e)}"),
                fg=typer.colors.YELLOW
            )
    
    # Use default RareLink mappings if no custom mappings provided
    if mapping_configs is None:
        mapping_configs = create_rarelink_phenopacket_mappings()

    typer.echo("Note - This pipeline fetches labels from BIOPORTAL. "
            "Ensure you have an internet connection as this may take a while.")

    try:
        typer.echo("🚀 Processing your REDCap records to Phenopackets...")

        # Load the JSON data from the file
        with open(input_path, "r") as f:
            input_data = json.load(f)

        # Use the number of records in input_data for the progress bar
        phenopacket_pipeline(
            input_data=input_data, 
            output_dir=str(output_dir), 
            created_by=created_by,
            mapping_configs=mapping_configs
        )
        
        typer.secho(success_text("✅ Phenopackets successfully created!"))
        typer.echo(f"📂 Find your Phenopackets here: {output_dir}")
        
    except Exception as e:
        typer.secho(
            error_text(f"❌ Failed to export Phenopackets: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    end_of_section_separator()

if __name__ == "__main__":
    app()