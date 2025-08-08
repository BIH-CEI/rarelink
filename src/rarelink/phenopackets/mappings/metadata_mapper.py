from __future__ import annotations

from typing import Dict, Any, Optional, Set, List
import logging
from datetime import datetime, timezone
import dataclasses
import re
from collections import deque

from phenopackets import (
    MetaData,
    Resource,
    Phenopacket
)
from rarelink.phenopackets.mappings.base_mapper import BaseMapper
from rarelink.utils.date_handling import date_to_timestamp
from rarelink_cdm import get_codesystems_container_class
import sys
import typing
from typing import get_origin, get_args, ForwardRef

logger = logging.getLogger(__name__)

# Map CodeSystemsContainer field names → CURIE prefixes that imply usage
_FIELD_TO_PREFIXES = {
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

_CURIE_PREFIX_RE = re.compile(r"^([A-Za-z0-9]+):")

def _is_hgvs_syntax(val: str) -> bool:
    if not isinstance(val, str):
        return False
    s = val.strip().lower()
    return s == "hgvs" or s.startswith("hgvs.")


def _resolve_enum_class_from_field(container_cls, field):
    """
    Given a dataclass Field from CodeSystemsContainer, resolve the LinkML
    enum class referenced in its type annotation (e.g., Union[str, "HP"] -> HP).
    Returns the class object or None if it cannot be resolved.
    """
    ann = field.type
    enum_name = None

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


def _latest_versions_map() -> dict[str, str]:
    versions: dict[str, str] = {}
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
                # if enum isn’t present, try instance (legacy datamodel objects)
                inst = getattr(LatestCls(), f.name, None)
                if inst is not None:
                    raw_ver = getattr(inst, "code_set_version", None) or getattr(inst, "version", None)
            if raw_ver:
                versions[f.name] = str(raw_ver)
    except Exception as e:
        logger.debug(f"Could not build latest versions map: {e}")
    return versions


def _filter_fields_by_prefixes(code_systems_container, used_prefixes: Set[str]) -> list[Resource]:
    """
    Return Resource entries for only the used code systems, but with VERSION
    overlaid from the *latest* container when available.
    """
    resources: list[Resource] = []
    latest_ver = _latest_versions_map()

    # normalize once
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


_ALLOWED_KEYS = {
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
    "genomic_interpretations", "genomicInterpretations",
    "variation_descriptors", "variationDescriptors",
    # time-ish (safe)
    "time_observed", "timeObserved",
    "time_at_last_encounter", "timeAtLastEncounter",
}


def _maybe_add_curie_prefix(s: Optional[str], used: Set[str]) -> None:
    if not isinstance(s, str):
        return
    m = _CURIE_PREFIX_RE.match(s)
    if m:
        used.add(m.group(1).upper())

def _is_hgvs_syntax(syntax: Optional[str]) -> bool:
    return isinstance(syntax, str) and syntax.lower().startswith("hgvs")

def _extract_prefix(curie: str) -> Optional[str]:
    if not isinstance(curie, str) or ":" not in curie:
        return None
    return curie.split(":", 1)[0].upper()

def _collect_prefixes_deep(*roots: Any) -> Set[str]:
    used: Set[str] = set()
    q = deque(roots)
    seen: Set[int] = set()
    max_nodes = 20000
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
        if nodes > max_nodes:
            logger.debug("[metadata] prefix scan hit node cap; stopping early")
            break

        # sequence
        if isinstance(obj, (list, tuple, set)):
            q.extend(obj)
            continue

        # dict
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("id", "value_id", "valueId", "code"):
                    _maybe_add_curie_prefix(v, used)
                elif k == "syntax" and _is_hgvs_syntax(v):
                    used.add("HGVS")
                # GA4GH enums by presence (strings)
                elif k in ("progress_status", "interpretation_status", "progressStatus", "interpretationStatus"):
                    if v is not None:
                        used.add("GA4GH")
                if isinstance(v, (dict, list, tuple)) or dataclasses.is_dataclass(v):
                    q.append(v)
            continue

        # dataclass objects
        if dataclasses.is_dataclass(obj):
            for f in dataclasses.fields(obj):
                name = f.name
                try:
                    v = getattr(obj, name)
                except Exception:
                    continue

                # collect direct IDs/codes
                if name in ("id", "value_id", "valueId", "code"):
                    _maybe_add_curie_prefix(v, used)

                # expressions → HGVS
                if name == "expressions" and isinstance(v, (list, tuple)):
                    for ex in v:
                        try:
                            syn = getattr(ex, "syntax", None)
                            if _is_hgvs_syntax(syn):
                                used.add("HGVS")
                        except Exception:
                            pass
                        q.append(ex)

                # GA4GH enums on interpretation/progress
                if name in ("progress_status", "interpretation_status", "progressStatus", "interpretationStatus"):
                    if v is not None:
                        used.add("GA4GH")

                # traverse only whitelisted attrs (plus basic containers)
                if name in _ALLOWED_KEYS or isinstance(v, (list, tuple, dict)) or dataclasses.is_dataclass(v):
                    q.append(v)

            # also pick up common direct attrs that might not be dataclass fields (defensive)
            for k in ("id", "value_id", "valueId", "code"):
                if hasattr(obj, k):
                    _maybe_add_curie_prefix(getattr(obj, k, None), used)

            # gene context HGNC
            for gc_name in ("gene_context", "geneContext"):
                if hasattr(obj, gc_name):
                    gc = getattr(obj, gc_name)
                    if gc is not None:
                        _maybe_add_curie_prefix(getattr(gc, "value_id", None) or getattr(gc, "valueId", None), used)

            continue

        # generic object with attributes
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

def _collect_used_prefixes_from_blocks(
    *,
    features=None,
    diseases=None,
    measurements=None,
    medical_actions=None,
    interpretations=None,
) -> Set[str]:
    """
    Collect CURIE prefixes used anywhere in the main Phenopacket blocks.
    Handles both snake_case and camelCase models, and inspects
    variant structures for HGVS/GENO/HGNC, plus LOINC LA* allelic states.
    """
    used: Set[str] = set()

    def _maybe_add(value):
        if not value or not isinstance(value, str):
            return
        p = _extract_prefix(value)
        if p:
            used.add(p)

    # --- Phenotypic features ---
    for f in features or []:
        t = getattr(f, "type", None)
        if t is not None:
            _maybe_add(getattr(t, "id", None))
        # severity
        sev = getattr(f, "severity", None)
        if sev is not None:
            _maybe_add(getattr(sev, "id", None))
        # modifiers
        for m in getattr(f, "modifiers", []) or []:
            _maybe_add(getattr(m, "id", None))
        # evidence (ECO etc.)
        for ev in getattr(f, "evidence", []) or []:
            ec = getattr(ev, "evidence_code", None) or getattr(ev, "evidenceCode", None)
            if ec is not None:
                _maybe_add(getattr(ec, "id", None))

    # --- Diseases ---
    for d in diseases or []:
        term = getattr(d, "term", None)
        if term is not None:
            _maybe_add(getattr(term, "id", None))
        # primary_site / stage etc. if present
        ps = getattr(d, "primary_site", None) or getattr(d, "primarySite", None)
        if ps is not None:
            _maybe_add(getattr(ps, "id", None))
        for st in getattr(d, "disease_stage", []) or getattr(d, "diseaseStage", []) or []:
            _maybe_add(getattr(st, "id", None))

    # --- Measurements ---
    for m in measurements or []:
        assay = getattr(m, "assay", None)
        if assay is not None:
            _maybe_add(getattr(assay, "id", None))
        mtype = getattr(m, "measurement_type", None) or getattr(m, "measurementType", None)
        if mtype is not None:
            _maybe_add(getattr(mtype, "id", None))
        # value as OntologyClass
        val = getattr(m, "value", None)
        if val is not None:
            oc = getattr(val, "ontology_class", None) or getattr(val, "ontologyClass", None)
            if oc is not None:
                _maybe_add(getattr(oc, "id", None))

    # --- Medical Actions (procedures & treatments) ---
    for a in medical_actions or []:
        proc = getattr(a, "procedure", None)
        if proc is not None:
            code = getattr(proc, "code", None)
            if code is not None:
                _maybe_add(getattr(code, "id", None))
        trt = getattr(a, "treatment", None)
        if trt is not None:
            agent = getattr(trt, "agent", None)
            if agent is not None:
                _maybe_add(getattr(agent, "id", None))
        # adverse events are OntologyClass list
        for ev in getattr(a, "adverse_events", []) or getattr(a, "adverseEvents", []) or []:
            _maybe_add(getattr(ev, "id", None))

    # --- Interpretations → GenomicInterpretation → VariationDescriptor ---
    for intr in interpretations or []:
        diag = getattr(intr, "diagnosis", None)
        gi_list = (
            getattr(diag, "genomic_interpretations", None)
            or getattr(diag, "genomicInterpretations", None)
            or []
        )
        for gi in gi_list:
            vint = (
                getattr(gi, "variant_interpretation", None)
                or getattr(gi, "variantInterpretation", None)
            )
            if not vint:
                continue
            vd = (
                getattr(vint, "variation_descriptor", None)
                or getattr(vint, "variationDescriptor", None)
            )
            if not vd:
                continue

            # allelic_state → typically GENO, sometimes LOINC:LA****
            allelic = getattr(vd, "allelic_state", None) or getattr(vd, "allelicState", None)
            if allelic is not None:
                _maybe_add(getattr(allelic, "id", None))

            # expressions[ ].syntax == hgvs or hgvs.* → HGVS
            for ex in getattr(vd, "expressions", []) or []:
                syn = getattr(ex, "syntax", None)
                if _is_hgvs_syntax(syn):
                    used.add("HGVS")

            # gene_context.value_id → HGNC
            gc = getattr(vd, "gene_context", None) or getattr(vd, "geneContext", None)
            if gc is not None:
                vid = getattr(gc, "value_id", None) or getattr(gc, "valueId", None)
                _maybe_add(vid)

            # structural_type (sometimes LOINC LA-codes or SO terms)
            st = getattr(vd, "structural_type", None) or getattr(vd, "structuralType", None)
            if st is not None:
                _maybe_add(getattr(st, "id", None))

    return used


def _collect_used_prefixes_from_packet(pkt: Phenopacket) -> Set[str]:
    return _collect_prefixes_deep(pkt)

def _collect_used_prefixes_from_blocks(**kwargs) -> Set[str]:
    return _collect_prefixes_deep(*[v for v in kwargs.values() if v is not None])

class MetadataMapper(BaseMapper[MetaData]):
    """
    Mapper for MetaData entity in the Phenopacket schema.

    Behavior:
      - Includes only resources for code systems actually referenced in the Phenopacket(s).
      - If no CodeSystemsContainer is provided, automatically instantiates the latest one
        from `rarelink_cdm` using `get_codesystems_container_class()`.
    """

    def map(self, data: Dict[str, Any], **kwargs) -> MetaData:
        """
        Args (kwargs):
            created_by: str
            code_systems: an instance of latest CodeSystemsContainer (optional)
            used_prefixes: Set[str]  (optional; if omitted we try to infer from `data` if it's a Phenopacket)
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

        # If caller didn’t pass used_prefixes, best-effort inference if data is Phenopacket-like
        if not used_prefixes and isinstance(data, Phenopacket):
            used_prefixes = _collect_used_prefixes_from_packet(data)

        return self._map_single_entity(
            {},
            [],
            created_by=created_by,
            code_systems=code_systems,
            used_prefixes=used_prefixes,
        )

    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> MetaData:
        created_by = kwargs.get("created_by", "") or ""
        code_systems = kwargs.get("code_systems")
        used_prefixes: Set[str] = set(kwargs.get("used_prefixes") or [])

        created_time = datetime.now(timezone.utc).isoformat()
        created_timestamp = date_to_timestamp(created_time)

        resources = []
        if code_systems:
            resources = _filter_fields_by_prefixes(code_systems, used_prefixes)

        return MetaData(
            created_by=created_by,
            created=created_timestamp,
            resources=resources,
            phenopacket_schema_version="2.0",
        )

    def _map_multi_entity(
        self,
        data: Dict[str, Any],
        instruments: list,
        **kwargs,
    ) -> Optional[MetaData]:
        """
        Multi-entity case:

        - If `data` contains a list of Phenopackets under key 'phenopackets', collect a union
          of prefixes across all and filter resources accordingly.
        - If caller provides `used_prefixes`, that overrides inference.
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

        # Infer used prefixes across multiple phenopackets, if not supplied
        if not used_prefixes:
            pkts: List[Phenopacket] = []
            if isinstance(data, dict) and isinstance(data.get("phenopackets"), list):
                pkts = [p for p in data["phenopackets"] if isinstance(p, Phenopacket)]
            # Union all prefixes across packets
            agg: Set[str] = set()
            for p in pkts:
                agg |= _collect_used_prefixes_from_packet(p)
            used_prefixes = agg

        return self._map_single_entity(
            {},
            instruments,
            created_by=created_by,
            code_systems=code_systems,
            used_prefixes=used_prefixes,
        )
