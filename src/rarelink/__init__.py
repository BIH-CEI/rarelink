from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("rarelink")
except PackageNotFoundError:
    __version__ = "0.0.0+local"  # or None/raise, your call
