"""Phase 0 safety net — the Phenopacket regression oracle (invariants I3, I7).

This is the spine of the refactor: it runs the **real** pipeline (no mocks) over
the committed sample records and asserts the output matches the frozen goldens.
Any diff is either a regression to fix, or an intended change to re-baseline via
``scripts/generate_goldens.py`` — never a silent update.

It runs **offline**: the only non-deterministic *input* is BioPortal label
lookup, so ``fetch_label_from_bioportal`` is replaced by the frozen
``label_dict.json`` captured during generation. Everything else — enum lookup,
local dicts, code processing, mapping, construction — executes for real.

Normalization (volatile metadata, generated uuids) lives in ``_golden_utils`` so
it is shared with the generator and cannot drift.

Generate the goldens once with::

    python scripts/generate_goldens.py
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from rarelink.phenopackets import phenopacket_pipeline, validate_phenopackets

from ._golden_utils import (
    CREATED_BY,
    GOLDEN_DIR,
    LABEL_DICT,
    SAMPLE,
    golden_ids,
    normalize,
    patch_everywhere,
    restore,
)

GENERATE_HINT = (
    "golden oracle not generated — run: python scripts/generate_goldens.py"
)


@pytest.fixture(scope="module")
def generated(tmp_path_factory) -> Path:
    """Run the real pipeline offline and return the output directory."""
    if not LABEL_DICT.exists():
        pytest.skip(GENERATE_HINT)

    # Import before patching so from-import sites are already bound.
    from rarelink.rarelink_cdm.mappings.phenopackets import (
        create_rarelink_phenopacket_mappings,
    )

    labels: dict[str, str] = json.loads(LABEL_DICT.read_text(encoding="utf-8"))

    def offline_bioportal(code: str):
        return labels.get(str(code))

    out_dir = tmp_path_factory.mktemp("golden_run")
    patched = patch_everywhere("fetch_label_from_bioportal", offline_bioportal)
    try:
        records = json.loads(SAMPLE.read_text(encoding="utf-8"))
        result = phenopacket_pipeline(
            input_data=records,
            output_dir=str(out_dir),
            created_by=CREATED_BY,
            mapping_configs=create_rarelink_phenopacket_mappings(),
            timeout=3600,
            debug=False,
        )
    finally:
        restore("fetch_label_from_bioportal", patched)

    assert not result.failed_creations, (
        "pipeline failed to create phenopackets: "
        f"{json.dumps(result.failed_creations, indent=2)}"
    )
    return out_dir


def test_goldens_exist() -> None:
    """Guard against the oracle silently degrading to zero test cases."""
    if not LABEL_DICT.exists():
        pytest.skip(GENERATE_HINT)
    assert golden_ids(), f"no golden phenopackets found in {GOLDEN_DIR}"


@pytest.mark.parametrize("record_id", golden_ids())
def test_phenopacket_matches_golden(generated: Path, record_id: str) -> None:
    produced = generated / f"{record_id}.json"
    assert produced.exists(), (
        f"pipeline did not emit {record_id}.json — a phenopacket that used to "
        f"be produced is missing"
    )

    got = normalize(json.loads(produced.read_text(encoding="utf-8")))
    # Normalize the golden too: what gets normalized can then change without
    # forcing a regeneration of every golden file.
    want = normalize(
        json.loads((GOLDEN_DIR / f"{record_id}.json").read_text(encoding="utf-8"))
    )

    assert got == want, (
        f"phenopacket {record_id} drifted from its golden.\n"
        f"If this change is intended, re-run scripts/generate_goldens.py and "
        f"justify the diff in the PR description."
    )


@pytest.mark.parametrize("record_id", golden_ids())
def test_metadata_has_resources(generated: Path, record_id: str) -> None:
    """Weaker stand-in while metaData.resources is excluded from the golden.

    The exact resource list is environment-dependent (see UNSTABLE_METADATA in
    _golden_utils), so we only assert that code systems are emitted at all and
    that each entry is well-formed. Restore the full comparison in Phase 2.4.
    """
    doc = json.loads((generated / f"{record_id}.json").read_text(encoding="utf-8"))
    resources = doc.get("metaData", {}).get("resources", [])
    assert resources, f"{record_id}: no code-system resources emitted in metaData"
    for resource in resources:
        assert resource.get("id"), f"{record_id}: resource without an id: {resource}"
        assert resource.get("version"), (
            f"{record_id}: resource {resource.get('id')!r} has no version"
        )


@pytest.mark.parametrize("record_id", golden_ids())
def test_phenopacket_validates(generated: Path, record_id: str) -> None:
    success, detail = validate_phenopackets(generated / f"{record_id}.json")
    assert success, f"validation failed for {record_id}: {detail}"
