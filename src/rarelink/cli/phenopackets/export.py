# src/rarelink/cli/phenopackets/export.py
import json
import logging
import os
import importlib.machinery
import warnings as _warnings
from pathlib import Path
from typing import Callable, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.table import Table
from rich.text import Text

from rarelink.rarelink_cdm.mappings import phenopackets as default_mappings
from rarelink.cli.utils.terminal_utils import (
    between_section_separator,
    end_of_section_separator,
)
from rarelink.cli.utils.string_utils import (
    error_text,
    format_command,
    format_header,
    success_text,
)
from rarelink.cli.utils.validation_utils import validate_env

app = typer.Typer()
console = Console()

ENV_PATH = Path(".env")
DEFAULT_INPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads"


def _make_progress(description: str, total: int) -> tuple:
    """
    Create a Progress instance with a single labelled task.
    Returns (progress, task_id) ready to use as a context manager.
    """
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=36),
        MofNCompleteColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    )
    task_id = progress.add_task(description, total=total)
    return progress, task_id


@app.command()
def export(
    input_path: Path = typer.Option(
        None, "--input-path", "-i", help="Path to the input LinkML JSON file"
    ),
    output_dir: Path = typer.Option(
        None, "--output-dir", "-o", help="Directory to save Phenopackets"
    ),
    mappings: Path = typer.Option(
        None, "--mappings", "-m",
        help="Path to custom mapping configuration module"
    ),
    label_dict: Path = typer.Option(
        None, "--label-dict",
        help="Path to JSON file with code→label mappings"
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
        None, "--bioportal-api-token",
        help="Provide BioPortal API token (overrides .env)"
    ),
    timeout: int = typer.Option(
        3600, "--timeout", "-t", help="Timeout in seconds (default: 3600)"
    ),
):
    """
    Export REDCap records to a cohort of GA4GH Phenopackets (v2).
    """
    log_level = logging.DEBUG if debug else logging.WARNING
    logging.basicConfig(level=log_level)
    logging.getLogger("rarelink").setLevel(log_level)
    logger = logging.getLogger("rarelink.cli.phenopackets.export")

    format_header("REDCap to Phenopackets Export")

    # ── Step 1: Environment validation ──────────────────────────────────────
    if not skip_validation:
        typer.echo("🔄 Validating setup files...")
        typer.echo("🔄 Validating the .env file...")

        required_env_vars = ["CREATED_BY"]
        will_use_bioportal = (
            bioportal_api_token or os.getenv("BIOPORTAL_API_TOKEN")
        ) and not label_dict
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
                "💡 You can use --skip-validation to bypass this.",
                fg=typer.colors.YELLOW,
            )
            raise typer.Exit(1)

    _created_by = created_by or os.getenv("CREATED_BY")
    if not _created_by and not skip_validation:
        typer.secho(
            error_text(
                "❌ Missing CREATED_BY environment variable or --created-by argument."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    _api_token = bioportal_api_token or os.getenv("BIOPORTAL_API_TOKEN")
    if not _api_token and not skip_validation:
        typer.secho(
            error_text(
                "❌ Missing BioPortal API token. "
                "Provide --bioportal-api-token or set BIOPORTAL_API_TOKEN in .env."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    if _api_token:
        os.environ["BIOPORTAL_API_TOKEN"] = _api_token

    # ── Step 2: Input file ───────────────────────────────────────────────────
    if input_path is None:
        input_path = typer.prompt(
            "Enter the path to the validated linkml-json file", type=Path
        )
    if not input_path.exists():
        typer.secho(
            error_text(f"❌ Input file not found: {input_path}."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # ── Step 3: Output directory ─────────────────────────────────────────────
    if output_dir is None:
        suggested_dir = Path.cwd() / f"{input_path.stem}_phenopackets"
        typer.echo(f"📂 Suggested output directory: {suggested_dir}")
        if typer.confirm("Do you want to use this directory?"):
            output_dir = suggested_dir
        else:
            output_dir = typer.prompt(
                "Enter the path to save Phenopackets", type=Path
            )

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    between_section_separator()

    # ── Step 4: Mapping configuration ───────────────────────────────────────
    mapping_configs = None
    if mappings:
        try:
            logger.debug(f"Loading custom mappings from: {mappings}")
            if str(mappings).endswith(".py"):
                loader = importlib.machinery.SourceFileLoader(
                    mappings.stem, str(mappings)
                )
                mod = loader.load_module()
                if hasattr(mod, "create_phenopacket_mappings"):
                    mapping_configs = mod.create_phenopacket_mappings()
                else:
                    logger.warning(
                        "No create_phenopacket_mappings function found in module"
                    )
            elif str(mappings).endswith(".json"):
                with open(mappings, "r") as f:
                    mapping_configs = json.load(f)
            else:
                typer.secho(
                    error_text(
                        "❌ Unsupported mapping file format. Use .py or .json."
                    ),
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)
        except Exception as e:
            typer.secho(
                error_text(f"❌ Failed to load custom mappings: {str(e)}"),
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
    else:
        if typer.confirm(
            "No custom mappings provided. Use default RareLink-CDM mappings?"
        ):
            try:
                mapping_configs = (
                    default_mappings.create_rarelink_phenopacket_mappings()
                )
            except Exception as e:
                typer.secho(
                    error_text(
                        f"❌ Default RareLink-CDM mappings not available: {e}"
                    ),
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)
        else:
            typer.secho(
                error_text("❌ Mapping configurations are required."),
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)

    if debug:
        for key, value in mapping_configs.items():
            logger.debug(
                f"- {key}: "
                f"{list(value.keys()) if isinstance(value, dict) else type(value)}"
            )

    # ── Step 5: Optional label dict patch ───────────────────────────────────
    if label_dict:
        from rarelink.utils.label_fetching import fetch_label as _orig

        with open(label_dict, "r") as lf:
            label_map = json.load(lf)

        def fetch_label(code: str, enum_class=None, label_dict=None):
            if code in label_map:
                return label_map[code]
            return _orig(code, enum_class=enum_class, label_dict=label_map)

        import rarelink.utils.label_fetching as mu
        mu.fetch_label = fetch_label

    if not label_dict:
        typer.echo(
            "NOTE: This pipeline may fetch labels from BioPortal. "
            "Ensure you have an internet connection — time to get a tea ☕ ..."
        )
    else:
        typer.echo("Using local label dictionary (no BioPortal needed).")

    # ── Step 6: Load input data ──────────────────────────────────────────────
    with open(input_path, "r") as f:
        input_data = json.load(f)

    total = len(input_data)
    typer.echo(f"\n🚀 Processing {total} record(s) → Phenopackets\n")

    from rarelink.phenopackets.pipeline import phenopacket_pipeline

    # ── Step 7a: Phase 1 progress bar — Creating ─────────────────────────────
    import logging as _logging
    _root_logger = _logging.getLogger()
    _saved_handlers = _root_logger.handlers[:]
    if not debug:
        _root_logger.handlers = []

    _creation_warnings: list = []

    create_progress, create_task = _make_progress(
        "Creating phenopackets", total
    )
    with create_progress:
        def on_created(record_id, success, error):
            create_progress.advance(create_task)
            # Collect per-record warnings (success=True but error contains ⚠ lines)
            if success and error:
                for line in error.splitlines():
                    line = line.lstrip("⚠").strip()
                    if line:
                        _creation_warnings.append(f"Record {record_id}: {line}")

        try:
            result = phenopacket_pipeline(
                input_data=input_data,
                output_dir=str(output_dir),
                created_by=_created_by,
                mapping_configs=mapping_configs,
                timeout=timeout,
                debug=debug,
                progress_callback=on_created,
                validation_callback=None,
            )
        except Exception as e:
            _root_logger.handlers = _saved_handlers
            typer.secho(
                error_text(f"❌ Pipeline failed: {str(e)}"),
                fg=typer.colors.RED,
            )
            if debug:
                import traceback
                traceback.print_exc()
            raise typer.Exit(1)

    # ── Step 7b: Phase 2 progress bar — Validating ───────────────────────────
    _prefix_warnings: list = []

    n_to_validate = result.n_created
    if n_to_validate > 0:
        validate_progress, validate_task = _make_progress(
            "Validating phenopackets", n_to_validate
        )
        with validate_progress:
            def on_validated(file_path, success, error):
                validate_progress.advance(validate_task)
                if error and "Ontology prefix warnings" in error:
                    fname = Path(file_path).name
                    for line in error.splitlines():
                        line = line.strip()
                        if line.startswith("⚠"):
                            _prefix_warnings.append(f"{fname}: {line.lstrip('⚠').strip()}")

            _run_write_and_validate(
                phenopackets=result.phenopackets,
                output_dir=output_dir,
                result=result,
                validation_callback=on_validated,
                debug=debug,
            )
        
        if _prefix_warnings:
            warnings_file = output_dir / "warnings.json"
            existing = []
            if warnings_file.exists():
                with open(warnings_file, "r") as fh:
                    existing = json.load(fh)
            existing.extend(
                {"file": w.split(":")[0], "warning": w, "stage": "validation"}
                for w in _prefix_warnings
            )
            with open(warnings_file, "w") as fh:
                json.dump(existing, fh, indent=2)

    _root_logger.handlers = _saved_handlers

    # ── Step 8: Summary ──────────────────────────────────────────────────────
    console.print()
    _print_summary(
        total=total,
        n_created=result.n_created,
        n_failed_creation=result.n_failed_creation,
        n_validated=result.n_created - result.n_failed_validation,
        n_failed_validation=result.n_failed_validation,
        output_dir=output_dir,
        failed_creations=result.failed_creations,
        failed_validations=result.failed_validations,
        prefix_warnings=_prefix_warnings,
        creation_warnings=_creation_warnings,
    )

    end_of_section_separator()


def _run_write_and_validate(
    phenopackets: list,
    output_dir: Path,
    result,
    validation_callback: Optional[Callable] = None,
    debug: bool = False,
):
    """
    Write and validate a list of already-created Phenopackets.
    Updates result.failed_validations in place.
    Called by export() after the creation phase completes.
    """
    import json as _json
    from google.protobuf.json_format import MessageToDict
    from phenopackets import VitalStatus as VitalStatusEnum
    from rarelink.phenopackets.validate import validate_phenopackets

    output_path = Path(output_dir)

    for phenopacket in phenopackets:
        full = MessageToDict(
            phenopacket,
            preserving_proto_field_name=False,
            including_default_value_fields=False,
        )
        raw_status_int = phenopacket.subject.vital_status.status
        try:
            status_name = VitalStatusEnum.Status.Name(raw_status_int)
        except Exception:
            status_name = "UNKNOWN_STATUS"
        if "subject" in full:
            full["subject"]["vitalStatus"] = {"status": status_name}

        file_path = output_path / f"{phenopacket.id}.json"
        with open(file_path, "w") as f:
            _json.dump(full, f, indent=2)

        try:
            ok, details = validate_phenopackets(file_path)
            if ok:
                if validation_callback:
                    # Pass details even on success — may contain prefix warnings
                    validation_callback(str(file_path), success=True, error=details)
            else:
                result.failed_validations.append(
                    {"file": str(file_path), "error": details}
                )
                if validation_callback:
                    validation_callback(str(file_path), success=False, error=details)
        except Exception as e:
            error_msg = str(e)
            result.failed_validations.append(
                {"file": str(file_path), "error": error_msg}
            )
            if validation_callback:
                validation_callback(str(file_path), success=False, error=error_msg)


def _print_summary(
    total: int,
    n_created: int,
    n_failed_creation: int,
    n_validated: int,
    n_failed_validation: int,
    output_dir: Path,
    failed_creations: list,
    failed_validations: list,
    prefix_warnings: list = None,
    creation_warnings: list = None,
):
    """Render a clean Rich summary table with failure details and warnings."""
    prefix_warnings = prefix_warnings or []
    creation_warnings = creation_warnings or []
    all_ok = (n_failed_creation == 0 and n_failed_validation == 0)
    has_warnings = bool(prefix_warnings or creation_warnings)

    # ── Stats table ──────────────────────────────────────────────────────────
    table = Table(
        title="Export Summary",
        show_header=True,
        header_style="bold white",
        title_style="bold cyan",
        border_style="cyan",
        min_width=52,
    )
    table.add_column("Stage", style="dim", width=24)
    table.add_column("Passed", justify="right", style="green")
    table.add_column("Failed", justify="right")
    table.add_column("Warnings", justify="right")
    table.add_column("Total", justify="right", style="bold")

    def _fail_style(n: int) -> Text:
        return Text(str(n), style="bold red" if n > 0 else "green")

    def _warn_style(n: int) -> Text:
        return Text(str(n), style="bold yellow" if n > 0 else "dim")

    table.add_row(
        "Creation",
        str(n_created),
        _fail_style(n_failed_creation),
        _warn_style(len(creation_warnings)),
        str(total),
    )
    table.add_row(
        "Validation",
        str(n_validated),
        _fail_style(n_failed_validation),
        _warn_style(len(prefix_warnings)),
        str(n_created),
    )

    console.print(table)
    console.print(f"  📂 Output directory: [bold]{output_dir}[/bold]\n")

    # ── Success / failure panel ───────────────────────────────────────────────
    if all_ok and not has_warnings:
        console.print(
            "✅ [green]All phenopackets created and validated successfully![/green]",
        )
        return

    if all_ok and has_warnings:
        console.print(
            "✅ [green]All phenopackets created and validated successfully.[/green]\n"
            "[yellow]Warnings were found — see below.[/yellow]",
        )

    # ── Creation failures ─────────────────────────────────────────────────────
    if failed_creations:
        console.print(f"\n  [red]❌ Creation failures ({len(failed_creations)}):[/red]")
        for f in failed_creations[:5]:
            console.print(f"    [dim]{f['record_id']}[/dim]  {f['error']}")
        if len(failed_creations) > 5:
            console.print(f"    [dim]... and {len(failed_creations) - 5} more — see failures.json[/dim]")

    # ── Validation failures ──────────────────────────────────────────────────
    if failed_validations:
        console.print(f"\n  [yellow]⚠  Validation failures ({len(failed_validations)}):[/yellow]")
        for f in failed_validations[:5]:
            console.print(f"    [dim]{Path(f['file']).name}[/dim]  {f['error'][:80]}")
        if len(failed_validations) > 5:
            console.print(f"    [dim]... and {len(failed_validations) - 5} more — see failures.json[/dim]")

    # ── Creation warnings (inline) ────────────────────────────────────────────
    if creation_warnings:
        unique = list(dict.fromkeys(creation_warnings))
        console.print(f"\n  [yellow]⚠  Creation warnings ({len(creation_warnings)}) — non-fatal:[/yellow]")
        for w in unique[:5]:
            count = creation_warnings.count(w)
            suffix = f" (×{count})" if count > 1 else ""
            console.print(f"    [dim]{w}{suffix}[/dim]")
        if len(unique) > 5:
            console.print(f"    [dim]... and {len(unique) - 5} more distinct warning(s)[/dim]")

    # ── Prefix warnings (inline) ──────────────────────────────────────────────
    if prefix_warnings:
        console.print(f"\n  [yellow]⚠  Ontology prefix warnings ({len(prefix_warnings)}) — non-fatal:[/yellow]")
        for w in prefix_warnings[:5]:
            console.print(f"    [dim]{w}[/dim]")
        if len(prefix_warnings) > 5:
            console.print(f"    [dim]... and {len(prefix_warnings) - 5} more[/dim]")

    failure_file = output_dir / "failures.json"
    warnings_file = output_dir / "warnings.json"
    if failure_file.exists():
        console.print(f"\n  💾 Full failure report: [bold]{failure_file}[/bold]")
    if warnings_file.exists():
        console.print(f"  💾 Full warnings report: [bold]{warnings_file}[/bold]")


if __name__ == "__main__":
    app()