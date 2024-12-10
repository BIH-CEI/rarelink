from . import before_header_separator, after_header_separator
import typer
import os

def format_command(command: str) -> str:
    """
    Format a terminal command to make it stand out.
    """
    return typer.style(command, fg=typer.colors.BRIGHT_CYAN)

def error_text(text: str) -> str:
    """
    Format text to indicate an error in terminal output.
    """
    return typer.secho(text, fg=typer.colors.RED)

def success_text(text: str) -> str:
    """
    Format text to indicate success in terminal output.
    """
    return typer.secho(text, fg=typer.colors.GREEN)

def hint_text(text: str) -> str:
    """
    Format text to indicate a warning in terminal output.
    """
    return typer.secho(text, fg=typer.colors.YELLOW)

def hyperlink(text: str, url: str) -> str:
    """
    Create a clickable hyperlink for terminal output with a fallback for 
    unsupported terminals.
    """
    if "TERM" in os.environ and os.environ["TERM"] not in ("dumb", ""):
        return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"
    else:
        return f"{text} ({url})"
    
def format_header(title: str, separator_length: int = 80):
    """
    Print a styled header for a CLI command.

    Parameters:
        title (str): The title or header text of the command.
        separator_length (int): The length of the separator line (default: 80).
    """
    before_header_separator(separator_length)
    typer.secho(f"▶▶▶ {title}", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
    after_header_separator(separator_length)