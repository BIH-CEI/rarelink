"""Shared helpers for the Phenopacket golden oracle.

Imported by **both** ``scripts/generate_goldens.py`` and
``tests/phenopackets/test_golden_phenopackets.py`` so the normalization applied
when freezing a golden can never drift from the normalization applied when
comparing against it — a mismatch there produces phantom failures.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SAMPLE = (
    REPO_ROOT
    / "tests"
    / "phenopackets"
    / "test_data"
    / "sample_records_rarelink_cdm.json"
)
GOLDEN_DIR = REPO_ROOT / "tests" / "phenopackets" / "golden"
LABEL_DICT = GOLDEN_DIR / "label_dict.json"

CREATED_BY = "rarelink-golden-oracle"

VOLATILE_METADATA = ("created", "createdBy")

# metaData.resources is environment-dependent (#251): the prefix scan in
# metadata_mapper yields different results on Linux/py3.10 than macOS/py3.12.
# Remove once #251 is fixed in Phase 2.4.
UNSTABLE_METADATA = ("resources",)

NON_PHENOPACKET_FILES = {"failures.json", "warnings.json", "label_dict.json"}


def normalize(doc: dict) -> dict:
    """Strip volatile/environment-dependent fields. Applied to both sides of a
    golden comparison, so changing it never requires regenerating goldens."""
    meta = doc.get("metaData")
    if isinstance(meta, dict):
        for key in VOLATILE_METADATA + UNSTABLE_METADATA:
            meta.pop(key, None)
    return json.loads(json.dumps(doc, sort_keys=True))


def patch_everywhere(name: str, replacement):
    """Rebind ``name`` in every already-imported module that holds it.

    Several modules (e.g. ``rarelink.utils.processor.processor``) do
    ``from ..label_fetching import fetch_label_from_bioportal``, which binds the
    function at import time — patching only the defining module would miss them
    and the "offline" run would silently hit the network.

    Returns a list of ``(module, original)`` for :func:`restore`.
    """
    import rarelink.utils.label_fetching as source

    original = getattr(source, name)
    patched: list[tuple[object, object]] = []
    for module in list(sys.modules.values()):
        if module is None:
            continue
        if getattr(module, name, None) is original:
            setattr(module, name, replacement)
            patched.append((module, original))
    return patched


def restore(name: str, patched) -> None:
    for module, original in patched:
        setattr(module, name, original)


def golden_ids() -> list[str]:
    if not GOLDEN_DIR.exists():
        return []
    return [
        path.stem
        for path in sorted(GOLDEN_DIR.glob("*.json"))
        if path.name not in NON_PHENOPACKET_FILES
    ]
