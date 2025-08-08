"""
RareLink CLI Entry Point
------------------------

This module allows the CLI to be executed directly via `python -m rarelink.cli`.
"""

import sys
from rarelink.cli import app

if __name__ == "__main__":
    # Run the Typer CLI app with error handling
    try:
        app(prog_name="rarelink")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
