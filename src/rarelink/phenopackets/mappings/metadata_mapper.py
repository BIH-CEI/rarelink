"""Metadata mapper for Phenopackets.

This module inspects a Phenopacket (or a collection thereof), discovers which
code systems are actually *used* (by CURIE prefixes like HP:, MONDO:, GENO:, etc.),
and then builds a `MetaData` block whose `resources` only include those systems.

Key ideas:
- We traverse the packet(s) breadth-first, collecting CURIE prefixes found in common
  fields (id/value_id/code) and a few special cases (HGVS syntax, GA4GH enums).
- We look up the latest known versions for each code system from the current
  `CodeSystemsContainer` in `rarelink_cdm` and overlay those versions in the output.
- If no `used_prefixes` are provided, we infer them from the data.
"""

from __future__ import annotations

import dataclasses
import logging
import re
import sys
import typing
from collections import deque
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set, get_args, get_origin, ForwardRef

from phenopackets import MetaData, Phenopacket, Resource

from rarelink.phenopackets.mappings.base_mapper import BaseMapper
from rarelink.utils.date_handling import date_to_timestamp
from rarelink_cdm import get_codesystems_container_class

logger = logging.getLogger(__name__)

# --- Configuration -----------------------------------------------------------------

# Map CodeSystemsContainer field names → CURIE prefixes that imply usage
# (Keys must match the dataclass field names in the container.)
_FIELD_TO_PREFIXES: Dict[str, List[str]] = {
    "hpo": ["HP", "HPO"],
    "mondo": ["MONDO", "Mondo"],
    "SNOMEDCT": ["SNOMEDCT", "SCTID"],
    "loinc": ["LOINC"],
    "omim": ["OMIM"],
    "orpha": ["ORPHA", "ORDO"],
    "ncit": ["NCIT"],
    "uo": ["UO"],
    "hgnc": ["HGNC"],
    "hgvs": ["HGVS"],
    "ga4gh": ["GA4GH"],
    "hl7fhir": ["FHIR", "HL7FHIR"],
    "icd11": ["ICD11"],
    "icd10cm": ["ICD10CM"],
    "icd10gm": ["ICD10GM"],
    "so": ["SO"],
    "geno": ["GENO"],
    "iso3166": ["ISO3166"],
    "icf": ["ICF"],
    "ncbi_taxon": ["NCBITAXON", "NCBITaxon"],
    "eco": ["ECO"],
    "vo": ["VO"],
}

# Fields we consider "safe/interesting" for deep traversal on dataclasses/objects.
_ALLOWED_KEYS: Set[str] = {
    # code-ish fields
    "type", "term", "assay", "measurement_type", "measurementType",
    "evidence_code", "evidenceCode", "modifiers", "evidence",
    "procedure", "disease_stage", "diseaseStage",
    "expressions", "allelic_state", "allelicState", "zygosity",
    "gene", "gene_context", "geneContext",
    "ontology_class", "ontologyClass",
    "value", "quantity", "unit",
    "taxonomy", "agent", "treatment",
    # block containers
    "subject",
    "phenotypic_features", "phenotypicFeatures",
    "diseases",
    "measurements",
    "medical_actions", "medicalActions",
    "interpretations",
    "diagnosis",
    "genomic_interpretations", "genomicInterpretations",
    "variant_interpretation", "variantInterpretation",
    "variation_descriptor", "variationDescriptor",
    # time-ish (safe)
    "time_observed", "timeObserved",
    "time_at_last_encounter", "timeAtLastEncounter",
}

# Stop traversal if an object graph is unexpectedly huge (defensive).
_MAX_SCAN_NODES = 20_000

# CURIE prefix matcher (e.g., "HP:0001250" → "HP")
_CURIE_PREFIX_RE = re.compile(r"^([A-Za-z0-9]+):")


# --- Helpers: code system metadata --------------------------------------------------

