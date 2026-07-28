"""Shared helpers for the Phenopacket golden oracle.

Imported by **both** ``scripts/generate_goldens.py`` and
``tests/phenopackets/test_golden_phenopackets.py`` so the normalization applied
when freezing a golden can never drift from the normalization applied when
comparing against it — a mismatch there produces phantom failures.
"""

from __future__ import annotations

import json
import re
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

# Timestamps and creator differ on every run by design.
VOLATILE_METADATA = ("created", "createdBy")

# metaData.resources is environment-dependent and therefore excluded from the
# golden comparison. Which code systems appear depends on MetadataMapper's deep
# prefix scan (_collect_prefixes_deep), which yields different results on
# Linux/py3.10 than on macOS/py3.12 for identical input — CI omits `hgvs`, for
# example. That is a real defect in the export (two sites can emit different
# resource lists for the same record), tracked separately.
#
# Phase 2.4 rewrites this path when rd-cdm becomes the single source of truth for
# code systems. Once resource selection is deterministic, delete this tuple and
# let the goldens assert on resources again. Until then
# test_metadata_has_resources keeps a weaker sanity check.
UNSTABLE_METADATA = ("resources",)

NON_PHENOPACKET_FILES = {"failures.json", "warnings.json", "label_dict.json"}

# Randomly generated identifiers (currently the VariationDescriptor id, which is
# a fresh uuid on every run). Masked so the oracle can compare everything else.
#
# NOTE: this is a *known non-determinism in the pipeline*, not a property we
# want. The same record exported twice yields two different variant ids. Phase 3
# should derive that id from (record_id, redcap_repeat_instance) instead; once it
# does, drop this mask and let the real value be compared.
_GENERATED_ID = re.compile(
    r"^[0-9a-f]{30,32}$"
    r"|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)
GENERATED_ID_PLACEHOLDER = "<generated-id>"


def _mask_generated_ids(node):
    """Replace opaque generated hex/uuid ``id`` values with a placeholder.

    Deliberately narrow: only values under an ``"id"`` key that are pure hex of
    uuid length. Real identifiers are unaffected — CURIEs contain ``:``, record
    and subject ids are short, interpretation ids look like ``101-interpretation-0``.
    """
    if isinstance(node, dict):
        return {
            key: (
                GENERATED_ID_PLACEHOLDER
                if key == "id"
                and isinstance(value, str)
                and _GENERATED_ID.match(value)
                else _mask_generated_ids(value)
            )
            for key, value in node.items()
        }
    if isinstance(node, list):
        return [_mask_generated_ids(item) for item in node]
    return node


def normalize(doc: dict) -> dict:
    """Strip volatile/environment-dependent fields and canonicalize.

    Applied to **both** sides of a golden comparison, so changing what is
    normalized never requires regenerating the goldens.
    """
    meta = doc.get("metaData")
    if isinstance(meta, dict):
        for key in VOLATILE_METADATA + UNSTABLE_METADATA:
            meta.pop(key, None)
    doc = _mask_generated_ids(doc)
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
