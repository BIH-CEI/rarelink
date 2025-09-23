# src/rarelink/utils/label_fetching.py
from typing import Optional, Dict, Any, List
import logging
import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv

from .code_processing import process_code, normalize_hgnc_id

logger = logging.getLogger(__name__)

# Load environment variables once
load_dotenv()
BIOPORTAL_API_TOKEN = (os.getenv("BIOPORTAL_API_TOKEN") or "").strip()


# ---------- Helpers: candidate forms ----------

def _candidate_codes(code: str) -> List[str]:
    """
    Return a short, ordered list of normalized code variants to try for local lookups.

    Order:
      1) original code
      2) process_code(code)      → canonical CURIE (e.g., hp_0000400 → HP:0000400)
      3) normalize_hgnc_id(...)  → HGNC normalization on both raw and processed
    """
    if not isinstance(code, str) or not code:
        return []

    out: List[str] = []
    seen = set()

    def _add(v: Optional[str]):
        if v and v not in seen:
            out.append(v)
            seen.add(v)

    _add(code)
    pc = process_code(code)
    _add(pc)

    _add(normalize_hgnc_id(code))
    if pc and pc != code:
        _add(normalize_hgnc_id(pc))

    return out


# ---------- Enum lookup ----------

def fetch_label_from_enum(code: str, enum_class: Any) -> Optional[str]:
    """
    Try to fetch a label from a LinkML/Python Enum-like class.

    We attempt a few common patterns:
      - Direct attribute by name (rare)
      - Scan __members__ (Python Enum) for matching value/name/normalized variants
      - Prefer member.description / member.label / member.title, fall back to member.name
    """
    if not code or not enum_class:
        return None

    try:
        # Very rare: direct attribute by literal code
        direct = getattr(enum_class, code, None)
        if direct and hasattr(direct, "description"):
            return getattr(direct, "description", None)

        members = getattr(enum_class, "__members__", None)
        if not isinstance(members, dict):
            return None

        candidates = _candidate_codes(code)

        for name, member in members.items():
            # Things we can compare against
            member_val = getattr(member, "value", None)
            # Some LinkML gens use dicts as value; extract "text"/"meaning"/etc. if present
            member_val_str = None
            if isinstance(member_val, dict):
                member_val_str = (
                    member_val.get("text")
                    or member_val.get("value")
                    or member_val.get("code")
                    or member_val.get("id")
                )
            else:
                member_val_str = str(member_val) if member_val is not None else None

            # Match by member name, value, or normalized forms
            if (
                name in candidates
                or (member_val_str and member_val_str in candidates)
            ):
                for attr in ("description", "label", "title"):
                    lbl = getattr(member, attr, None)
                    if lbl:
                        return lbl
                # If value is a dict with description/label, use that
                if isinstance(member_val, dict):
                    lbl = member_val.get("description") or member_val.get("label")
                    if lbl:
                        return lbl
                # Last resort: member name
                return name

        return None
    except Exception as e:
        logger.debug(f"Enum lookup failed for {code}: {e}")
        return None


# ---------- Dict lookup ----------

def fetch_label_from_dict(code: str, label_dict: Dict[str, str]) -> Optional[str]:
    """
    Try local dictionary first with a couple of canonicalized variants.
    """
    if not code or not label_dict:
        return None

    for cand in _candidate_codes(code):
        if cand in label_dict:
            return label_dict[cand]
    return None


# ---------- BioPortal lookup ----------

def fetch_label_from_bioportal(code: str) -> Optional[str]:
    """
    Fetch a label from the BioPortal API.

    Args:
        code: Canonical CURIE form (PREFIX:ID)
    """
    if not code or ":" not in code or not BIOPORTAL_API_TOKEN:
        return None

    try:
        ontology, identifier = code.split(":", 1)

        # Map some ontologies to their API name & expected IRI form
        ontology_map = {
            "ORPHA":   {"api": "ORDO",       "iri": f"http://www.orpha.net/ORDO/Orphanet_{identifier}"},
            "HGNC":    {"api": "HGNC-NR",    "iri": f"http://identifiers.org/hgnc/{identifier}"},
            "NCIT":    {"api": "NCIT",       "iri": f"http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#{identifier}"},
            "NCBITAXON":{"api": "NCBITAXON", "iri": f"http://purl.bioontology.org/ontology/NCBITAXON/{identifier}"},
            "HP":      {"api": "HP",         "iri": f"http://purl.obolibrary.org/obo/HP_{identifier}"},
            "ICD10CM": {"api": "ICD10CM",    "iri": identifier},
            "SNOMEDCT":{"api": "SNOMEDCT",   "iri": identifier},
            "LOINC":   {"api": "LOINC",      "iri": identifier},
            "MONDO":   {"api": "MONDO",      "iri": f"http://purl.obolibrary.org/obo/MONDO_{identifier}"},
            "OMIM":    {"api": "OMIM",       "iri": f"http://purl.bioontology.org/ontology/OMIM/{identifier}"},
            "ECO":     {"api": "ECO",        "iri": f"http://purl.obolibrary.org/obo/ECO_{identifier}"},
            "UO":      {"api": "UO",         "iri": f"http://purl.obolibrary.org/obo/UO_{identifier}"},
            "VO":      {"api": "VO",         "iri": f"http://purl.obolibrary.org/obo/VO_{identifier}"},
            "GENO":    {"api": "GENO",       "iri": f"http://purl.obolibrary.org/obo/GENO_{identifier}"},
        }

        mapping = ontology_map.get(ontology)
        if mapping:
            api_ontology = mapping["api"]
            iri = mapping["iri"]
        else:
            # Default: pass raw identifier (BioPortal will try)
            logger.debug(f"Unsupported ontology {ontology}; using default pass-through")
            api_ontology = ontology
            iri = identifier

        # Encode IRI for the path segment
        url = (
            f"https://data.bioontology.org/ontologies/"
            f"{api_ontology}/classes/{quote(iri, safe='')}?apikey={BIOPORTAL_API_TOKEN}"
        )

        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("prefLabel")

        # Some ontologies (LOINC/SNOMEDCT) may require a different lookup; keep quiet on non-200.
        return None

    except Exception as e:
        logger.debug(f"BioPortal lookup failed for {code}: {e}")
        return None


# ---------- Unified fetch ----------

def fetch_label(code: str, enum_class: Any = None, label_dict: Dict[str, str] = None) -> Optional[str]:
    """
    Fetch a label with the following priority:
      1) Enum (if provided)
      2) Local label_dict (if provided) — using normalized candidates
      3) BioPortal — only for CURIE-like codes, or after process_code produces one
    """
    if not code:
        return None

    # 1) Enum class
    if enum_class:
        for cand in _candidate_codes(code):
            lbl = fetch_label_from_enum(cand, enum_class)
            if lbl:
                return lbl

    # 2) Local dictionary
    if label_dict:
        lbl = fetch_label_from_dict(code, label_dict)
        if lbl:
            return lbl

    # 3) BioPortal (prefer canonical CURIE; if not, try process_code)
    if ":" in code:
        lbl = fetch_label_from_bioportal(code)
        if lbl:
            return lbl
    else:
        pc = process_code(code)
        if pc and pc != code and ":" in pc:
            lbl = fetch_label_from_bioportal(pc)
            if lbl:
                return lbl

    return None
