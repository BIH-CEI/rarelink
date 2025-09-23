# Auto generated from rarelink_3_patient_status.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:57:32
# Schema: rarelink_3_patient_status
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_3_patient_status.yaml
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
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None


# Namespaces
ICD10CM = CurieNamespace('ICD10CM', 'http://hl7.org/fhir/sid/icd-10-cm')
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
class PatientStatus(YAMLRoot):
    """
    The section Patient Status (3) of the RareLink CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["PatientStatus"]
    class_class_curie: ClassVar[str] = "rarelink:PatientStatus"
    class_name: ClassVar[str] = "PatientStatus"
    class_model_uri: ClassVar[URIRef] = RARELINK.PatientStatus

    rarelink_3_patient_status_complete: str = None
    patient_status_date: Optional[Union[str, XSDDate]] = None
    snomedct_278844005: Optional[Union[str, "ClinicalVitalStatus"]] = None
    snomedct_398299004: Optional[Union[str, UnionDateString]] = None
    snomedct_184305005: Optional[str] = None
    snomedct_105727008: Optional[Union[str, "AgeCategory"]] = None
    snomedct_412726003: Optional[str] = None
    snomedct_723663001: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rarelink_3_patient_status_complete):
            self.MissingRequiredField("rarelink_3_patient_status_complete")
        if not isinstance(self.rarelink_3_patient_status_complete, str):
            self.rarelink_3_patient_status_complete = str(self.rarelink_3_patient_status_complete)

        if self.patient_status_date is not None and not isinstance(self.patient_status_date, XSDDate):
            self.patient_status_date = XSDDate(self.patient_status_date)

        if self.snomedct_278844005 is not None and not isinstance(self.snomedct_278844005, ClinicalVitalStatus):
            self.snomedct_278844005 = ClinicalVitalStatus(self.snomedct_278844005)

        if self.snomedct_398299004 is not None and not isinstance(self.snomedct_398299004, UnionDateString):
            self.snomedct_398299004 = UnionDateString(self.snomedct_398299004)

        if self.snomedct_184305005 is not None and not isinstance(self.snomedct_184305005, str):
            self.snomedct_184305005 = str(self.snomedct_184305005)

        if self.snomedct_105727008 is not None and not isinstance(self.snomedct_105727008, AgeCategory):
            self.snomedct_105727008 = AgeCategory(self.snomedct_105727008)

        if self.snomedct_412726003 is not None and not isinstance(self.snomedct_412726003, str):
            self.snomedct_412726003 = str(self.snomedct_412726003)

        if self.snomedct_723663001 is not None and not isinstance(self.snomedct_723663001, Bool):
            self.snomedct_723663001 = Bool(self.snomedct_723663001)

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
class ClinicalVitalStatus(EnumDefinitionImpl):

    snomedct_438949009 = PermissibleValue(
        text="snomedct_438949009",
        description="Alive",
        meaning=SNOMEDCT["438949009"])
    snomedct_419099009 = PermissibleValue(
        text="snomedct_419099009",
        description="Dead",
        meaning=SNOMEDCT["419099009"])
    snomedct_399307001 = PermissibleValue(
        text="snomedct_399307001",
        description="Unknown - Lost in follow-up",
        meaning=SNOMEDCT["399307001"])
    snomedct_185924006 = PermissibleValue(
        text="snomedct_185924006",
        description="Unknown - Opted-out",
        meaning=SNOMEDCT["185924006"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown - Other Reason",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="ClinicalVitalStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class AgeCategory(EnumDefinitionImpl):

    snomedct_3658006 = PermissibleValue(
        text="snomedct_3658006",
        description="Infancy",
        meaning=SNOMEDCT["3658006"])
    snomedct_713153009 = PermissibleValue(
        text="snomedct_713153009",
        description="Toddler",
        meaning=SNOMEDCT["713153009"])
    snomedct_255398004 = PermissibleValue(
        text="snomedct_255398004",
        description="Childhood",
        meaning=SNOMEDCT["255398004"])
    snomedct_263659003 = PermissibleValue(
        text="snomedct_263659003",
        description="Adolescence",
        meaning=SNOMEDCT["263659003"])
    snomedct_41847000 = PermissibleValue(
        text="snomedct_41847000",
        description="Adulthood",
        meaning=SNOMEDCT["41847000"])
    snomedct_303112003 = PermissibleValue(
        text="snomedct_303112003",
        description="Fetal period",
        meaning=SNOMEDCT["303112003"])
    snomedct_419099009 = PermissibleValue(
        text="snomedct_419099009",
        description="Dead",
        meaning=SNOMEDCT["419099009"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="AgeCategory",
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

class ICD10CM(EnumDefinitionImpl):  # noqa: F811
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

slots.patient_status_date = Slot(uri=RARELINK.patient_status_date, name="patient_status_date", curie=RARELINK.curie('patient_status_date'),
                   model_uri=RARELINK.patient_status_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomedct_278844005 = Slot(uri=RARELINK.snomedct_278844005, name="snomedct_278844005", curie=RARELINK.curie('snomedct_278844005'),
                   model_uri=RARELINK.snomedct_278844005, domain=None, range=Optional[Union[str, "ClinicalVitalStatus"]])

slots.snomedct_398299004 = Slot(uri=RARELINK.snomedct_398299004, name="snomedct_398299004", curie=RARELINK.curie('snomedct_398299004'),
                   model_uri=RARELINK.snomedct_398299004, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_184305005 = Slot(uri=RARELINK.snomedct_184305005, name="snomedct_184305005", curie=RARELINK.curie('snomedct_184305005'),
                   model_uri=RARELINK.snomedct_184305005, domain=None, range=Optional[str])

slots.snomedct_105727008 = Slot(uri=RARELINK.snomedct_105727008, name="snomedct_105727008", curie=RARELINK.curie('snomedct_105727008'),
                   model_uri=RARELINK.snomedct_105727008, domain=None, range=Optional[Union[str, "AgeCategory"]])

slots.snomedct_412726003 = Slot(uri=RARELINK.snomedct_412726003, name="snomedct_412726003", curie=RARELINK.curie('snomedct_412726003'),
                   model_uri=RARELINK.snomedct_412726003, domain=None, range=Optional[str])

slots.snomedct_723663001 = Slot(uri=RARELINK.snomedct_723663001, name="snomedct_723663001", curie=RARELINK.curie('snomedct_723663001'),
                   model_uri=RARELINK.snomedct_723663001, domain=None, range=Optional[Union[bool, Bool]])

slots.rarelink_3_patient_status_complete = Slot(uri=RARELINK.rarelink_3_patient_status_complete, name="rarelink_3_patient_status_complete", curie=RARELINK.curie('rarelink_3_patient_status_complete'),
                   model_uri=RARELINK.rarelink_3_patient_status_complete, domain=None, range=str)

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
