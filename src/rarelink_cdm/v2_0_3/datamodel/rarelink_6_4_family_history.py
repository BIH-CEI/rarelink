# Auto generated from rarelink_6_4_family_history.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T16:00:36
# Schema: rarelink_6_4_family_history
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_6_4_family_history.yaml
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
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None


# Namespaces
HL7FHIR = CurieNamespace('HL7FHIR', 'http://hl7.org/fhir/')
ICD10CM = CurieNamespace('ICD10CM', 'http://hl7.org/fhir/sid/icd-10-cm')
LOINC = CurieNamespace('LOINC', 'https://loinc.org/')
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
class FamilyHistory(YAMLRoot):
    """
    Captures the family history of the individual, detailing relationships, consanguinity, and specific family member
    details like diseases, age, sex, and cause of death.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["FamilyHistory"]
    class_class_curie: ClassVar[str] = "rarelink:FamilyHistory"
    class_name: ClassVar[str] = "FamilyHistory"
    class_model_uri: ClassVar[URIRef] = RARELINK.FamilyHistory

    family_history_pseudonym: Optional[str] = None
    snomedct_64245008: Optional[str] = None
    snomedct_408732007: Optional[str] = None
    snomedct_842009: Optional[str] = None
    snomedct_444018008: Optional[str] = None
    hl7fhir_fmh_status: Optional[str] = None
    loinc_54123_5: Optional[str] = None
    loinc_54141_7: Optional[int] = None
    loinc_54124_3: Optional[Union[str, XSDDate]] = None
    snomedct_740604001: Optional[str] = None
    loinc_54112_8: Optional[str] = None
    loinc_92662_6: Optional[int] = None
    loinc_75315_2: Optional[str] = None
    rarelink_6_4_family_history_complete: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.family_history_pseudonym is not None and not isinstance(self.family_history_pseudonym, str):
            self.family_history_pseudonym = str(self.family_history_pseudonym)

        if self.snomedct_64245008 is not None and not isinstance(self.snomedct_64245008, str):
            self.snomedct_64245008 = str(self.snomedct_64245008)

        if self.snomedct_408732007 is not None and not isinstance(self.snomedct_408732007, str):
            self.snomedct_408732007 = str(self.snomedct_408732007)

        if self.snomedct_842009 is not None and not isinstance(self.snomedct_842009, str):
            self.snomedct_842009 = str(self.snomedct_842009)

        if self.snomedct_444018008 is not None and not isinstance(self.snomedct_444018008, str):
            self.snomedct_444018008 = str(self.snomedct_444018008)

        if self.hl7fhir_fmh_status is not None and not isinstance(self.hl7fhir_fmh_status, str):
            self.hl7fhir_fmh_status = str(self.hl7fhir_fmh_status)

        if self.loinc_54123_5 is not None and not isinstance(self.loinc_54123_5, str):
            self.loinc_54123_5 = str(self.loinc_54123_5)

        if self.loinc_54141_7 is not None and not isinstance(self.loinc_54141_7, int):
            self.loinc_54141_7 = int(self.loinc_54141_7)

        if self.loinc_54124_3 is not None and not isinstance(self.loinc_54124_3, XSDDate):
            self.loinc_54124_3 = XSDDate(self.loinc_54124_3)

        if self.snomedct_740604001 is not None and not isinstance(self.snomedct_740604001, str):
            self.snomedct_740604001 = str(self.snomedct_740604001)

        if self.loinc_54112_8 is not None and not isinstance(self.loinc_54112_8, str):
            self.loinc_54112_8 = str(self.loinc_54112_8)

        if self.loinc_92662_6 is not None and not isinstance(self.loinc_92662_6, int):
            self.loinc_92662_6 = int(self.loinc_92662_6)

        if self.loinc_75315_2 is not None and not isinstance(self.loinc_75315_2, str):
            self.loinc_75315_2 = str(self.loinc_75315_2)

        if self.rarelink_6_4_family_history_complete is not None and not isinstance(self.rarelink_6_4_family_history_complete, str):
            self.rarelink_6_4_family_history_complete = str(self.rarelink_6_4_family_history_complete)

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
class PropositusStatus(EnumDefinitionImpl):
    """
    Indicates whether the individual is the first affected family member who seeks medical attention.
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
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="PropositusStatus",
        description="""Indicates whether the individual is the first affected family member who seeks medical attention.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class RelationshipToIndexCase(EnumDefinitionImpl):
    """
    Specifies the relationship of the individual to the index case.
    """
    snomedct_65656005 = PermissibleValue(
        text="snomedct_65656005",
        description="Natural mother",
        meaning=SNOMEDCT["65656005"])
    snomedct_9947008 = PermissibleValue(
        text="snomedct_9947008",
        description="Natural father",
        meaning=SNOMEDCT["9947008"])
    snomedct_83420006 = PermissibleValue(
        text="snomedct_83420006",
        description="Natural daughter",
        meaning=SNOMEDCT["83420006"])
    snomedct_113160008 = PermissibleValue(
        text="snomedct_113160008",
        description="Natural son",
        meaning=SNOMEDCT["113160008"])
    snomedct_60614009 = PermissibleValue(
        text="snomedct_60614009",
        description="Natural brother",
        meaning=SNOMEDCT["60614009"])
    snomedct_73678001 = PermissibleValue(
        text="snomedct_73678001",
        description="Natural sister",
        meaning=SNOMEDCT["73678001"])
    snomedct_11286003 = PermissibleValue(
        text="snomedct_11286003",
        description="Twin sibling",
        meaning=SNOMEDCT["11286003"])
    snomedct_45929001 = PermissibleValue(
        text="snomedct_45929001",
        description="Half-brother",
        meaning=SNOMEDCT["45929001"])
    snomedct_2272004 = PermissibleValue(
        text="snomedct_2272004",
        description="Half-sister",
        meaning=SNOMEDCT["2272004"])
    snomedct_62296006 = PermissibleValue(
        text="snomedct_62296006",
        description="Natural grandfather",
        meaning=SNOMEDCT["62296006"])
    snomedct_17945006 = PermissibleValue(
        text="snomedct_17945006",
        description="Natural grandmother",
        meaning=SNOMEDCT["17945006"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="RelationshipToIndexCase",
        description="""Specifies the relationship of the individual to the index case.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class FamilyRelationship(EnumDefinitionImpl):
    """
    Specifies the relationship of the selected family member to the patient.
    """
    snomedct_65656005 = PermissibleValue(
        text="snomedct_65656005",
        description="Natural mother",
        meaning=SNOMEDCT["65656005"])
    snomedct_9947008 = PermissibleValue(
        text="snomedct_9947008",
        description="Natural father",
        meaning=SNOMEDCT["9947008"])
    snomedct_83420006 = PermissibleValue(
        text="snomedct_83420006",
        description="Natural daughter",
        meaning=SNOMEDCT["83420006"])
    snomedct_113160008 = PermissibleValue(
        text="snomedct_113160008",
        description="Natural son",
        meaning=SNOMEDCT["113160008"])
    snomedct_60614009 = PermissibleValue(
        text="snomedct_60614009",
        description="Natural brother",
        meaning=SNOMEDCT["60614009"])
    snomedct_73678001 = PermissibleValue(
        text="snomedct_73678001",
        description="Natural sister",
        meaning=SNOMEDCT["73678001"])
    snomedct_11286003 = PermissibleValue(
        text="snomedct_11286003",
        description="Twin sibling",
        meaning=SNOMEDCT["11286003"])
    snomedct_45929001 = PermissibleValue(
        text="snomedct_45929001",
        description="Half-brother",
        meaning=SNOMEDCT["45929001"])
    snomedct_2272004 = PermissibleValue(
        text="snomedct_2272004",
        description="Half-sister",
        meaning=SNOMEDCT["2272004"])
    snomedct_62296006 = PermissibleValue(
        text="snomedct_62296006",
        description="Natural grandfather",
        meaning=SNOMEDCT["62296006"])
    snomedct_17945006 = PermissibleValue(
        text="snomedct_17945006",
        description="Natural grandmother",
        meaning=SNOMEDCT["17945006"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="FamilyRelationship",
        description="""Specifies the relationship of the selected family member to the patient.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class FamilyRecordStatus(EnumDefinitionImpl):
    """
    Specifies the record’s status of the family history.
    """
    hl7fhir_partial = PermissibleValue(
        text="hl7fhir_partial",
        description="Partial",
        meaning=HL7FHIR["partial"])
    hl7fhir_completed = PermissibleValue(
        text="hl7fhir_completed",
        description="Completed",
        meaning=HL7FHIR["completed"])

    _defn = EnumDefinition(
        name="FamilyRecordStatus",
        description="""Specifies the record’s status of the family history.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))
        setattr(cls, "hl7fhir_health-unknown",
            PermissibleValue(
                text="hl7fhir_health-unknown",
                description="Health Unknown",
                meaning=HL7FHIR["health-unknown"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class FamilyMemberSex(EnumDefinitionImpl):
    """
    Specifies the sex (or gender) of the specific family member.
    """
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
        name="FamilyMemberSex",
        description="""Specifies the sex (or gender) of the specific family member.""",
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

class LOINC(EnumDefinitionImpl):  # noqa: F811
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

slots.family_history_pseudonym = Slot(uri=RARELINK.family_history_pseudonym, name="family_history_pseudonym", curie=RARELINK.curie('family_history_pseudonym'),
                   model_uri=RARELINK.family_history_pseudonym, domain=None, range=Optional[str])

slots.snomedct_64245008 = Slot(uri=RARELINK.snomedct_64245008, name="snomedct_64245008", curie=RARELINK.curie('snomedct_64245008'),
                   model_uri=RARELINK.snomedct_64245008, domain=None, range=Optional[str])

slots.snomedct_408732007 = Slot(uri=RARELINK.snomedct_408732007, name="snomedct_408732007", curie=RARELINK.curie('snomedct_408732007'),
                   model_uri=RARELINK.snomedct_408732007, domain=None, range=Optional[str])

slots.snomedct_842009 = Slot(uri=RARELINK.snomedct_842009, name="snomedct_842009", curie=RARELINK.curie('snomedct_842009'),
                   model_uri=RARELINK.snomedct_842009, domain=None, range=Optional[str])

slots.snomedct_444018008 = Slot(uri=RARELINK.snomedct_444018008, name="snomedct_444018008", curie=RARELINK.curie('snomedct_444018008'),
                   model_uri=RARELINK.snomedct_444018008, domain=None, range=Optional[str])

slots.hl7fhir_fmh_status = Slot(uri=RARELINK.hl7fhir_fmh_status, name="hl7fhir_fmh_status", curie=RARELINK.curie('hl7fhir_fmh_status'),
                   model_uri=RARELINK.hl7fhir_fmh_status, domain=None, range=Optional[str])

slots.loinc_54123_5 = Slot(uri=RARELINK.loinc_54123_5, name="loinc_54123_5", curie=RARELINK.curie('loinc_54123_5'),
                   model_uri=RARELINK.loinc_54123_5, domain=None, range=Optional[str])

slots.loinc_54141_7 = Slot(uri=RARELINK.loinc_54141_7, name="loinc_54141_7", curie=RARELINK.curie('loinc_54141_7'),
                   model_uri=RARELINK.loinc_54141_7, domain=None, range=Optional[int])

slots.loinc_54124_3 = Slot(uri=RARELINK.loinc_54124_3, name="loinc_54124_3", curie=RARELINK.curie('loinc_54124_3'),
                   model_uri=RARELINK.loinc_54124_3, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomedct_740604001 = Slot(uri=RARELINK.snomedct_740604001, name="snomedct_740604001", curie=RARELINK.curie('snomedct_740604001'),
                   model_uri=RARELINK.snomedct_740604001, domain=None, range=Optional[str])

slots.loinc_54112_8 = Slot(uri=RARELINK.loinc_54112_8, name="loinc_54112_8", curie=RARELINK.curie('loinc_54112_8'),
                   model_uri=RARELINK.loinc_54112_8, domain=None, range=Optional[str])

slots.loinc_92662_6 = Slot(uri=RARELINK.loinc_92662_6, name="loinc_92662_6", curie=RARELINK.curie('loinc_92662_6'),
                   model_uri=RARELINK.loinc_92662_6, domain=None, range=Optional[int])

slots.loinc_75315_2 = Slot(uri=RARELINK.loinc_75315_2, name="loinc_75315_2", curie=RARELINK.curie('loinc_75315_2'),
                   model_uri=RARELINK.loinc_75315_2, domain=None, range=Optional[str])

slots.rarelink_6_4_family_history_complete = Slot(uri=RARELINK.rarelink_6_4_family_history_complete, name="rarelink_6_4_family_history_complete", curie=RARELINK.curie('rarelink_6_4_family_history_complete'),
                   model_uri=RARELINK.rarelink_6_4_family_history_complete, domain=None, range=Optional[str])

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
