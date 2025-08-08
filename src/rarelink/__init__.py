# src/rarelink/__init__.py
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("rarelink")
except PackageNotFoundError:
    __version__ = "2.0.2"

__all__ = ["__version__"]