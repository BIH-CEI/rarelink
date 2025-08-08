import typer
from pathlib import Path

def execute_pipeline(config: dict):
    """
    Execute a pipeline based on a given configuration.
    """
    typer.secho(f"🚀 Starting pipeline with configuration: {config}", fg=typer.colors.CYAN)
    # Simulated pipeline logic (replace with real implementation)
    try:
        typer.secho("✅ Pipeline executed successfully!", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Pipeline execution failed: {e}", fg=typer.colors.RED)

def validate_pipeline_config(config: dict) -> bool:
    """
    Validate the pipeline configuration.
    """
    required_keys = ["input", "output", "steps"]
    for key in required_keys:
        if key not in config:
            typer.secho(f"❌ Missing required config key: {key}", fg=typer.colors.RED)
            return False
    return True

def log_pipeline_results(results: dict, log_path: Path):
    """
    Log pipeline results to a file.
    """
    try:
        with open(log_path, "w") as log_file:
            log_file.write(str(results))
        typer.secho(f"✅ Pipeline results logged to {log_path}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to log pipeline results: {e}", fg=typer.colors.RED)
        raise
