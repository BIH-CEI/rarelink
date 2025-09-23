# Auto generated from rarelink_2_personal_information.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:57:19
# Schema: rarelink_2_personal_information
#
# id: https://w3id.org/linkml/rarelink/personal_information
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Dict,
    Optional,
    List,
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
from rdflib import URIRef

from linkml_runtime.linkml_model.types import String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__

# Namespaces
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
class PersonalInformation(YAMLRoot):
    """
    The section Personal Information (2) of the RareLink CDM
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["PersonalInformation"]
    class_class_curie: ClassVar[str] = "rarelink:PersonalInformation"
    class_name: ClassVar[str] = "PersonalInformation"
    class_model_uri: ClassVar[URIRef] = RARELINK.PersonalInformation

    snomedct_184099003: Union[str, XSDDate] = None
    rarelink_2_personal_information_complete: str = None
    snomedct_281053000: Optional[Union[str, "SexAtBirth"]] = None
    snomedct_1296886006: Optional[Union[str, "KaryotypicSex"]] = None
    snomedct_263495000: Optional[Union[str, "GenderIdentity"]] = None
    snomedct_370159000: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomedct_184099003):
            self.MissingRequiredField("snomedct_184099003")
        if not isinstance(self.snomedct_184099003, XSDDate):
            self.snomedct_184099003 = XSDDate(self.snomedct_184099003)

        if self._is_empty(self.rarelink_2_personal_information_complete):
            self.MissingRequiredField("rarelink_2_personal_information_complete")
        if not isinstance(self.rarelink_2_personal_information_complete, str):
            self.rarelink_2_personal_information_complete = str(self.rarelink_2_personal_information_complete)

        if self.snomedct_281053000 is not None and not isinstance(self.snomedct_281053000, SexAtBirth):
            self.snomedct_281053000 = SexAtBirth(self.snomedct_281053000)

        if self.snomedct_1296886006 is not None and not isinstance(self.snomedct_1296886006, KaryotypicSex):
            self.snomedct_1296886006 = KaryotypicSex(self.snomedct_1296886006)

        if self.snomedct_263495000 is not None and not isinstance(self.snomedct_263495000, GenderIdentity):
            self.snomedct_263495000 = GenderIdentity(self.snomedct_263495000)

        if self.snomedct_370159000 is not None and not isinstance(self.snomedct_370159000, str):
            self.snomedct_370159000 = str(self.snomedct_370159000)

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
class SexAtBirth(EnumDefinitionImpl):

    snomedct_248152002 = PermissibleValue(
        text="snomedct_248152002",
        description="Female",
        meaning=SNOMEDCT["248152002"])
    snomedct_248153007 = PermissibleValue(
        text="snomedct_248153007",
        description="Male",
        meaning=SNOMEDCT["248153007"])
    snomedct_184115007 = PermissibleValue(
        text="snomedct_184115007",
        description="Patient sex unknown",
        meaning=SNOMEDCT["184115007"])
    snomedct_32570691000036108 = PermissibleValue(
        text="snomedct_32570691000036108",
        description="Intersex",
        meaning=SNOMEDCT["32570691000036108"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="SexAtBirth",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class KaryotypicSex(EnumDefinitionImpl):

    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])
    snomedct_734875008 = PermissibleValue(
        text="snomedct_734875008",
        description="XX",
        meaning=SNOMEDCT["734875008"])
    snomedct_734876009 = PermissibleValue(
        text="snomedct_734876009",
        description="XY",
        meaning=SNOMEDCT["734876009"])
    snomedct_80427008 = PermissibleValue(
        text="snomedct_80427008",
        description="X0",
        meaning=SNOMEDCT["80427008"])
    snomedct_65162001 = PermissibleValue(
        text="snomedct_65162001",
        description="XXY",
        meaning=SNOMEDCT["65162001"])
    snomedct_35111009 = PermissibleValue(
        text="snomedct_35111009",
        description="XXX",
        meaning=SNOMEDCT["35111009"])
    snomedct_403760006 = PermissibleValue(
        text="snomedct_403760006",
        description="XXYY",
        meaning=SNOMEDCT["403760006"])
    snomedct_78317008 = PermissibleValue(
        text="snomedct_78317008",
        description="XXXY",
        meaning=SNOMEDCT["78317008"])
    snomedct_10567003 = PermissibleValue(
        text="snomedct_10567003",
        description="XXXX",
        meaning=SNOMEDCT["10567003"])
    snomedct_48930007 = PermissibleValue(
        text="snomedct_48930007",
        description="XYY",
        meaning=SNOMEDCT["48930007"])
    snomedct_74964007 = PermissibleValue(
        text="snomedct_74964007",
        description="Other",
        meaning=SNOMEDCT["74964007"])

    _defn = EnumDefinition(
        name="KaryotypicSex",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class GenderIdentity(EnumDefinitionImpl):

    snomedct_446141000124107 = PermissibleValue(
        text="snomedct_446141000124107",
        description="Female gender identity",
        meaning=SNOMEDCT["446141000124107"])
    snomedct_446151000124109 = PermissibleValue(
        text="snomedct_446151000124109",
        description="Male gender identity",
        meaning=SNOMEDCT["446151000124109"])
    snomedct_394743007 = PermissibleValue(
        text="snomedct_394743007",
        description="Gender unknown",
        meaning=SNOMEDCT["394743007"])
    snomedct_33791000087105 = PermissibleValue(
        text="snomedct_33791000087105",
        description="Identifies as nonbinary gender",
        meaning=SNOMEDCT["33791000087105"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="GenderIdentity",
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

slots.snomedct_184099003 = Slot(uri=RARELINK.snomedct_184099003, name="snomedct_184099003", curie=RARELINK.curie('snomedct_184099003'),
                   model_uri=RARELINK.snomedct_184099003, domain=None, range=Union[str, XSDDate])

slots.snomedct_281053000 = Slot(uri=RARELINK.snomedct_281053000, name="snomedct_281053000", curie=RARELINK.curie('snomedct_281053000'),
                   model_uri=RARELINK.snomedct_281053000, domain=None, range=Optional[Union[str, "SexAtBirth"]])

slots.snomedct_1296886006 = Slot(uri=RARELINK.snomedct_1296886006, name="snomedct_1296886006", curie=RARELINK.curie('snomedct_1296886006'),
                   model_uri=RARELINK.snomedct_1296886006, domain=None, range=Optional[Union[str, "KaryotypicSex"]])

slots.snomedct_263495000 = Slot(uri=RARELINK.snomedct_263495000, name="snomedct_263495000", curie=RARELINK.curie('snomedct_263495000'),
                   model_uri=RARELINK.snomedct_263495000, domain=None, range=Optional[Union[str, "GenderIdentity"]])

slots.snomedct_370159000 = Slot(uri=RARELINK.snomedct_370159000, name="snomedct_370159000", curie=RARELINK.curie('snomedct_370159000'),
                   model_uri=RARELINK.snomedct_370159000, domain=None, range=Optional[str])

slots.rarelink_2_personal_information_complete = Slot(uri=RARELINK.rarelink_2_personal_information_complete, name="rarelink_2_personal_information_complete", curie=RARELINK.curie('rarelink_2_personal_information_complete'),
                   model_uri=RARELINK.rarelink_2_personal_information_complete, domain=None, range=str)

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
