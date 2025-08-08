import typer
from tqdm import tqdm
import sys
try:
    import tty
    import termios  # POSIX only
    _POSIX = True
except ImportError:      # Windows
    import msvcrt
    _POSIX = False

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

    if _POSIX:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        entered = ""
        try:
            tty.setraw(fd)
            while True:
                char = sys.stdin.read(1)
                if char in ("\r", "\n"):
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                    break
                elif char == "\x7f":  # Backspace
                    if entered:
                        entered = entered[:-1]
                        sys.stdout.write("\b \b")
                else:
                    entered += char
                    sys.stdout.write(mask)
                sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return entered
    else:
        entered = ""
        while True:
            ch = msvcrt.getch()
            # handle special keys (arrows, etc.) which come as two bytes: 0 or 224 then code
            if ch in (b"\x00", b"\xe0"):
                msvcrt.getch()
                continue
            if ch in (b"\r", b"\n"):
                sys.stdout.write("\n")
                sys.stdout.flush()
                break
            if ch == b"\x08":  # Backspace
                if entered:
                    entered = entered[:-1]
                    sys.stdout.write("\b \b")
            elif ch == b"\x03":  # Ctrl+C
                raise KeyboardInterrupt
            else:
                try:
                    entered += ch.decode(errors="ignore")
                except Exception:
                    continue
                sys.stdout.write(mask)
            sys.stdout.flush()
        return entered
