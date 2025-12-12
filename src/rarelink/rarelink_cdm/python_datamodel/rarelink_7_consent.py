# Auto generated from rarelink_7_consent.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T16:00:22
# Schema: rarelink_7_consent
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_7_consent.yaml
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
from linkml_runtime.utils.yamlutils import (
    YAMLRoot
)

from rdflib import (
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Namespaces
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/sct/')
HL7FHIR = CurieNamespace('hl7fhir', 'http://hl7.org/fhir/')
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
class Consent(YAMLRoot):
    """
    The section Consent (7) of the RareLink CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["Consent"]
    class_class_curie: ClassVar[str] = "rarelink:Consent"
    class_name: ClassVar[str] = "Consent"
    class_model_uri: ClassVar[URIRef] = RARELINK.Consent

    snomedct_309370004: Union[str, "ConsentStatus"] = None
    snomedct_386318002: str = None
    rarelink_consent_contact: Union[str, "YesNoUnknown"] = None
    rarelink_consent_data: Union[str, "YesNoUnknown"] = None
    rarelink_7_consent_complete: str = None
    hl7fhir_consent_datetime: Optional[Union[str, UnionDateString]] = None
    snomedct_123038009: Optional[Union[str, "YesNoUnknown"]] = None
    rarelink_biobank_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomedct_309370004):
            self.MissingRequiredField("snomedct_309370004")
        if not isinstance(self.snomedct_309370004, ConsentStatus):
            self.snomedct_309370004 = ConsentStatus(self.snomedct_309370004)

        if self._is_empty(self.snomedct_386318002):
            self.MissingRequiredField("snomedct_386318002")
        if not isinstance(self.snomedct_386318002, str):
            self.snomedct_386318002 = str(self.snomedct_386318002)

        if self._is_empty(self.rarelink_consent_contact):
            self.MissingRequiredField("rarelink_consent_contact")
        if not isinstance(self.rarelink_consent_contact, YesNoUnknown):
            self.rarelink_consent_contact = YesNoUnknown(self.rarelink_consent_contact)

        if self._is_empty(self.rarelink_consent_data):
            self.MissingRequiredField("rarelink_consent_data")
        if not isinstance(self.rarelink_consent_data, YesNoUnknown):
            self.rarelink_consent_data = YesNoUnknown(self.rarelink_consent_data)

        if self._is_empty(self.rarelink_7_consent_complete):
            self.MissingRequiredField("rarelink_7_consent_complete")
        if not isinstance(self.rarelink_7_consent_complete, str):
            self.rarelink_7_consent_complete = str(self.rarelink_7_consent_complete)

        if self.hl7fhir_consent_datetime is not None and not isinstance(self.hl7fhir_consent_datetime, UnionDateString):
            self.hl7fhir_consent_datetime = UnionDateString(self.hl7fhir_consent_datetime)

        if self.snomedct_123038009 is not None and not isinstance(self.snomedct_123038009, YesNoUnknown):
            self.snomedct_123038009 = YesNoUnknown(self.snomedct_123038009)

        if self.rarelink_biobank_link is not None and not isinstance(self.rarelink_biobank_link, str):
            self.rarelink_biobank_link = str(self.rarelink_biobank_link)

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
class ConsentStatus(EnumDefinitionImpl):
    """
    The status of the consent provided.
    """
    hl7fhir_draft = PermissibleValue(
        text="hl7fhir_draft",
        description="Pending",
        meaning=HL7FHIR["draft"])
    hl7fhir_proposed = PermissibleValue(
        text="hl7fhir_proposed",
        description="Proposed",
        meaning=HL7FHIR["proposed"])
    hl7fhir_active = PermissibleValue(
        text="hl7fhir_active",
        description="Active",
        meaning=HL7FHIR["active"])
    hl7fhir_rejected = PermissibleValue(
        text="hl7fhir_rejected",
        description="Rejected",
        meaning=HL7FHIR["rejected"])
    hl7fhir_inactive = PermissibleValue(
        text="hl7fhir_inactive",
        description="Inactive",
        meaning=HL7FHIR["inactive"])

    _defn = EnumDefinition(
        name="ConsentStatus",
        description="""The status of the consent provided.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))

class YesNoUnknown(EnumDefinitionImpl):
    """
    Indicates yes, no, or unknown status.
    """
    snomedct_373066001 = PermissibleValue(
        text="snomedct_373066001",
        description="True",
        meaning=SNOMEDCT["373066001"])
    snomedct_373067005 = PermissibleValue(
        text="snomedct_373067005",
        description="False",
        meaning=SNOMEDCT["373067005"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="YesNoUnknown",
        description="""Indicates yes, no, or unknown status.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

slots.snomedct_309370004 = Slot(uri=RARELINK.snomedct_309370004, name="snomedct_309370004", curie=RARELINK.curie('snomedct_309370004'),
                   model_uri=RARELINK.snomedct_309370004, domain=None, range=Union[str, "ConsentStatus"])

slots.hl7fhir_consent_datetime = Slot(uri=RARELINK.hl7fhir_consent_datetime, name="hl7fhir_consent_datetime", curie=RARELINK.curie('hl7fhir_consent_datetime'),
                   model_uri=RARELINK.hl7fhir_consent_datetime, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_386318002 = Slot(uri=RARELINK.snomedct_386318002, name="snomedct_386318002", curie=RARELINK.curie('snomedct_386318002'),
                   model_uri=RARELINK.snomedct_386318002, domain=None, range=str)

slots.rarelink_consent_contact = Slot(uri=RARELINK.rarelink_consent_contact, name="rarelink_consent_contact", curie=RARELINK.curie('rarelink_consent_contact'),
                   model_uri=RARELINK.rarelink_consent_contact, domain=None, range=Union[str, "YesNoUnknown"])

slots.rarelink_consent_data = Slot(uri=RARELINK.rarelink_consent_data, name="rarelink_consent_data", curie=RARELINK.curie('rarelink_consent_data'),
                   model_uri=RARELINK.rarelink_consent_data, domain=None, range=Union[str, "YesNoUnknown"])

slots.snomedct_123038009 = Slot(uri=RARELINK.snomedct_123038009, name="snomedct_123038009", curie=RARELINK.curie('snomedct_123038009'),
                   model_uri=RARELINK.snomedct_123038009, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.rarelink_biobank_link = Slot(uri=RARELINK.rarelink_biobank_link, name="rarelink_biobank_link", curie=RARELINK.curie('rarelink_biobank_link'),
                   model_uri=RARELINK.rarelink_biobank_link, domain=None, range=Optional[str])

slots.rarelink_7_consent_complete = Slot(uri=RARELINK.rarelink_7_consent_complete, name="rarelink_7_consent_complete", curie=RARELINK.curie('rarelink_7_consent_complete'),
                   model_uri=RARELINK.rarelink_7_consent_complete, domain=None, range=str)

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
