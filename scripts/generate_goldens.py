#!/usr/bin/env python
"""Phase 0 safety net — one-time generator for the Phenopacket golden oracle.

Runs the **real** (unmocked) pipeline over the committed sample records,
records every label resolved from BioPortal so the test can replay offline,
normalizes volatile fields, and writes::

    tests/phenopackets/golden/<phenopacket_id>.json
    tests/phenopackets/golden/label_dict.json

Run once from the repo root, then commit the golden directory::

    # the token is read by rarelink.utils.label_fetching at import time,
    # either from the environment or from the repo's .env file
    export BIOPORTAL_API_TOKEN=...
    python scripts/generate_goldens.py

Re-run it **only** to deliberately re-baseline after an intended change, and say
why in the PR description.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tests.phenopackets._golden_utils import (  # noqa: E402
    CREATED_BY,
    GOLDEN_DIR,
    LABEL_DICT,
    NON_PHENOPACKET_FILES,
    SAMPLE,
    normalize,
    patch_everywhere,
    restore,
)


def main() -> None:
    if not SAMPLE.exists():
        sys.exit(f"sample records not found: {SAMPLE}")

    # Import first: every module that from-imports the label helpers must be
    # loaded before we rebind them.
    import rarelink.utils.label_fetching as label_fetching
    from rarelink.phenopackets import phenopacket_pipeline
    from rarelink.rarelink_cdm.mappings.phenopackets import (
        create_rarelink_phenopacket_mappings,
    )

    if not label_fetching.BIOPORTAL_API_TOKEN:
        sys.exit(
            "BIOPORTAL_API_TOKEN is empty — set it in the environment or in "
            "the repo .env file. Labels are fetched from BioPortal, so the "
            "goldens would be generated without them."
        )

    captured: dict[str, str] = {}
    original_bioportal = label_fetching.fetch_label_from_bioportal

    def recording_bioportal(code: str):
        label = original_bioportal(code)
        if code and label:
            captured[str(code)] = label
        return label

    GOLDEN_DIR.mkdir(parents=True, exist_ok=True)
    records = json.loads(SAMPLE.read_text(encoding="utf-8"))
    mapping_configs = create_rarelink_phenopacket_mappings()

    patched = patch_everywhere("fetch_label_from_bioportal", recording_bioportal)
    try:
        with tempfile.TemporaryDirectory() as tmp:
            result = phenopacket_pipeline(
                input_data=records,
                output_dir=tmp,
                created_by=CREATED_BY,
                mapping_configs=mapping_configs,
                timeout=3600,
                debug=False,
            )
            if result.failed_creations:
                sys.exit(
                    "pipeline reported creation failures on the baseline — fix "
                    "these before freezing a golden:\n"
                    + json.dumps(result.failed_creations, indent=2)
                )

            written = 0
            for path in sorted(Path(tmp).glob("*.json")):
                if path.name in NON_PHENOPACKET_FILES:
                    continue
                doc = normalize(json.loads(path.read_text(encoding="utf-8")))
                (GOLDEN_DIR / path.name).write_text(
                    json.dumps(doc, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                written += 1
    finally:
        restore("fetch_label_from_bioportal", patched)

    LABEL_DICT.write_text(
        json.dumps(captured, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(f"total records:        {result.total_records:>4}")
    print(f"phenopackets created: {result.n_created:>4}")
    print(f"goldens written:      {written:>4}  -> {GOLDEN_DIR}")
    print(f"labels captured:      {len(captured):>4}  -> {LABEL_DICT}")
    if result.failed_validations:
        print(
            "\nNOTE: validation failures were reported:\n"
            + json.dumps(result.failed_validations, indent=2)
        )


if __name__ == "__main__":
    main()