def _resolve_enum_class_from_field(container_cls, field):
    """Resolve a LinkML enum class referenced in a CodeSystemsContainer field.

    Some container fields are annotated like `Union[str, "HP"]`. This inspects the
    annotation and returns the actual enum class object (e.g., HP) if present.

    Returns:
        The enum class object, or None if it cannot be resolved.
    """
    ann = field.type
    enum_name: Optional[str] = None

    origin = get_origin(ann)
    if origin is typing.Union:
        for a in get_args(ann):
            if a is str:
                continue
            if isinstance(a, ForwardRef):
                enum_name = a.__forward_arg__
            elif isinstance(a, type):
                enum_name = a.__name__
    elif isinstance(ann, ForwardRef):
        enum_name = ann.__forward_arg__

    if not enum_name:
        return None

    mod = sys.modules[container_cls.__module__]
    return getattr(mod, enum_name, None)


def _latest_versions_map() -> Dict[str, str]:
    """Build a map of container field name → latest known version string.

    We prefer reading the version from the LinkML enum definition (`_defn.version`
    or `_defn.code_set_version`). If that's missing, we instantiate the container and
    try `code_set_version`/`version` on the instance payload.

    Returns:
        Dict of `{field_name: "version"}` (missing entries mean we could not resolve).
    """
    versions: Dict[str, str] = {}
    try:
        LatestCls = get_codesystems_container_class()
        for f in dataclasses.fields(LatestCls):
            enum_cls = _resolve_enum_class_from_field(LatestCls, f)
            raw_ver = None
            if enum_cls is not None:
                defn = getattr(enum_cls, "_defn", None)
                if defn is not None:
                    raw_ver = getattr(defn, "code_set_version", None) or getattr(defn, "version", None)
            if not raw_ver:
                # If enum isn’t present, try instance (legacy datamodel objects).
                inst = getattr(LatestCls(), f.name, None)
                if inst is not None:
                    raw_ver = getattr(inst, "code_set_version", None) or getattr(inst, "version", None)
            if raw_ver:
                versions[f.name] = str(raw_ver)
    except Exception as e:
        logger.debug(f"Could not build latest versions map: {e}")
    return versions


def _filter_fields_by_prefixes(code_systems_container, used_prefixes: Set[str]) -> List[Resource]:
    """Select `Resource` entries for code systems that are actually used.

    Args:
        code_systems_container: Instance of the CodeSystemsContainer.
        used_prefixes: Set of CURIE prefixes detected in the packet(s); if empty,
            we include *all* code systems.

    Returns:
        A list of `Resource` objects suitable for `MetaData.resources`.
    """
    resources: List[Resource] = []
    latest_ver = _latest_versions_map()

    used_upper = {p.upper() for p in (used_prefixes or set())}
    include_all = not used_upper

    for field in dataclasses.fields(code_systems_container):
        fname = field.name
        value = getattr(code_systems_container, fname, None)
        if not value:
            continue

        if not include_all:
            prefixes = {p.upper() for p in _FIELD_TO_PREFIXES.get(fname, [])}
            if prefixes.isdisjoint(used_upper):
                continue

        # Normalize payload (support both modern payloads and legacy objects).
        if all(hasattr(value, a) for a in ("name", "url", "version")):
            name = value.name
            url = value.url
            ver = value.version
            ns = getattr(value, "prefix", None)
            iri = getattr(value, "iri_prefix", None)
        else:
            name = getattr(value, "description", fname)
            url = getattr(value, "code_set", None) or getattr(value, "url", None) or ""
            ver = getattr(value, "code_set_version", None) or getattr(value, "version", None) or ""
            ns = getattr(value, "prefix", None)
            iri = getattr(value, "iri_prefix", None)

        # Overlay with the latest known version if available.
        if fname in latest_ver and latest_ver[fname]:
            if str(ver) != str(latest_ver[fname]) and logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"[metadata] overriding {fname} version {ver!r} -> {latest_ver[fname]!r}")
            ver = latest_ver[fname]

        resources.append(
            Resource(
                id=fname.lower(),
                name=str(name),
                url=str(url),
                version=str(ver),
                namespace_prefix=ns,
                iri_prefix=iri,
            )
        )
    return resources


# --- Helpers: prefix collection (deep scan) ----------------------------------------

