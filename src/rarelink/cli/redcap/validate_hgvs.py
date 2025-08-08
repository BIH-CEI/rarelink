import typer
import json
from pathlib import Path
from typing import Optional, List
from dotenv import dotenv_values
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.string_utils import (
    format_header,
    success_text,
    error_text,
    hint_text
)
from rarelink.cli.utils.validation_utils import validate_env
import logging

def validate_and_encode_hgvs(*args, **kwargs):
    from rarelink.utils.validation import validate_and_encode_hgvs as _impl
    return _impl(*args, **kwargs)

logger = logging.getLogger(__name__)
app = typer.Typer()

# Define constants used across commands
REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file

@app.command()
def app(
    input_file: Optional[Path] = typer.Option(
        None, "--input-file", "-i", 
        help="Path to the specific JSON file containing REDCap records"
    ),
    input_dir: Optional[Path] = typer.Option(
        None, "--input-dir", "-d", 
        help="Directory containing the REDCap records (defaults to ~/Downloads/rarelink_records)"
    ),
    hgvs_variables: Optional[List[str]] = typer.Option(
        None, "--hgvs-variable", "-v",
        help="Name of an HGVS field to validate (repeatable). If omitted, uses default HGVS_VARIABLES of the RareLink-CDM."
    ),
):
    """
    Validate and encode HGVS strings in the REDCap records.

    This command iterates over all records in the records file,
    validates each record's HGVS strings (recursing into nested dicts/lists),
    and produces a summary report showing the total number of validations attempted,
    succeeded, and failed.
    """
    format_header("Validate HGVS Strings in REDCap Records")
    validate_env(["REDCAP_PROJECT_NAME"])

    env_values = dotenv_values(ENV_PATH)
    project_name = env_values["REDCAP_PROJECT_NAME"]
    sanitized_project_name = project_name.replace(" ", "_")
    
    # Determine the input file path
    if input_file:
        records_file = input_file
        typer.echo(f"🔍 Using specified input file: {records_file}")
    elif input_dir:
        records_file = input_dir / f"{sanitized_project_name}-records.json"
        typer.echo(f"🔍 Looking for records file in specified directory: {records_file}")
    else:
        default_file = DEFAULT_OUTPUT_DIR / f"{sanitized_project_name}-records.json"
        typer.echo(f"🔍 Default records file location: {default_file}")
        if typer.confirm("Do you want to use this default file path?", default=True):
            records_file = default_file
        else:
            records_file = typer.prompt(
                "Please enter the full path to your records file",
                type=Path
            )

    if not records_file.exists():
        error_text(f"Records file not found at {records_file}.")
        hint_text("You can download records using 'rarelink redcap download-records'")
        raise typer.Exit(1)

    typer.echo(f"📄 Found records file: {records_file}")
    between_section_separator()

    try:
        with open(records_file, 'r') as file:
            records = json.load(file)

        typer.echo("🔄 Validating HGVS strings in records...")
        total_validations = total_successes = total_failures = 0
        failed_records = []

        updated_records = []
        for rec in records:
            # pass the user-supplied list (or None to use defaults)
            rec = validate_and_encode_hgvs(
                rec,
                transcript_key="transcript",
                variables=hgvs_variables
            )
            summary = rec.get("_hgvs_validation_summary", {})
            total_validations += summary.get("validations_attempted", 0)
            total_successes    += summary.get("successes", 0)
            total_failures     += summary.get("failures", 0)

            # only genetic findings instrument has repeat info at top level
            if rec.get("redcap_repeat_instrument") == "rarelink_6_1_genetic_findings" \
               and summary.get("failures", 0) > 0:
                failed_records.append({
                    "record_id": rec.get("record_id"),
                    "redcap_repeat_instance": rec.get("redcap_repeat_instance"),
                    "failures": summary.get("failure_details")
                })

            updated_records.append(rec)

        typer.echo("\nValidation Summary:")
        typer.echo(f"Total HGVS validations attempted: {total_validations}")
        typer.echo(f"Total successful validations:       {total_successes}")
        typer.echo(f"Total failed validations:           {total_failures}")

        if failed_records:
            typer.echo("\nFailed validations for genetic findings records:")
            for fr in failed_records:
                typer.echo(
                    f"Record {fr['record_id']} (instance {fr['redcap_repeat_instance']}):"
                )
                for f in fr["failures"]:
                    typer.echo(f"  - Variable '{f['variable']}': {f['error']}")

        success_text("✅ HGVS validation and encoding completed successfully!")
    except Exception as e:
        error_text(f"❌ Error during HGVS validation: {e}")
        raise typer.Exit(1)

    end_of_section_separator()

if __name__ == "__main__":
    app()
