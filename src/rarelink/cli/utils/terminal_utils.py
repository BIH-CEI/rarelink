import typer
from tqdm import tqdm

def before_header_separator(separator_length: int = 80):
    """
    Print a separator line before a command header.
    """
    typer.secho("=" * separator_length, fg=typer.colors.BRIGHT_CYAN)


def after_header_separator(separator_length: int = 80):
    """
    Print a separator line after a command header.
    """
    typer.secho("-" * separator_length, fg=typer.colors.BRIGHT_CYAN)


def between_section_separator(separator_length: int = 80):
    """
    Print a separator line between sections.
    """
    typer.secho("-" * separator_length, fg=typer.colors.CYAN) 


def end_of_section_separator(separator_length: int = 80):
    """
    Print a separator line at the end of a section.
    """
    typer.secho("=" * separator_length, fg=typer.colors.WHITE)

def display_progress_bar(iterable, desc: str = "Processing"):
    """
    Display a progress bar for an iterable using tqdm.
    """
    for item in tqdm(iterable, desc=desc, colour="cyan"):
        yield item

def confirm_action(message: str) -> bool:
    """
    Prompt the user for confirmation and return their choice.
    """
    return typer.confirm(message)

def display_banner(text: str):
    """
    Display a styled banner in the terminal.
    """
    typer.secho(f"{'=' * 80}\n{text}\n{'=' * 80}", fg=typer.colors.CYAN, bold=True)