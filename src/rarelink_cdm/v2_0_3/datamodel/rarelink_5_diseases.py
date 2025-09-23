# Auto generated from rarelink_5_disease.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:58:17
# Schema: rarelink_5_disease
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_5_disease.yaml
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
ICD10CM = CurieNamespace('ICD10CM', 'http://hl7.org/fhir/sid/icd-10-cm')
ICD11 = CurieNamespace('ICD11', 'https://id.who.int/icd/release/11/')
MONDO = CurieNamespace('MONDO', 'https://purl.obolibrary.org/obo/MONDO_')
OMIM = CurieNamespace('OMIM', 'https://omim.org/entry/')
ORDO = CurieNamespace('ORDO', 'http://www.orpha.net/ORDO/')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/sct')
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
class Disease(YAMLRoot):
    """
    Captures details of diseases encoded using various terminologies and provides relevant metadata such as age at
    onset, verification status, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["Disease"]
    class_class_curie: ClassVar[str] = "rarelink:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = RARELINK.Disease

    disease_coding: Union[str, "DiseaseCodeSystems"] = None
    loinc_99498_8: Union[str, "VerificationStatus"] = None
    rarelink_5_disease_complete: str = None
    snomedct_64572001_mondo: Optional[str] = None
    snomedct_64572001_ordo: Optional[str] = None
    snomedct_64572001_icd10cm: Optional[str] = None
    snomedct_64572001_icd11: Optional[str] = None
    snomedct_64572001_omim_p: Optional[str] = None
    snomedct_424850005: Optional[Union[str, "AgeAtOnset"]] = None
    snomedct_298059007: Optional[Union[str, UnionDateString]] = None
    snomedct_423493009: Optional[Union[str, "AgeAtDiagnosis"]] = None
    snomedct_432213005: Optional[Union[str, UnionDateString]] = None
    snomedct_363698007: Optional[str] = None
    snomedct_263493007: Optional[Union[str, "ClinicalStatus"]] = None
    snomedct_246112005: Optional[Union[str, "DiseaseSeverity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.disease_coding):
            self.MissingRequiredField("disease_coding")
        if not isinstance(self.disease_coding, DiseaseCodeSystems):
            self.disease_coding = DiseaseCodeSystems(self.disease_coding)

        if self._is_empty(self.loinc_99498_8):
            self.MissingRequiredField("loinc_99498_8")
        if not isinstance(self.loinc_99498_8, VerificationStatus):
            self.loinc_99498_8 = VerificationStatus(self.loinc_99498_8)

        if self._is_empty(self.rarelink_5_disease_complete):
            self.MissingRequiredField("rarelink_5_disease_complete")
        if not isinstance(self.rarelink_5_disease_complete, str):
            self.rarelink_5_disease_complete = str(self.rarelink_5_disease_complete)

        if self.snomedct_64572001_mondo is not None and not isinstance(self.snomedct_64572001_mondo, str):
            self.snomedct_64572001_mondo = str(self.snomedct_64572001_mondo)

        if self.snomedct_64572001_ordo is not None and not isinstance(self.snomedct_64572001_ordo, str):
            self.snomedct_64572001_ordo = str(self.snomedct_64572001_ordo)

        if self.snomedct_64572001_icd10cm is not None and not isinstance(self.snomedct_64572001_icd10cm, str):
            self.snomedct_64572001_icd10cm = str(self.snomedct_64572001_icd10cm)

        if self.snomedct_64572001_icd11 is not None and not isinstance(self.snomedct_64572001_icd11, str):
            self.snomedct_64572001_icd11 = str(self.snomedct_64572001_icd11)

        if self.snomedct_64572001_omim_p is not None and not isinstance(self.snomedct_64572001_omim_p, str):
            self.snomedct_64572001_omim_p = str(self.snomedct_64572001_omim_p)

        if self.snomedct_424850005 is not None and not isinstance(self.snomedct_424850005, AgeAtOnset):
            self.snomedct_424850005 = AgeAtOnset(self.snomedct_424850005)

        if self.snomedct_298059007 is not None and not isinstance(self.snomedct_298059007, UnionDateString):
            self.snomedct_298059007 = UnionDateString(self.snomedct_298059007)

        if self.snomedct_423493009 is not None and not isinstance(self.snomedct_423493009, AgeAtDiagnosis):
            self.snomedct_423493009 = AgeAtDiagnosis(self.snomedct_423493009)

        if self.snomedct_432213005 is not None and not isinstance(self.snomedct_432213005, UnionDateString):
            self.snomedct_432213005 = UnionDateString(self.snomedct_432213005)

        if self.snomedct_363698007 is not None and not isinstance(self.snomedct_363698007, str):
            self.snomedct_363698007 = str(self.snomedct_363698007)

        if self.snomedct_263493007 is not None and not isinstance(self.snomedct_263493007, ClinicalStatus):
            self.snomedct_263493007 = ClinicalStatus(self.snomedct_263493007)

        if self.snomedct_246112005 is not None and not isinstance(self.snomedct_246112005, DiseaseSeverity):
            self.snomedct_246112005 = DiseaseSeverity(self.snomedct_246112005)

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
class DiseaseCodeSystems(EnumDefinitionImpl):

    mondo = PermissibleValue(
        text="mondo",
        description="MONDO",
        meaning=RARELINK["MONDO"])
    ordo = PermissibleValue(
        text="ordo",
        description="ORDO",
        meaning=RARELINK["ORDO"])
    icd10cm = PermissibleValue(
        text="icd10cm",
        description="ICD-10-CM",
        meaning=RARELINK["ICD10CM"])
    icd11 = PermissibleValue(
        text="icd11",
        description="ICD-11",
        meaning=RARELINK["ICD11"])
    omim = PermissibleValue(
        text="omim",
        description="OMIM",
        meaning=RARELINK["OMIM"])

    _defn = EnumDefinition(
        name="DiseaseCodeSystems",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class VerificationStatus(EnumDefinitionImpl):

    hl7fhir_unconfirmed = PermissibleValue(
        text="hl7fhir_unconfirmed",
        description="Unconfirmed",
        meaning=HL7FHIR["unconfirmed"])
    hl7fhir_provisional = PermissibleValue(
        text="hl7fhir_provisional",
        description="Provisional",
        meaning=HL7FHIR["provisional"])
    hl7fhir_differential = PermissibleValue(
        text="hl7fhir_differential",
        description="Differential",
        meaning=HL7FHIR["differential"])
    hl7fhir_confirmed = PermissibleValue(
        text="hl7fhir_confirmed",
        description="Confirmed",
        meaning=HL7FHIR["confirmed"])
    hl7fhir_refuted = PermissibleValue(
        text="hl7fhir_refuted",
        description="Refuted",
        meaning=HL7FHIR["refuted"])

    _defn = EnumDefinition(
        name="VerificationStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class AgeAtOnset(EnumDefinitionImpl):

    snomedct_118189007 = PermissibleValue(
        text="snomedct_118189007",
        description="Prenatal",
        meaning=SNOMEDCT["118189007"])
    snomedct_3950001 = PermissibleValue(
        text="snomedct_3950001",
        description="Birth",
        meaning=SNOMEDCT["3950001"])
    snomedct_410672004 = PermissibleValue(
        text="snomedct_410672004",
        description="Date",
        meaning=SNOMEDCT["410672004"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="AgeAtOnset",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class AgeAtDiagnosis(EnumDefinitionImpl):

    snomedct_118189007 = PermissibleValue(
        text="snomedct_118189007",
        description="Prenatal",
        meaning=SNOMEDCT["118189007"])
    snomedct_3950001 = PermissibleValue(
        text="snomedct_3950001",
        description="Birth",
        meaning=SNOMEDCT["3950001"])
    snomedct_410672004 = PermissibleValue(
        text="snomedct_410672004",
        description="Date",
        meaning=SNOMEDCT["410672004"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="AgeAtDiagnosis",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class ClinicalStatus(EnumDefinitionImpl):

    hl7fhir_active = PermissibleValue(
        text="hl7fhir_active",
        description="Active",
        meaning=HL7FHIR["active"])
    hl7fhir_recurrence = PermissibleValue(
        text="hl7fhir_recurrence",
        description="Recurrence",
        meaning=HL7FHIR["recurrence"])
    hl7fhir_relapse = PermissibleValue(
        text="hl7fhir_relapse",
        description="Relapse",
        meaning=HL7FHIR["relapse"])
    hl7fhir_inactive = PermissibleValue(
        text="hl7fhir_inactive",
        description="Inactive",
        meaning=HL7FHIR["inactive"])
    hl7fhir_remission = PermissibleValue(
        text="hl7fhir_remission",
        description="Remission",
        meaning=HL7FHIR["remission"])
    hl7fhir_resolved = PermissibleValue(
        text="hl7fhir_resolved",
        description="Resolved",
        meaning=HL7FHIR["resolved"])

    _defn = EnumDefinition(
        name="ClinicalStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class DiseaseSeverity(EnumDefinitionImpl):

    snomedct_24484000 = PermissibleValue(
        text="snomedct_24484000",
        description="Severe",
        meaning=SNOMEDCT["24484000"])
    snomedct_6736007 = PermissibleValue(
        text="snomedct_6736007",
        description="Moderate",
        meaning=SNOMEDCT["6736007"])
    snomedct_255604002 = PermissibleValue(
        text="snomedct_255604002",
        description="Mild",
        meaning=SNOMEDCT["255604002"])

    _defn = EnumDefinition(
        name="DiseaseSeverity",
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

slots.disease_coding = Slot(uri=RARELINK.disease_coding, name="disease_coding", curie=RARELINK.curie('disease_coding'),
                   model_uri=RARELINK.disease_coding, domain=None, range=Union[str, "DiseaseCodeSystems"])

slots.snomedct_64572001_mondo = Slot(uri=RARELINK.snomedct_64572001_mondo, name="snomedct_64572001_mondo", curie=RARELINK.curie('snomedct_64572001_mondo'),
                   model_uri=RARELINK.snomedct_64572001_mondo, domain=None, range=Optional[str])

slots.snomedct_64572001_ordo = Slot(uri=RARELINK.snomedct_64572001_ordo, name="snomedct_64572001_ordo", curie=RARELINK.curie('snomedct_64572001_ordo'),
                   model_uri=RARELINK.snomedct_64572001_ordo, domain=None, range=Optional[str])

slots.snomedct_64572001_icd10cm = Slot(uri=RARELINK.snomedct_64572001_icd10cm, name="snomedct_64572001_icd10cm", curie=RARELINK.curie('snomedct_64572001_icd10cm'),
                   model_uri=RARELINK.snomedct_64572001_icd10cm, domain=None, range=Optional[str])

slots.snomedct_64572001_icd11 = Slot(uri=RARELINK.snomedct_64572001_icd11, name="snomedct_64572001_icd11", curie=RARELINK.curie('snomedct_64572001_icd11'),
                   model_uri=RARELINK.snomedct_64572001_icd11, domain=None, range=Optional[str])

slots.snomedct_64572001_omim_p = Slot(uri=RARELINK.snomedct_64572001_omim_p, name="snomedct_64572001_omim_p", curie=RARELINK.curie('snomedct_64572001_omim_p'),
                   model_uri=RARELINK.snomedct_64572001_omim_p, domain=None, range=Optional[str])

slots.loinc_99498_8 = Slot(uri=RARELINK.loinc_99498_8, name="loinc_99498_8", curie=RARELINK.curie('loinc_99498_8'),
                   model_uri=RARELINK.loinc_99498_8, domain=None, range=Union[str, "VerificationStatus"])

slots.snomedct_424850005 = Slot(uri=RARELINK.snomedct_424850005, name="snomedct_424850005", curie=RARELINK.curie('snomedct_424850005'),
                   model_uri=RARELINK.snomedct_424850005, domain=None, range=Optional[Union[str, "AgeAtOnset"]])

slots.snomedct_298059007 = Slot(uri=RARELINK.snomedct_298059007, name="snomedct_298059007", curie=RARELINK.curie('snomedct_298059007'),
                   model_uri=RARELINK.snomedct_298059007, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_423493009 = Slot(uri=RARELINK.snomedct_423493009, name="snomedct_423493009", curie=RARELINK.curie('snomedct_423493009'),
                   model_uri=RARELINK.snomedct_423493009, domain=None, range=Optional[Union[str, "AgeAtDiagnosis"]])

slots.snomedct_432213005 = Slot(uri=RARELINK.snomedct_432213005, name="snomedct_432213005", curie=RARELINK.curie('snomedct_432213005'),
                   model_uri=RARELINK.snomedct_432213005, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_363698007 = Slot(uri=RARELINK.snomedct_363698007, name="snomedct_363698007", curie=RARELINK.curie('snomedct_363698007'),
                   model_uri=RARELINK.snomedct_363698007, domain=None, range=Optional[str])

slots.snomedct_263493007 = Slot(uri=RARELINK.snomedct_263493007, name="snomedct_263493007", curie=RARELINK.curie('snomedct_263493007'),
                   model_uri=RARELINK.snomedct_263493007, domain=None, range=Optional[Union[str, "ClinicalStatus"]])

slots.snomedct_246112005 = Slot(uri=RARELINK.snomedct_246112005, name="snomedct_246112005", curie=RARELINK.curie('snomedct_246112005'),
                   model_uri=RARELINK.snomedct_246112005, domain=None, range=Optional[Union[str, "DiseaseSeverity"]])

slots.rarelink_5_disease_complete = Slot(uri=RARELINK.rarelink_5_disease_complete, name="rarelink_5_disease_complete", curie=RARELINK.curie('rarelink_5_disease_complete'),
                   model_uri=RARELINK.rarelink_5_disease_complete, domain=None, range=str)

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
