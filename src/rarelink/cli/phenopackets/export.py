# src/rarelink/cli/phenopackets/export.py
import json
import typer
import os
import importlib.util
import importlib.machinery
from pathlib import Path
from typing import Optional
import logging
from rarelink_cdm import import_from_latest, list_available_versions, import_from_version


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


app = typer.Typer()

ENV_PATH = Path(".env")
DEFAULT_INPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads"

@app.command()
def export(
    input_path: Path = typer.Option(
        None, "--input-path", "-i", help="Path to the input LinkML JSON file"
    ),
    output_dir: Path = typer.Option(
        None, "--output-dir", "-o", help="Directory to save Phenopackets"
    ),
    mappings: Path = typer.Option(
        None, "--mappings", "-m", help="Path to custom mapping configuration module"
    ),
    label_dict: Path = typer.Option(
        None, "--label-dict", help="Path to JSON file with code→label mappings"
    ),
    debug: bool = typer.Option(
        False, "--debug", "-d", help="Enable debug mode for verbose logging"
    ),
    skip_validation: bool = typer.Option(
        False, "--skip-validation", help="Skip environment validation"
    ),
    created_by: Optional[str] = typer.Option(
        None, "--created-by", help="Override CREATED_BY from .env"
    ),
    bioportal_api_token: Optional[str] = typer.Option(
        None, "--bioportal-api-token", help="Provide BioPortal API token (overrides .env)"
    ),
    timeout: int = typer.Option(
        3600, "--timeout", "-t", help="Timeout in seconds (default: 3600)"
    ),
):
    """
    CLI command to export data to a cohort of Phenopackets.

    Enhanced to support different data models through custom mapping configurations.
    """
    # Configure logging
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=log_level)
    logger = logging.getLogger("rarelink.cli.phenopackets.export")

    format_header("REDCap to Phenopackets Export")

    # Step 1: Validate setup files (only if not skipped)
    if not skip_validation:
        typer.echo("🔄 Validating setup files...")
        typer.echo("🔄 Validating the .env file...")

        # Determine which env keys are required
        required_env_vars = ["CREATED_BY"]
        # Only require BioPortal when we actually plan to use it
        will_use_bioportal = (bioportal_api_token or os.getenv("BIOPORTAL_API_TOKEN")) and not label_dict
        if will_use_bioportal:
            required_env_vars.append("BIOPORTAL_API_TOKEN")

        try:
            validate_env(required_env_vars)
            typer.secho(success_text("✅ Environment validation successful."))
        except Exception as e:
            typer.secho(
                error_text(
                    f"❌ Validation of .env file failed: {str(e)}. "
                    f"Please run {format_command('rarelink setup keys')} "
                    "to configure the required keys."
                ),
                fg=typer.colors.RED,
            )
            typer.secho(
                "💡 You can use --skip-validation to bypass environment validation.",
                fg=typer.colors.YELLOW,
            )
            raise typer.Exit(1)

    # Fetch CREATED_BY from env or argument
    _created_by = created_by or os.getenv("CREATED_BY")
    if not _created_by and not skip_validation:
        typer.secho(
            error_text("❌ Missing CREATED_BY environment variable or --created-by argument."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Fetch BIOPORTAL_API_TOKEN from argument or env
    _api_token = bioportal_api_token or os.getenv("BIOPORTAL_API_TOKEN")
    if not _api_token and not skip_validation:
        typer.secho(
            error_text("❌ Missing BioPortal API token. Provide --bioportal-api-token or set BIOPORTAL_API_TOKEN in .env."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Ensure the BIOPORTAL_API_TOKEN is set in the environment for downstream usage
    if _api_token:
        os.environ["BIOPORTAL_API_TOKEN"] = _api_token

    # Step 2: Determine input file path
    if input_path is None:
        input_path = typer.prompt(
            "Enter the path to the validated linkml-json file",
            type=Path
        )

    if not input_path.exists():
        typer.secho(
            error_text(f"❌ Input file not found: {input_path}."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Step 3: Determine output directory
    if output_dir is None:
        # Try to infer a suitable output directory name
        input_stem = input_path.stem
        suggested_dir = Path.cwd() / f"{input_stem}_phenopackets"

        typer.echo(f"📂 Suggested output directory: {suggested_dir}")
        is_correct_output_dir = typer.confirm("Do you want to use this directory?")
        if not is_correct_output_dir:
            output_dir = typer.prompt(
                "Enter the path to save Phenopackets",
                type=Path
            )
        else:
            output_dir = suggested_dir

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    between_section_separator()

    # Step 4: Determine mapping configuration
    mapping_configs = None
    if mappings:
        try:
            logger.info(f"Loading custom mappings from: {mappings}")

            # Method 1: Try loading as a regular module
            if str(mappings).endswith('.py'):
                # Calculate the module name from the file path
                module_name = mappings.stem

                # Use importlib machinery to load the module
                loader = importlib.machinery.SourceFileLoader(module_name, str(mappings))
                custom_mappings_module = loader.load_module()

                # Check if the module has the expected function
                if hasattr(custom_mappings_module, 'create_phenopacket_mappings'):
                    mapping_configs = custom_mappings_module.create_phenopacket_mappings()
                    logger.info("Successfully loaded custom mappings")
                else:
                    logger.warning("No create_phenopacket_mappings function found in module")
            # Method 2: Try loading as a JSON file
            elif str(mappings).endswith('.json'):
                with open(mappings, 'r') as f:
                    mapping_configs = json.load(f)
                logger.info("Successfully loaded mappings from JSON file")
            else:
                typer.secho(
                    error_text("❌ Unsupported mapping file format. Use .py or .json files."),
                    fg=typer.colors.RED
                )
                raise typer.Exit(1)

        except Exception as e:
            typer.secho(
                error_text(f"❌ Failed to load custom mappings: {str(e)}"),
                fg=typer.colors.RED
            )
            raise typer.Exit(1)
    else:
        try_default = typer.confirm(
            "No custom mappings provided. Would you like to try with default RareLink-CDM mappings?"
        )
        if try_default:
            # First try “latest”, then gracefully fall back through all available versions.
            tried = []
            mod = None
            try:
                mod = import_from_latest("mappings.phenopackets")
            except Exception as first_err:
                tried.append(("latest", str(first_err)))
                for v in list_available_versions():
                    try:
                        mod = import_from_version(v, "mappings.phenopackets")
                        logger.info(f"Using RareLink-CDM mappings from {v}")
                        break
                    except Exception as e:
                        tried.append((v, str(e)))
                        continue
                if mod is None:
                    detail = "; ".join(f"{v}: {err}" for v, err in tried)
                    typer.secho(
                        error_text(f"❌ Default RareLink-CDM mappings not available ({detail})"),
                        fg=typer.colors.RED,
                    )
                    raise typer.Exit(1)

            create_rarelink_phenopacket_mappings = getattr(
                mod, "create_rarelink_phenopacket_mappings"
            )
            mapping_configs = create_rarelink_phenopacket_mappings()
            logger.info("Using default RareLink-CDM mappings")
        else:
            typer.secho(
                error_text("❌ Mapping configurations are required."),
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
    if debug:
        logger.debug("Using the following mapping configurations:")
        for key, value in mapping_configs.items():
            logger.debug(f"- {key}: {list(value.keys()) if isinstance(value, dict) else type(value)}")

    if label_dict:
        from rarelink.utils.label_fetching import fetch_label as _orig_fetch_label

        # 1) load code→label map
        with open(label_dict, "r") as lf:
            label_map = json.load(lf)

        # 2) monkey‐patch the pipeline’s fetch_label so it prefers your dict
        def fetch_label(code: str, enum_class=None, label_dict=None):
            # priority: your map → existing logic
            if code in label_map:
                return label_map[code]
            return _orig_fetch_label(code, enum_class=enum_class, label_dict=label_map)

        # 3) inject into the phenopacket pipeline namespace
        import rarelink.utils.label_fetching as mu
        mu.fetch_label = fetch_label
        
    from rarelink.phenopackets import phenopacket_pipeline

    if not label_dict:
        typer.echo("NOTE: This pipeline may fetch labels from BIOPORTAL. "
                   "Ensure you have an internet connection as this may take a while - time to get a tea ☕ ...")
    else:
        typer.echo("Using local label dictionary for labels (no BioPortal needed).")

    try:
        typer.echo("🚀 Processing your records to Phenopackets...")

        # Load the JSON data from the file
        with open(input_path, "r") as f:
            input_data = json.load(f)

        # Run the pipeline with enhanced error handling and debug support
        phenopackets = phenopacket_pipeline(
            input_data=input_data,
            output_dir=str(output_dir),
            created_by=_created_by,
            mapping_configs=mapping_configs,
            timeout=timeout,
            debug=debug
        )

        typer.secho(success_text("✅ Phenopackets successfully created!"))
        typer.echo(f"📂 Find your Phenopackets here: {output_dir}")

        # Report counts
        typer.echo("\nExport Summary:")
        typer.echo(f"Total records processed: {len(input_data)}")
        typer.echo(f"Total successful exports: {len(phenopackets)}")
        typer.echo(f"Total failed exports: {len(input_data) - len(phenopackets)}")

        # Check for failure report
        failure_file = os.path.join(output_dir, "failures.json")
        if os.path.exists(failure_file):
            typer.secho(
                f"⚠️ Some records failed to process. See {failure_file} for details.",
                fg=typer.colors.YELLOW
            )

    except Exception as e:
        typer.secho(
            error_text(f"❌ Failed to export Phenopackets: {str(e)}"),
            fg=typer.colors.RED,
        )
        if debug:
            import traceback
            traceback.print_exc()
        raise typer.Exit(1)

    end_of_section_separator()


if __name__ == "__main__":
    app()