def _maybe_add_curie_prefix(s: Optional[str], used: Set[str]) -> None:
    """If `s` looks like a CURIE (e.g., 'HP:0001250'), add its prefix to `used`."""
    if not isinstance(s, str):
        return
    m = _CURIE_PREFIX_RE.match(s)
    if m:
        used.add(m.group(1).upper())


def _is_hgvs_syntax(syntax: Optional[str]) -> bool:
    """Return True when an expression syntax is HGVS (e.g., 'hgvs' or 'hgvs.c')."""
    return isinstance(syntax, str) and syntax.lower().startswith("hgvs")


def _collect_prefixes_deep(*roots: Any) -> Set[str]:
    """Traverse arbitrary packet-like objects and collect CURIE prefixes.

    We scan:
      - `id` / `value_id` / `valueId` / `code` attributes and dict keys
      - `expressions[].syntax` for HGVS
      - GA4GH enums via presence of `progress_status`/`interpretation_status`
      - Specific nested attributes such as `gene_context.value_id`

    The traversal is defensive (deduped objects; node cap).

    Returns:
        Set of uppercase CURIE prefixes seen (e.g., {"HP", "MONDO", "GENO"}).
    """
    used: Set[str] = set()
    q = deque(roots)
    seen: Set[int] = set()
    nodes = 0

    while q:
        obj = q.popleft()
        if obj is None:
            continue

        oid = id(obj)
        if oid in seen:
            continue
        seen.add(oid)

        nodes += 1
        if nodes > _MAX_SCAN_NODES:
            logger.debug("[metadata] prefix scan hit node cap; stopping early")
            break

        # Sequences
        if isinstance(obj, (list, tuple, set)):
            q.extend(obj)
            continue

        # Dicts
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("id", "value_id", "valueId", "code"):
                    _maybe_add_curie_prefix(v, used)
                elif k == "syntax" and _is_hgvs_syntax(v):
                    used.add("HGVS")
                elif k in ("progress_status", "interpretation_status", "progressStatus", "interpretationStatus"):
                    if v is not None:
                        used.add("GA4GH")
                if isinstance(v, (dict, list, tuple)) or dataclasses.is_dataclass(v):
                    q.append(v)
            continue

        # Dataclasses
        if dataclasses.is_dataclass(obj):
            for f in dataclasses.fields(obj):
                name = f.name
                try:
                    v = getattr(obj, name)
                except Exception:
                    continue

                if name in ("id", "value_id", "valueId", "code"):
                    _maybe_add_curie_prefix(v, used)

                if name == "expressions" and isinstance(v, (list, tuple)):
                    for ex in v:
                        try:
                            if _is_hgvs_syntax(getattr(ex, "syntax", None)):
                                used.add("HGVS")
                        except Exception:
                            pass
                        q.append(ex)

                if name in ("progress_status", "interpretation_status", "progressStatus", "interpretationStatus"):
                    if v is not None:
                        used.add("GA4GH")

                # Traverse selected fields (plus common container types).
                if name in _ALLOWED_KEYS or isinstance(v, (list, tuple, dict)) or dataclasses.is_dataclass(v):
                    q.append(v)

            # Fall-through checks on dataclasses (defensive)
            for k in ("id", "value_id", "valueId", "code"):
                if hasattr(obj, k):
                    _maybe_add_curie_prefix(getattr(obj, k, None), used)

            for gc_name in ("gene_context", "geneContext"):
                if hasattr(obj, gc_name):
                    gc = getattr(obj, gc_name)
                    if gc is not None:
                        _maybe_add_curie_prefix(
                            getattr(gc, "value_id", None) or getattr(gc, "valueId", None),
                            used,
                        )
            continue

        # Generic objects
        for k in ("id", "value_id", "valueId", "code"):
            if hasattr(obj, k):
                _maybe_add_curie_prefix(getattr(obj, k, None), used)

        if hasattr(obj, "expressions"):
            exprs = getattr(obj, "expressions") or []
            for ex in exprs:
                try:
                    if _is_hgvs_syntax(getattr(ex, "syntax", None)):
                        used.add("HGVS")
                except Exception:
                    pass
                q.append(ex)

        for k in ("progress_status", "interpretation_status", "progressStatus", "interpretationStatus"):
            if hasattr(obj, k) and getattr(obj, k) is not None:
                used.add("GA4GH")

        for k in _ALLOWED_KEYS:
            if hasattr(obj, k):
                v = getattr(obj, k)
                if not callable(v):
                    q.append(v)

    return used

