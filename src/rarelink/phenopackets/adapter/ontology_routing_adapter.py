import logging
import re
from typing import Any, Dict, List, Optional, Tuple
from rarelink.utils.code_processing import process_code

logger = logging.getLogger(__name__)

# Semantic defaults based on the Phenopacket Schema v2.0
DEFAULT_ROUTING_RULES: Dict[str, str] = {
    "HP":    "phenotypicFeatures",
    "MONDO": "diseases",
    "OMIM":  "diseases",
    "ORDO":  "diseases",
}

_SKIP_FIELDS = frozenset({
    "redcap_repeat_instrument",
    "redcap_repeat_instance",
    "type_of_infection",
    "type_of_condition",
})

# Prefixes that describe phenotypic features and therefore must NOT appear as
# Disease.term. Named for what it forbids, not for the block it applies to.
_PREFIXES_DISALLOWED_IN_DISEASES = frozenset({"HP"})

# Public API
def should_route(mapping_configs: Dict[str, Any]) -> bool:
    """Return True when ontology routing is configured and enabled."""
    cfg = mapping_configs.get("ontology_routing", {})
    return bool(cfg) and cfg.get("enabled", True)
 
 
def apply_ontology_routing(
    data: Dict[str, Any],
    mapping_configs: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Inspect ``data["repeated_elements"]``, route each element from a
    configured instrument to either ``phenotypicFeatures`` or ``diseases``
    based on the ontology prefix of its type-field value.

    Returns a shallow copy of ``data`` with two extra keys:

    * ``__routed__phenotypicFeatures`` — HP-bearing elements (unchanged dicts)
    * ``__routed__diseases``           — MONDO/OMIM/ORDO elements normalized
      to the ``term_field_1`` / ``onset_date_field`` convention

    The original ``repeated_elements`` list is never mutated.
    """
    routing_cfg = mapping_configs.get("ontology_routing", {})
    rules = _build_rules(routing_cfg)
    instruments = set(routing_cfg.get("instruments", []))
    scan_fields_map: Dict[str, List[str]] = routing_cfg.get("scan_fields", {})
    onset_fields_map: Dict[str, List[str]] = routing_cfg.get("onset_fields", {})

    routed_pf: List[Dict[str, Any]] = []
    routed_diseases: List[Dict[str, Any]] = []
    skipped = 0

    for element in data.get("repeated_elements", []):
        inst = element.get("redcap_repeat_instrument", "")
        if inst not in instruments:
            continue

        inner = element.get(inst, {})
        if not inner:
            continue

        scan = scan_fields_map.get(inst)  # None means scan all fields
        code, field = _find_routable_code(inner, scan)

        if code is None:
            skipped += 1
            logger.debug(
                f"[ontology_routing] {inst} #{element.get('redcap_repeat_instance')}"
                f": no routable code found — element left in original stream"
            )
            continue

        prefix = _get_prefix(code)
        destination = rules.get(prefix.upper()) if prefix else None

        if destination is None:
            logger.debug(
                f"[ontology_routing] {inst} #{element.get('redcap_repeat_instance')}"
                f": prefix '{prefix}' not in routing rules — skipping"
            )
            skipped += 1
            continue

        if destination == "phenotypicFeatures":
            routed_pf.append(element)
            logger.debug(
                f"[ontology_routing] {inst} #{element.get('redcap_repeat_instance')}"
                f": {code} ({prefix}) → phenotypicFeatures"
            )

        elif destination == "diseases":
            onset_fields = onset_fields_map.get(inst, [])
            normalized = _normalize_for_disease_mapper(
                inner, code, onset_fields,
                instance=element.get("redcap_repeat_instance"),
                instrument=inst,
            )
            routed_diseases.append(normalized)
            logger.debug(
                f"[ontology_routing] {inst} #{element.get('redcap_repeat_instance')}"
                f": {code} ({prefix}) → diseases (normalized onset="
                f"{normalized.get('onset_date_field')})"
            )

    logger.debug(
        f"[ontology_routing] result: "
        f"{len(routed_pf)} → phenotypicFeatures, "
        f"{len(routed_diseases)} → diseases, "
        f"{skipped} skipped"
    )

    augmented = dict(data)
    augmented["__routed__phenotypicFeatures"] = routed_pf
    augmented["__routed__diseases"] = routed_diseases
    return augmented


def get_routed_phenotypic_elements(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return pre-routed HP elements, or empty list if routing was not applied."""
    return data.get("__routed__phenotypicFeatures", [])


def get_routed_disease_dicts(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return pre-routed normalized disease dicts, or empty list."""
    return data.get("__routed__diseases", [])


# ---------------------------------------------------------------------------
# Validation helper — for use in validate.py soft-warning checks
# ---------------------------------------------------------------------------

def check_prefix_placement(phenopacket_json: Dict[str, Any]) -> List[str]:
    """
    Inspect a serialized Phenopacket JSON dict and return a list of
    soft-warning messages where ontology terms appear in semantically
    wrong blocks (e.g. an HP: term in ``diseases``).

    These are warnings only — a phenopacket can still be structurally
    valid while violating these semantic conventions.  They are surfaced
    in the validation output to help data curators catch routing errors.
    """
    warnings: List[str] = []

    # HP codes must only appear as PhenotypicFeature.type
    for i, pf in enumerate(phenopacket_json.get("phenotypicFeatures", [])):
        term_id = pf.get("type", {}).get("id", "")
        if term_id and not term_id.startswith("HP:"):
            warnings.append(
                f"phenotypicFeatures[{i}].type.id = '{term_id}' — "
                f"expected HP: prefix (GA4GH Phenopacket v2 convention)"
            )

    # Disease.term must carry a disease ontology (MONDO/OMIM/ORDO), never HP:
    for i, disease in enumerate(phenopacket_json.get("diseases", [])):
        term_id = disease.get("term", {}).get("id", "")
        if term_id:
            prefix = term_id.split(":")[0].upper() if ":" in term_id else ""
            if prefix in _PREFIXES_DISALLOWED_IN_DISEASES:
                warnings.append(
                    f"diseases[{i}].term.id = '{term_id}' — "
                    f"HP: terms describe phenotypic features, not diseases "
                    f"(GA4GH Phenopacket v2 convention)"
                )

    return warnings



# Internal helpers -----------------------------------------------------------
def _build_rules(routing_cfg: Dict[str, Any]) -> Dict[str, str]:
    """Merge user-supplied rules over the semantic defaults."""
    rules = dict(DEFAULT_ROUTING_RULES)
    user_rules = routing_cfg.get("rules", {})
    rules.update({k.upper(): v for k, v in user_rules.items()})
    return rules
 
 
def _get_prefix(code: str) -> Optional[str]:
    if not code:
        return None
    try:
        normalised = process_code(code)
        if ":" in normalised:
            return normalised.split(":")[0].upper()
    except Exception:
        pass
    return None
 
 
def _find_routable_code(
    inner: Dict[str, Any],
    scan_fields: Optional[List[str]],
) -> Tuple[Optional[str], Optional[str]]:
    """
    Scan ``inner`` for the first non-empty string value whose normalised
    prefix appears in ``DEFAULT_ROUTING_RULES``.
 
    Args:
        inner:       The instrument-level dict from a repeated element.
        scan_fields: Explicit list of field names to check, or ``None``
                     to scan all non-structural fields.
 
    Returns:
        ``(code_value, field_name)`` or ``(None, None)``.
    """
    fields_to_check = scan_fields if scan_fields else [
        k for k in inner if k not in _SKIP_FIELDS
    ]
 
    for field in fields_to_check:
        value = inner.get(field)
        if not value or not isinstance(value, str):
            continue
        prefix = _get_prefix(value)
        if prefix and prefix.upper() in DEFAULT_ROUTING_RULES:
            return value, field
 
    return None, None
 
 
def _normalize_for_disease_mapper(
    inner: Dict[str, Any],
    code: str,
    onset_fields: List[str],
    instance: Optional[int] = None,
    instrument: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Produce a normalized dict in the ``term_field_1`` / ``onset_date_field``
    convention expected by DiseaseMapper.
 
    The ``code`` value (e.g. ``"mondo_0043653"``) is placed in
    ``term_field_1``.  The first non-empty value from ``onset_fields``
    is placed in ``onset_date_field``.
 
    ``__source_instrument`` and ``__source_instance`` are added for
    traceability and are ignored by all mappers.
    """
    onset_date: Optional[str] = None
    for field in onset_fields:
        val = inner.get(field)
        if val and isinstance(val, str):
            onset_date = val
            break
 
    return {
        "term_field_1": code,
        "onset_date_field": onset_date,
        "onset_category_field": None,
        "excluded_field": None,
        "primary_site_field": None,
        "__source_instrument": instrument,
        "__source_instance": instance,
    }