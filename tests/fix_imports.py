"""
Helper module to fix import paths in tests.
Import this at the top of each test file to ensure tests directory is in sys.path.
"""
import sys
from pathlib import Path

# Get the path to the project root (parent of tests directory)
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))