def _prefixes_from_variants(interpretations, variation_descriptors) -> Set[str]:
    """Extract HGNC/GENO/HGVS prefixes directly from variant containers (robust)."""
    used: Set[str] = set()

    # 1) Top-level variation_descriptors
    for vd in variation_descriptors or []:
        try:
            gc = getattr(vd, "gene_context", None) or getattr(vd, "geneContext", None)
            if gc:
                vid = getattr(gc, "value_id", None) or getattr(gc, "valueId", None)
                if isinstance(vid, str) and ":" in vid:
                    used.add(vid.split(":", 1)[0].upper())

            allelic = getattr(vd, "allelic_state", None) or getattr(vd, "allelicState", None)
            aid = getattr(allelic, "id", None) if allelic else None
            if isinstance(aid, str) and ":" in aid:
                used.add(aid.split(":", 1)[0].upper())
                # policy: LOINC LA allelic states still imply GENO context
                if aid.upper().startswith("LOINC:LA"):
                    used.add("GENO")

            exprs = getattr(vd, "expressions", None) or []
            for ex in exprs:
                syn = getattr(ex, "syntax", None)
                if isinstance(syn, str) and syn.lower().startswith("hgvs"):
                    used.add("HGVS")
        except Exception:
            pass

    # 2) Variants embedded in interpretations
    for intr in interpretations or []:
        try:
            diag = getattr(intr, "diagnosis", None)
            gis = (getattr(diag, "genomic_interpretations", None)
                   or getattr(diag, "genomicInterpretations", None) or [])
            for gi in gis:
                vint = (getattr(gi, "variant_interpretation", None)
                        or getattr(gi, "variantInterpretation", None))
                vd = (getattr(vint, "variation_descriptor", None)
                      or getattr(vint, "variationDescriptor", None))
                if not vd:
                    continue

                gc = getattr(vd, "gene_context", None) or getattr(vd, "geneContext", None)
                if gc:
                    vid = getattr(gc, "value_id", None) or getattr(gc, "valueId", None)
                    if isinstance(vid, str) and ":" in vid:
                        used.add(vid.split(":", 1)[0].upper())

                allelic = getattr(vd, "allelic_state", None) or getattr(vd, "allelicState", None)
                aid = getattr(allelic, "id", None) if allelic else None
                if isinstance(aid, str) and ":" in aid:
                    used.add(aid.split(":", 1)[0].upper())
                    if aid.upper().startswith("LOINC:LA"):
                        used.add("GENO")

                exprs = getattr(vd, "expressions", None) or []
                for ex in exprs:
                    syn = getattr(ex, "syntax", None)
                    if isinstance(syn, str) and syn.lower().startswith("hgvs"):
                        used.add("HGVS")
        except Exception:
            pass

    return used


def _collect_used_prefixes_from_packet(pkt: Phenopacket) -> Set[str]:
    """Shortcut for collecting prefixes from a single Phenopacket."""
    return _collect_prefixes_deep(pkt)


def _collect_used_prefixes_from_packets(pkts: List[Phenopacket]) -> Set[str]:
    """Collect prefixes from multiple Phenopackets at once (union)."""
    return _collect_prefixes_deep(*pkts)

def collect_used_prefixes_from_blocks(
    *,
    features=None,
    diseases=None,
    measurements=None,
    medical_actions=None,
    interpretations=None,
    variation_descriptors=None,
) -> Set[str]:
    """Collect CURIE prefixes from packet blocks (generic scan + variant-specific pass)."""
    used = _collect_prefixes_deep(
        features,
        diseases,
        measurements,
        medical_actions,
        interpretations,
        variation_descriptors,
    )
    used |= _prefixes_from_variants(interpretations, variation_descriptors)
    return used


