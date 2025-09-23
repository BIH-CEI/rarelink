# Auto generated from rarelink_4_care_pathway.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:58:27
# Schema: rarelink_4_care_pathway
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_4_care_pathway.yaml
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import (
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None


# Namespaces
HL7FHIR = CurieNamespace('HL7FHIR', 'http://hl7.org/fhir/')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/sct/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = RARELINK


# Types
class UnionDateString(String):
    """ A field that allows both dates and empty strings. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "union_date_string"
    type_model_uri = RARELINK.UnionDateString


# Class references



@dataclass(repr=False)
class CarePathway(YAMLRoot):
    """
    The section Care Pathway (4) of the RareLink CDM, documenting encounters including their start and end dates,
    status, and class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CarePathway"]
    class_class_curie: ClassVar[str] = "rarelink:CarePathway"
    class_name: ClassVar[str] = "CarePathway"
    class_model_uri: ClassVar[URIRef] = RARELINK.CarePathway

    snomedct_305058001: Union[str, "EncounterStatus"] = None
    hl7fhir_encounter_class: Union[str, "EncounterClass"] = None
    rarelink_4_care_pathway_complete: str = None
    hl7fhir_enc_period_start: Optional[Union[str, UnionDateString]] = None
    hl7fhir_enc_period_end: Optional[Union[str, UnionDateString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomedct_305058001):
            self.MissingRequiredField("snomedct_305058001")
        if not isinstance(self.snomedct_305058001, EncounterStatus):
            self.snomedct_305058001 = EncounterStatus(self.snomedct_305058001)

        if self._is_empty(self.hl7fhir_encounter_class):
            self.MissingRequiredField("hl7fhir_encounter_class")
        if not isinstance(self.hl7fhir_encounter_class, EncounterClass):
            self.hl7fhir_encounter_class = EncounterClass(self.hl7fhir_encounter_class)

        if self._is_empty(self.rarelink_4_care_pathway_complete):
            self.MissingRequiredField("rarelink_4_care_pathway_complete")
        if not isinstance(self.rarelink_4_care_pathway_complete, str):
            self.rarelink_4_care_pathway_complete = str(self.rarelink_4_care_pathway_complete)

        if self.hl7fhir_enc_period_start is not None and not isinstance(self.hl7fhir_enc_period_start, UnionDateString):
            self.hl7fhir_enc_period_start = UnionDateString(self.hl7fhir_enc_period_start)

        if self.hl7fhir_enc_period_end is not None and not isinstance(self.hl7fhir_enc_period_end, UnionDateString):
            self.hl7fhir_enc_period_end = UnionDateString(self.hl7fhir_enc_period_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystemsContainer(YAMLRoot):
    """
    A container class for all code systems used in RareLink.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystemsContainer"]
    class_class_curie: ClassVar[str] = "rarelink:CodeSystemsContainer"
    class_name: ClassVar[str] = "CodeSystemsContainer"
    class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystemsContainer

    ncbi_taxon: Union[str, "NCBITaxon"] = None
    SNOMEDCT: Union[str, "SNOMEDCT"] = None
    mondo: Union[str, "MONDO"] = None
    hpo: Union[str, "HP"] = None
    loinc: Union[str, "LOINC"] = None
    omim: Union[str, "OMIM"] = None
    orpha: Union[str, "ORPHA"] = None
    ncit: Union[str, "NCIT"] = None
    uo: Union[str, "UO"] = None
    hgnc: Union[str, "HGNC"] = None
    hgvs: Union[str, "HGVS"] = None
    ga4gh: Union[str, "GA4GH"] = None
    hl7fhir: Union[str, "HL7FHIR"] = None
    icd11: Union[str, "ICD11"] = None
    icd10cm: Union[str, "ICD10CM"] = None
    icd10gm: Union[str, "ICD10GM"] = None
    so: Union[str, "SO"] = None
    geno: Union[str, "GENO"] = None
    iso3166: Union[str, "ISO3166"] = None
    icf: Union[str, "ICF"] = None

# Enumerations
class EncounterStatus(EnumDefinitionImpl):

    hl7fhir_planned = PermissibleValue(
        text="hl7fhir_planned",
        description="Planned",
        meaning=HL7FHIR["planned"])
    hl7fhir_arrived = PermissibleValue(
        text="hl7fhir_arrived",
        description="Arrived",
        meaning=HL7FHIR["arrived"])
    hl7fhir_triaged = PermissibleValue(
        text="hl7fhir_triaged",
        description="Triaged",
        meaning=HL7FHIR["triaged"])
    hl7fhir_onleave = PermissibleValue(
        text="hl7fhir_onleave",
        description="On Leave",
        meaning=HL7FHIR["onleave"])
    hl7fhir_finished = PermissibleValue(
        text="hl7fhir_finished",
        description="Finished",
        meaning=HL7FHIR["finished"])
    hl7fhir_cancelled = PermissibleValue(
        text="hl7fhir_cancelled",
        description="Cancelled",
        meaning=HL7FHIR["cancelled"])
    hl7fhir_unknown = PermissibleValue(
        text="hl7fhir_unknown",
        description="Unknown",
        meaning=HL7FHIR["unknown"])

    _defn = EnumDefinition(
        name="EncounterStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_in-progress",
            PermissibleValue(
                text="hl7fhir_in-progress",
                description="In Progress",
                meaning=HL7FHIR["in-progress"]))
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))

class EncounterClass(EnumDefinitionImpl):

    hl7fhir_amb = PermissibleValue(
        text="hl7fhir_amb",
        description="Ambulatory",
        meaning=HL7FHIR["amb"])
    hl7fhir_imp = PermissibleValue(
        text="hl7fhir_imp",
        description="Inpatient",
        meaning=HL7FHIR["imp"])
    hl7fhir_obsenc = PermissibleValue(
        text="hl7fhir_obsenc",
        description="Observation",
        meaning=HL7FHIR["obsenc"])
    hl7fhir_emer = PermissibleValue(
        text="hl7fhir_emer",
        description="Emergency",
        meaning=HL7FHIR["emer"])
    hl7fhir_vr = PermissibleValue(
        text="hl7fhir_vr",
        description="Virtual",
        meaning=HL7FHIR["vr"])
    hl7fhir_hh = PermissibleValue(
        text="hl7fhir_hh",
        description="Home Health",
        meaning=HL7FHIR["hh"])
    rarelink_rdc = PermissibleValue(
        text="rarelink_rdc",
        description="RD Specialist Center",
        meaning=RARELINK["rdc"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="EncounterClass",
    )

class NCBITaxon(EnumDefinitionImpl):
    """
    NCBI organismal classification
    """
    _defn = EnumDefinition(
        name="NCBITaxon",
        description="NCBI organismal classification",
        code_set_version="2024-07-03",
    )

class SNOMEDCT(EnumDefinitionImpl):
    """
    SNOMED CT
    """
    _defn = EnumDefinition(
        name="SNOMEDCT",
        description="SNOMED CT",
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class MONDO(EnumDefinitionImpl):
    """
    Monarch Disease Ontology
    """
    _defn = EnumDefinition(
        name="MONDO",
        description="Monarch Disease Ontology",
        code_set_version="2025-06-03",
    )

class HP(EnumDefinitionImpl):
    """
    Human Phenotype Ontology
    """
    _defn = EnumDefinition(
        name="HP",
        description="Human Phenotype Ontology",
        code_set_version="2025-05-06",
    )

class LOINC(EnumDefinitionImpl):
    """
    Logical Observation Identifiers Names and Codes
    """
    _defn = EnumDefinition(
        name="LOINC",
        description="Logical Observation Identifiers Names and Codes",
        code_set_version="LNC278",
    )

class OMIM(EnumDefinitionImpl):
    """
    Online Mendelian Inheritance
    """
    _defn = EnumDefinition(
        name="OMIM",
        description="Online Mendelian Inheritance",
        code_set_version="OMIM2024_08_09",
    )

class ORPHA(EnumDefinitionImpl):
    """
    Orphanet Rare Disease Ontology
    """
    _defn = EnumDefinition(
        name="ORPHA",
        description="Orphanet Rare Disease Ontology",
        code_set_version="OMIM2024_08_09",
    )

class NCIT(EnumDefinitionImpl):
    """
    NCI Thesaurus OBO Edition
    """
    _defn = EnumDefinition(
        name="NCIT",
        description="NCI Thesaurus OBO Edition",
        code_set_version="24.01e",
    )

class UO(EnumDefinitionImpl):
    """
    Units of Measurement Ontology
    """
    _defn = EnumDefinition(
        name="UO",
        description="Units of Measurement Ontology",
        code_set_version="OMIM2024_08_09",
    )

class HGNC(EnumDefinitionImpl):
    """
    HUGO Gene Nomenclature Committee
    """
    _defn = EnumDefinition(
        name="HGNC",
        description="HUGO Gene Nomenclature Committee",
        code_set_version="2024-08-23",
    )

class HGVS(EnumDefinitionImpl):
    """
    Human Genome Variation Society
    """
    _defn = EnumDefinition(
        name="HGVS",
        description="Human Genome Variation Society",
        code_set_version="21.0.0",
    )

class GA4GH(EnumDefinitionImpl):
    """
    Global Alliance for Genomics and Health
    """
    _defn = EnumDefinition(
        name="GA4GH",
        description="Global Alliance for Genomics and Health",
        code_set_version="v2.0",
    )

class HL7FHIR(EnumDefinitionImpl):
    """
    Health Level 7 Fast Healthcare Interoperability Resources
    """
    _defn = EnumDefinition(
        name="HL7FHIR",
        description="Health Level 7 Fast Healthcare Interoperability Resources",
        code_set_version="v4.0.1",
    )

class ICD11(EnumDefinitionImpl):
    """
    International Classification of Diseases, Eleventh Revision
    """
    _defn = EnumDefinition(
        name="ICD11",
        description="International Classification of Diseases, Eleventh Revision",
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class ICD10CM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, Clinical Modification
    """
    _defn = EnumDefinition(
        name="ICD10CM",
        description="International Classification of Diseases, Tenth Revision, Clinical Modification",
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class ICD10GM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, German Modification
    """
    _defn = EnumDefinition(
        name="ICD10GM",
        description="International Classification of Diseases, Tenth Revision, German Modification",
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class SO(EnumDefinitionImpl):
    """
    Sequence types and features ontology
    """
    _defn = EnumDefinition(
        name="SO",
        description="Sequence types and features ontology",
        code_set_version="2.6",
    )

class GENO(EnumDefinitionImpl):
    """
    GENO - The Genotype Ontology
    """
    _defn = EnumDefinition(
        name="GENO",
        description="GENO - The Genotype Ontology",
        code_set_version="2023-10-08",
    )

class ISO3166(EnumDefinitionImpl):
    """
    ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes
    """
    _defn = EnumDefinition(
        name="ISO3166",
        description="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
        code_set_version="2020(en)",
    )

class ICF(EnumDefinitionImpl):
    """
    International Classification of Functioning, Disability and Health
    """
    _defn = EnumDefinition(
        name="ICF",
        description="International Classification of Functioning, Disability and Health",
        code_set_version="1.0.2",
    )

# Slots
class slots:
    pass

slots.hl7fhir_enc_period_start = Slot(uri=RARELINK.hl7fhir_enc_period_start, name="hl7fhir_enc_period_start", curie=RARELINK.curie('hl7fhir_enc_period_start'),
                   model_uri=RARELINK.hl7fhir_enc_period_start, domain=None, range=Optional[Union[str, UnionDateString]])

slots.hl7fhir_enc_period_end = Slot(uri=RARELINK.hl7fhir_enc_period_end, name="hl7fhir_enc_period_end", curie=RARELINK.curie('hl7fhir_enc_period_end'),
                   model_uri=RARELINK.hl7fhir_enc_period_end, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_305058001 = Slot(uri=RARELINK.snomedct_305058001, name="snomedct_305058001", curie=RARELINK.curie('snomedct_305058001'),
                   model_uri=RARELINK.snomedct_305058001, domain=None, range=Union[str, "EncounterStatus"])

slots.hl7fhir_encounter_class = Slot(uri=RARELINK.hl7fhir_encounter_class, name="hl7fhir_encounter_class", curie=RARELINK.curie('hl7fhir_encounter_class'),
                   model_uri=RARELINK.hl7fhir_encounter_class, domain=None, range=Union[str, "EncounterClass"])

slots.rarelink_4_care_pathway_complete = Slot(uri=RARELINK.rarelink_4_care_pathway_complete, name="rarelink_4_care_pathway_complete", curie=RARELINK.curie('rarelink_4_care_pathway_complete'),
                   model_uri=RARELINK.rarelink_4_care_pathway_complete, domain=None, range=str)

slots.codeSystemsContainer__ncbi_taxon = Slot(uri=RARELINK.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=RARELINK.curie('ncbi_taxon'),
                   model_uri=RARELINK.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

slots.codeSystemsContainer__SNOMEDCT = Slot(uri=RARELINK.SNOMEDCT, name="codeSystemsContainer__SNOMEDCT", curie=RARELINK.curie('SNOMEDCT'),
                   model_uri=RARELINK.codeSystemsContainer__SNOMEDCT, domain=None, range=Union[str, "SNOMEDCT"])

slots.codeSystemsContainer__mondo = Slot(uri=RARELINK.mondo, name="codeSystemsContainer__mondo", curie=RARELINK.curie('mondo'),
                   model_uri=RARELINK.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

slots.codeSystemsContainer__hpo = Slot(uri=RARELINK.hpo, name="codeSystemsContainer__hpo", curie=RARELINK.curie('hpo'),
                   model_uri=RARELINK.codeSystemsContainer__hpo, domain=None, range=Union[str, "HP"])

slots.codeSystemsContainer__loinc = Slot(uri=RARELINK.loinc, name="codeSystemsContainer__loinc", curie=RARELINK.curie('loinc'),
                   model_uri=RARELINK.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

slots.codeSystemsContainer__omim = Slot(uri=RARELINK.omim, name="codeSystemsContainer__omim", curie=RARELINK.curie('omim'),
                   model_uri=RARELINK.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

slots.codeSystemsContainer__orpha = Slot(uri=RARELINK.orpha, name="codeSystemsContainer__orpha", curie=RARELINK.curie('orpha'),
                   model_uri=RARELINK.codeSystemsContainer__orpha, domain=None, range=Union[str, "ORPHA"])

slots.codeSystemsContainer__ncit = Slot(uri=RARELINK.ncit, name="codeSystemsContainer__ncit", curie=RARELINK.curie('ncit'),
                   model_uri=RARELINK.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

slots.codeSystemsContainer__uo = Slot(uri=RARELINK.uo, name="codeSystemsContainer__uo", curie=RARELINK.curie('uo'),
                   model_uri=RARELINK.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

slots.codeSystemsContainer__hgnc = Slot(uri=RARELINK.hgnc, name="codeSystemsContainer__hgnc", curie=RARELINK.curie('hgnc'),
                   model_uri=RARELINK.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

slots.codeSystemsContainer__hgvs = Slot(uri=RARELINK.hgvs, name="codeSystemsContainer__hgvs", curie=RARELINK.curie('hgvs'),
                   model_uri=RARELINK.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

slots.codeSystemsContainer__ga4gh = Slot(uri=RARELINK.ga4gh, name="codeSystemsContainer__ga4gh", curie=RARELINK.curie('ga4gh'),
                   model_uri=RARELINK.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

slots.codeSystemsContainer__hl7fhir = Slot(uri=RARELINK.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=RARELINK.curie('hl7fhir'),
                   model_uri=RARELINK.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

slots.codeSystemsContainer__icd11 = Slot(uri=RARELINK.icd11, name="codeSystemsContainer__icd11", curie=RARELINK.curie('icd11'),
                   model_uri=RARELINK.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

slots.codeSystemsContainer__icd10cm = Slot(uri=RARELINK.icd10cm, name="codeSystemsContainer__icd10cm", curie=RARELINK.curie('icd10cm'),
                   model_uri=RARELINK.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

slots.codeSystemsContainer__icd10gm = Slot(uri=RARELINK.icd10gm, name="codeSystemsContainer__icd10gm", curie=RARELINK.curie('icd10gm'),
                   model_uri=RARELINK.codeSystemsContainer__icd10gm, domain=None, range=Union[str, "ICD10GM"])

slots.codeSystemsContainer__so = Slot(uri=RARELINK.so, name="codeSystemsContainer__so", curie=RARELINK.curie('so'),
                   model_uri=RARELINK.codeSystemsContainer__so, domain=None, range=Union[str, "SO"])

slots.codeSystemsContainer__geno = Slot(uri=RARELINK.geno, name="codeSystemsContainer__geno", curie=RARELINK.curie('geno'),
                   model_uri=RARELINK.codeSystemsContainer__geno, domain=None, range=Union[str, "GENO"])

slots.codeSystemsContainer__iso3166 = Slot(uri=RARELINK.iso3166, name="codeSystemsContainer__iso3166", curie=RARELINK.curie('iso3166'),
                   model_uri=RARELINK.codeSystemsContainer__iso3166, domain=None, range=Union[str, "ISO3166"])

slots.codeSystemsContainer__icf = Slot(uri=RARELINK.icf, name="codeSystemsContainer__icf", curie=RARELINK.curie('icf'),
                   model_uri=RARELINK.codeSystemsContainer__icf, domain=None, range=Union[str, "ICF"])
