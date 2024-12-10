import typer
from tqdm import tqdm
import sys
import tty 
import termios

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
    
def masked_input(prompt: str, mask: str = "#") -> str:
    """
    Prompt the user for input and display a masked version while typing.

    Parameters:
        prompt (str): The message to display to the user.
        mask (str): The character to display instead of the actual input.

    Returns:
        str: The input entered by the user.
    """
    sys.stdout.write(prompt)
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    entered = ""
    try:
        tty.setraw(fd)
        while True:
            char = sys.stdin.read(1)
            if char == "\r" or char == "\n":  # Handle Enter key
                sys.stdout.write("\n")  # Ensure new line
                sys.stdout.flush()
                break
            elif char == "\x7f":  # Handle Backspace key
                if entered:
                    entered = entered[:-1]
                    sys.stdout.write("\b \b")  # Remove last mask character
            else:
                entered += char
                sys.stdout.write(mask)
            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return entered