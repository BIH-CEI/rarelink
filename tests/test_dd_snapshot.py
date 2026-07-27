"""Phase 0 safety net — freeze the REDCap data dictionary (invariant I4).

The shipped ``rarelink_cdm_datadictionary - v2_0_6.csv`` is **hand-maintained**
today, so right now it *is* the source of truth and this test simply asserts it
has not drifted.

In Phase 3 the schema-driven generator becomes the producer and this same golden
becomes the target it must reproduce byte-for-byte — at which point only the
``_shipped_dd_text()`` call below changes, not the golden.

Create the golden once (from the repo root)::

    mkdir -p tests/_baseline
    cp "src/rarelink/rarelink_cdm/rarelink_cdm_datadictionary - v2_0_6.csv" \\
       tests/_baseline/rarelink_cdm_datadictionary.golden.csv
"""

from __future__ import annotations

import difflib
from pathlib import Path

import pytest

from rarelink.rarelink_cdm import get_data_dictionary_path

GOLDEN = (
    Path(__file__).parent
    / "_baseline"
    / "rarelink_cdm_datadictionary.golden.csv"
)


def _normalize(text: str) -> list[str]:
    """Split into lines, ignoring line-ending and trailing-newline noise."""
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n").split("\n")


def _shipped_dd_text() -> str:
    return Path(str(get_data_dictionary_path())).read_text(encoding="utf-8")


def test_data_dictionary_matches_golden() -> None:
    if not GOLDEN.exists():
        pytest.skip(
            f"golden not created yet — see the cp command in this file's "
            f"docstring ({GOLDEN} missing)"
        )

    shipped = _normalize(_shipped_dd_text())
    golden = _normalize(GOLDEN.read_text(encoding="utf-8"))

    if shipped != golden:
        diff = "\n".join(
            list(
                difflib.unified_diff(
                    golden,
                    shipped,
                    fromfile="golden",
                    tofile="shipped",
                    lineterm="",
                )
            )[:40]
        )
        pytest.fail(
            "REDCap data dictionary drifted from the frozen v2.0.6 golden.\n"
            "If this change is intended, re-baseline the golden in the same PR "
            "and justify it in the PR description.\n\n" + diff
        )


def test_data_dictionary_is_shipped() -> None:
    """The DD must stay packaged — cieinr/marfan resolve it via this helper."""
    path = Path(str(get_data_dictionary_path()))
    assert path.exists(), f"packaged data dictionary not found at {path}"
