# src/rarelink_cdm/__init__.py
from importlib import import_module
from pathlib import Path
import pkgutil
import re

__all__ = [
    "get_codesystems_container_class",
    "get_latest_version",
    "import_from_latest",
    "import_from_version",
    "list_available_versions",
]

_VERSION_RX = re.compile(r"^v(\d+)_(\d+)_(\d+)$")

def list_available_versions() -> list[str]:
    """Return version package names like ['v2_0_4', 'v2_0_1', ...] found on disk."""
    pkg_path = Path(__file__).parent
    names = []
    for m in pkgutil.iter_modules([str(pkg_path)]):
        if _VERSION_RX.match(m.name):
            names.append(m.name)
    # sort descending by numeric tuple
    def _key(v: str):
        a, b, c = _VERSION_RX.match(v).groups()
        return (int(a), int(b), int(c))
    return sorted(names, key=_key, reverse=True)

def _try_import_version(version: str, submodule: str | None = None):
    modname = f"rarelink_cdm.{version}" + (f".{submodule}" if submodule else "")
    return import_module(modname)

def get_latest_version() -> str:
    """Return the newest version that can actually be imported (prefers highest)."""
    for v in list_available_versions():
        try:
            _try_import_version(v)  # smoke test the package
            return v
        except Exception:
            continue
    raise RuntimeError("No importable rarelink_cdm version packages found.")

def import_from_version(version: str, submodule: str):
    """Import a submodule from a specific rarelink_cdm version, e.g. mappings.redcap."""
    return _try_import_version(version, submodule)

def import_from_latest(submodule: str):
    """Import a submodule from the newest importable rarelink_cdm version."""
    last_error = None
    for v in list_available_versions():
        try:
            return import_from_version(v, submodule)
        except Exception as e:
            last_error = e
            continue
    # if we got here, nothing worked
    raise ImportError(f"Could not import {submodule!r} from any rarelink_cdm version") from last_error

def get_codesystems_container_class(version: str | None = None):
    """Return CodeSystemsContainer from the requested (or newest) version."""
    if version:
        mod = import_from_version(version, "python_datamodel")
    else:
        mod = import_from_latest("python_datamodel")
    return getattr(mod, "CodeSystemsContainer")