# --- Mapper ------------------------------------------------------------------------

class MetadataMapper(BaseMapper[MetaData]):
    """Mapper for Phenopackets `MetaData`.

    Behavior:
      - Includes only resources for code systems actually referenced in the Phenopacket(s).
      - If no CodeSystemsContainer is provided, automatically instantiates the latest one
        via `rarelink_cdm.get_codesystems_container_class()`.
      - Overlays versions with the latest values known to the container.
    """

    def map(self, data: Dict[str, Any], **kwargs) -> MetaData:
        """Map a Phenopacket or packet collection to a `MetaData` instance.

        Keyword Args:
            created_by: Optional[str] – value for `MetaData.created_by`.
            code_systems: Optional[CodeSystemsContainer] – if omitted, we load the latest.
            used_prefixes: Optional[Set[str]] – override auto-detection.

        Notes:
            - If `data` is a `Phenopacket`, we infer prefixes from it.
            - If `data` is a dict with key `"phenopackets"` (list of Phenopacket),
              we infer the union across all.
        """
        created_by = kwargs.get("created_by", "") or ""
        code_systems = kwargs.get("code_systems")
        used_prefixes: Set[str] = set(kwargs.get("used_prefixes") or [])

        if not code_systems:
            try:
                ContainerCls = get_codesystems_container_class()
                code_systems = ContainerCls()
            except Exception as e:
                logger.warning(f"Auto-load CodeSystemsContainer failed: {e}")

        # Infer used prefixes if not provided
        if not used_prefixes:
            if isinstance(data, Phenopacket):
                used_prefixes = _collect_used_prefixes_from_packet(data)
            elif isinstance(data, dict) and isinstance(data.get("phenopackets"), list):
                pkts = [p for p in data["phenopackets"] if isinstance(p, Phenopacket)]
                used_prefixes = _collect_used_prefixes_from_packets(pkts)

        return self._map_single_entity(
            {},
            [],
            created_by=created_by,
            code_systems=code_systems,
            used_prefixes=used_prefixes,
        )

    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> MetaData:
        """Build a single `MetaData` with the given context (internal entry point)."""
        created_by = kwargs.get("created_by", "") or ""
        code_systems = kwargs.get("code_systems")
        used_prefixes: Set[str] = set(kwargs.get("used_prefixes") or [])

        created_time = datetime.now(timezone.utc).isoformat()
        created_timestamp = date_to_timestamp(created_time)

        resources: List[Resource] = []
        if code_systems:
            resources = _filter_fields_by_prefixes(code_systems, used_prefixes)

        return MetaData(
            created_by=created_by,
            created=created_timestamp,
            resources=resources,
            phenopacket_schema_version="2.0",
        )

    def _map_multi_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> Optional[MetaData]:
        """Map multiple Phenopackets to a shared `MetaData` (for batch exports).

        If `used_prefixes` are provided, they override auto-detection. Otherwise:
        - If `data` has key `"phenopackets"` with a list of Phenopacket objects, we infer
          the union of prefixes across all packets.
        """
        created_by = kwargs.get("created_by", "") or ""
        code_systems = kwargs.get("code_systems")
        used_prefixes: Set[str] = set(kwargs.get("used_prefixes") or [])

        if not code_systems:
            try:
                ContainerCls = get_codesystems_container_class()
                code_systems = ContainerCls()
            except Exception as e:
                logger.warning(f"Auto-load CodeSystemsContainer failed: {e}")

        if not used_prefixes:
            pkts: List[Phenopacket] = []
            if isinstance(data, dict) and isinstance(data.get("phenopackets"), list):
                pkts = [p for p in data["phenopackets"] if isinstance(p, Phenopacket)]
            used_prefixes = _collect_used_prefixes_from_packets(pkts)

        return self._map_single_entity(
            {},
            instruments,
            created_by=created_by,
            code_systems=code_systems,
            used_prefixes=used_prefixes,
        )
        
