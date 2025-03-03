import typer
import json
from pathlib import Path
from dotenv import dotenv_values
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
)
from rarelink.cli.utils.string_utils import (
    format_header,
    success_text,
    error_text
)
from rarelink.cli.utils.validation_utils import validate_env
from rarelink.utils.validation import validate_and_encode_hgvs
import logging

logger = logging.getLogger(__name__)
app = typer.Typer()

# Define constants used across commands
REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file

@app.command()
def app(output_dir: Path = DEFAULT_OUTPUT_DIR):
    """
    Validate and encode HGVS strings in the REDCap records.

    This command iterates over all records in the designated output directory,
    validates each record’s HGVS strings, and produces a summary report showing
    the total number of validations attempted, succeeded, and failed.

    For records from the genetic findings instrument (i.e. where
    'redcap_repeat_instrument' is 'rarelink_6_1_genetic_findings'),
    any failures are listed along with the record_id and repeat instance.

    Args:
        output_dir (Path): Directory containing the REDCap records.
                           Defaults to ~/Downloads/rarelink_records.
    """
    format_header("Validate HGVS Strings in REDCap Records")
    validate_env(["REDCAP_PROJECT_NAME"])

    env_values = dotenv_values(ENV_PATH)
    project_name = env_values["REDCAP_PROJECT_NAME"]
    sanitized_project_name = project_name.replace(" ", "_")
    records_file = output_dir / f"{sanitized_project_name}-records.json"

    if not records_file.exists():
        error_text(
            f"Records file not found at {records_file}. Please run 'rarelink redcap download-records' first."
        )
        raise typer.Exit(1)

    try:
        with open(records_file, 'r') as file:
            records = json.load(file)

        typer.echo("🔄 Validating HGVS strings in records...")
        total_validations = 0
        total_successes = 0
        total_failures = 0
        failed_records = []

        updated_records = []
        for rec in records:
            rec = validate_and_encode_hgvs(rec, transcript_key="transcript")
            summary = rec.get("_hgvs_validation_summary", {})
            total_validations += summary.get("validations_attempted", 0)
            total_successes += summary.get("successes", 0)
            total_failures += summary.get("failures", 0)
            if rec.get("redcap_repeat_instrument") == "rarelink_6_1_genetic_findings" and summary.get("failures", 0) > 0:
                failed_records.append({
                    "record_id": rec.get("record_id"),
                    "redcap_repeat_instance": rec.get("redcap_repeat_instance"),
                    "failures": summary.get("failure_details")
                })
            updated_records.append(rec)

        with open(records_file, 'w') as file:
            json.dump(updated_records, file, indent=4)

        typer.echo("\nValidation Summary:")
        typer.echo(f"Total HGVS validations attempted: {total_validations}")
        typer.echo(f"Total successful validations: {total_successes}")
        typer.echo(f"Total failed validations: {total_failures}")

        if failed_records:
            typer.echo("\nFailed validations for genetic findings records:")
            for rec in failed_records:
                typer.echo(f"Record {rec['record_id']} (instance {rec.get('redcap_repeat_instance')}):")
                for fail in rec.get("failures", []):
                    typer.echo(f"  - Variable '{fail['variable']}': {fail['error']}")

        success_text("✅ HGVS validation and encoding completed successfully!")
    except Exception as e:
        error_text(f"❌ Error during HGVS validation: {e}")
        raise typer.Exit(1)

    end_of_section_separator()

if __name__ == "__main__":
    app()