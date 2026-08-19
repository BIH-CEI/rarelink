"""Phase 0 safety net — freeze the public import surface (invariant I5).

Downstream repos (``cieinr``, ``marfan-charite``) import names from ``rarelink``.
This test fails the moment one of them disappears, so the refactor can only
remove a public name deliberately — by deleting it from SURFACE in the same PR.

Every entry below was verified importable against the tree at
``pre-refactor-baseline``.

Known Phase-2 tripwires (this is the point of the test):
  * ``python_datamodel.CodeSystemsContainer`` is re-exported from
    ``rarelink_code_systems`` — Phase 2.4 deletes that module, so a shim is
    required to keep this green.
  * ``UnionDateString`` was removed deliberately in v2.1.0 (replaced by
    linkml-redcap's ``redcap_date``).
"""

from __future__ import annotations

import importlib

import pytest

# (module, attribute) pairs that must remain importable.
SURFACE: list[tuple[str, str]] = [
    # --- Phenopacket engine entrypoints -----------------------------------
    ("rarelink.phenopackets", "create_phenopacket"),
    ("rarelink.phenopackets", "write_phenopackets"),
    ("rarelink.phenopackets", "phenopacket_pipeline"),
    ("rarelink.phenopackets", "validate_phenopackets"),
    # --- rarelink_cdm public helpers --------------------------------------
    ("rarelink.rarelink_cdm", "CodeSystemsContainer"),
    ("rarelink.rarelink_cdm", "get_codesystems_container_class"),
    ("rarelink.rarelink_cdm", "get_data_dictionary_path"),
    # --- generated datamodel package surface ------------------------------
    ("rarelink.rarelink_cdm.python_datamodel", "CodeSystemsContainer"),
    ("rarelink.rarelink_cdm.python_datamodel", "SexAtBirth"),
    ("rarelink.rarelink_cdm.python_datamodel", "ClinicalVitalStatus"),
    ("rarelink.rarelink_cdm.python_datamodel", "PhenotypicFeatureStatus"),
    # NOTE: RepeatedElement is deliberately NOT listed here. It lives only in
    # rarelink_repeated_elements, which currently cannot be imported at all —
    # see test_repeated_elements_module_imports below.
    # --- default phenopacket mappings used by the CLI ---------------------
    (
        "rarelink.rarelink_cdm.mappings.phenopackets",
        "create_rarelink_phenopacket_mappings",
    ),
    ("rarelink.rarelink_cdm.mappings.phenopackets", "RARELINK_CODE_SYSTEMS"),
    # --- TODO (before Phase 2): grep cieinr/ and marfan-charite/ for
    #     "from rarelink" and add anything they import that is missing here.
]


@pytest.mark.parametrize(
    "module_name,attr", SURFACE, ids=[f"{m}.{a}" for m, a in SURFACE]
)
def test_public_symbol_resolves(module_name: str, attr: str) -> None:
    module = importlib.import_module(module_name)
    assert hasattr(module, attr), (
        f"{module_name}.{attr} is missing — the public surface that "
        f"cieinr/marfan depend on is broken. Either restore it, add a "
        f"deprecation shim, or remove it from SURFACE deliberately."
    )


@pytest.mark.xfail(
    strict=True,
    reason=(
        "KNOWN BROKEN at pre-refactor-baseline. "
        "rarelink_repeated_elements.py raises KeyError('438949009') on import: "
        "pythongen emitted `meaning=SNOMEDCT[...]` expecting a CurieNamespace, "
        "but that module declares only LINKML/RARELINK/XSD namespaces, so the "
        "name resolves to the SNOMEDCT code-system *enum class* inlined from "
        "rarelink_code_systems — a name collision. "
        "Consequence: RepeatedElement and the instrument classes are "
        "unreachable, so they are not part of the working public surface. "
        "Phase 2.3/2.4 (adopt linkml-redcap's RepeatedElement, drop "
        "rarelink_code_systems in favour of rd-cdm) should resolve this. "
        "strict=True: when this starts passing, put RepeatedElement back into "
        "SURFACE and delete this test."
    ),
)
def test_repeated_elements_module_imports() -> None:
    module = importlib.import_module(
        "rarelink.rarelink_cdm.python_datamodel.rarelink_repeated_elements"
    )
    assert hasattr(module, "RepeatedElement")
