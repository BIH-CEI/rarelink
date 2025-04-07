# Auto generated from form_12_lymph_func_ini.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-07T10:53:12
# Schema: lymphocyte_functionnk_cytotoxicity
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/limkml_schemas/form_lymphfunc_initial.yaml
# description: Initial lymphocyte function and NK cytotoxicity form capturing test timing and assay results.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LOINC = CurieNamespace('LOINC', 'http://loinc.org/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
CIEINR = CurieNamespace('cieinr', 'https://github.com/BIH-CEI/cieinr')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CIEINR


# Types
class UnionDateString(String):
    """ A field that allows both dates and empty strings. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "union_date_string"
    type_model_uri = CIEINR.UnionDateString


class AgeInYears(Integer):
    """ Age in completed years """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "age_in_years"
    type_model_uri = CIEINR.AgeInYears


class AgeInMonths(Integer):
    """ Age in completed months """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "age_in_months"
    type_model_uri = CIEINR.AgeInMonths


class Percent(Float):
    """ A percentage value """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "percent"
    type_model_uri = CIEINR.Percent


class IeiCode(String):
    """ A code for an Inborn Error of Immunity """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "iei_code"
    type_model_uri = CIEINR.IeiCode


class LabValue(Float):
    """ A laboratory measurement value, can be negative in some cases """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "lab_value"
    type_model_uri = CIEINR.LabValue


class PositiveLabValue(Float):
    """ A laboratory measurement value that cannot be negative """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "positive_lab_value"
    type_model_uri = CIEINR.PositiveLabValue


class NonNegativeInteger(Integer):
    """ An integer value that cannot be negative """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "non_negative_integer"
    type_model_uri = CIEINR.NonNegativeInteger


class TextOrNull(String):
    """ A text field that can be empty or null """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "text_or_null"
    type_model_uri = CIEINR.TextOrNull


class CodedValue(String):
    """ A coded value from a standardized terminology """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "coded_value"
    type_model_uri = CIEINR.CodedValue


class RedcapCheckbox(String):
    """ REDCap checkbox field (contains checked values as comma-separated list) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "redcap_checkbox"
    type_model_uri = CIEINR.RedcapCheckbox


class RedcapCompletionStatus(String):
    """ REDCap form completion status """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "redcap_completion_status"
    type_model_uri = CIEINR.RedcapCompletionStatus


class BooleanAsInteger(Integer):
    """ Boolean represented as 0 (false) or 1 (true) """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "boolean_as_integer"
    type_model_uri = CIEINR.BooleanAsInteger


# Class references



@dataclass(repr=False)
class LymphocyteFunction(YAMLRoot):
    """
    Initial lymphocyte function and NK cytotoxicity information including test timing and assay results.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["LymphocyteFunction"]
    class_class_curie: ClassVar[str] = "cieinr:LymphocyteFunction"
    class_name: ClassVar[str] = "LymphocyteFunction"
    class_model_uri: ClassVar[URIRef] = CIEINR.LymphocyteFunction

    lymphfunc_test: Optional[Union[str, "LymphfuncTestEnum"]] = None
    lymphfunc_date: Optional[Union[str, XSDDate]] = None
    lymphfunc_ncit_c88791: Optional[Union[str, "PHATestEnum"]] = None
    lymphfunc_ncit_c88791_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c74017: Optional[Union[str, "AntiCD3CD28TestEnum"]] = None
    lymphfunc_ncit_c74017_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c88774: Optional[Union[str, "ConATestEnum"]] = None
    lymphfunc_ncit_c88774_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c88789: Optional[Union[str, "PWMTestEnum"]] = None
    lymphfunc_ncit_c88789_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c17166: Optional[Union[str, "SpaTestEnum"]] = None
    lymphfunc_ncit_c17166_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c85185: Optional[Union[str, "TetanusTestEnum"]] = None
    lymphfunc_ncit_c85185_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c34541: Optional[Union[str, "DiphtheriaTestEnum"]] = None
    lymphfunc_ncit_c34541_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c77163: Optional[Union[str, "CandidaTestEnum"]] = None
    lymphfunc_ncit_c77163_val: Optional[Union[str, "AssayResultEnum"]] = None
    lymphfunc_ncit_c116203: Optional[Union[str, "NKCytotoxicityTestEnum"]] = None
    lymphfunc_ncit_c116203_val: Optional[Union[str, "AssayResultEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.lymphfunc_test is not None and not isinstance(self.lymphfunc_test, LymphfuncTestEnum):
            self.lymphfunc_test = LymphfuncTestEnum(self.lymphfunc_test)

        if self.lymphfunc_date is not None and not isinstance(self.lymphfunc_date, XSDDate):
            self.lymphfunc_date = XSDDate(self.lymphfunc_date)

        if self.lymphfunc_ncit_c88791 is not None and not isinstance(self.lymphfunc_ncit_c88791, PHATestEnum):
            self.lymphfunc_ncit_c88791 = PHATestEnum(self.lymphfunc_ncit_c88791)

        if self.lymphfunc_ncit_c88791_val is not None and not isinstance(self.lymphfunc_ncit_c88791_val, AssayResultEnum):
            self.lymphfunc_ncit_c88791_val = AssayResultEnum(self.lymphfunc_ncit_c88791_val)

        if self.lymphfunc_ncit_c74017 is not None and not isinstance(self.lymphfunc_ncit_c74017, AntiCD3CD28TestEnum):
            self.lymphfunc_ncit_c74017 = AntiCD3CD28TestEnum(self.lymphfunc_ncit_c74017)

        if self.lymphfunc_ncit_c74017_val is not None and not isinstance(self.lymphfunc_ncit_c74017_val, AssayResultEnum):
            self.lymphfunc_ncit_c74017_val = AssayResultEnum(self.lymphfunc_ncit_c74017_val)

        if self.lymphfunc_ncit_c88774 is not None and not isinstance(self.lymphfunc_ncit_c88774, ConATestEnum):
            self.lymphfunc_ncit_c88774 = ConATestEnum(self.lymphfunc_ncit_c88774)

        if self.lymphfunc_ncit_c88774_val is not None and not isinstance(self.lymphfunc_ncit_c88774_val, AssayResultEnum):
            self.lymphfunc_ncit_c88774_val = AssayResultEnum(self.lymphfunc_ncit_c88774_val)

        if self.lymphfunc_ncit_c88789 is not None and not isinstance(self.lymphfunc_ncit_c88789, PWMTestEnum):
            self.lymphfunc_ncit_c88789 = PWMTestEnum(self.lymphfunc_ncit_c88789)

        if self.lymphfunc_ncit_c88789_val is not None and not isinstance(self.lymphfunc_ncit_c88789_val, AssayResultEnum):
            self.lymphfunc_ncit_c88789_val = AssayResultEnum(self.lymphfunc_ncit_c88789_val)

        if self.lymphfunc_ncit_c17166 is not None and not isinstance(self.lymphfunc_ncit_c17166, SpaTestEnum):
            self.lymphfunc_ncit_c17166 = SpaTestEnum(self.lymphfunc_ncit_c17166)

        if self.lymphfunc_ncit_c17166_val is not None and not isinstance(self.lymphfunc_ncit_c17166_val, AssayResultEnum):
            self.lymphfunc_ncit_c17166_val = AssayResultEnum(self.lymphfunc_ncit_c17166_val)

        if self.lymphfunc_ncit_c85185 is not None and not isinstance(self.lymphfunc_ncit_c85185, TetanusTestEnum):
            self.lymphfunc_ncit_c85185 = TetanusTestEnum(self.lymphfunc_ncit_c85185)

        if self.lymphfunc_ncit_c85185_val is not None and not isinstance(self.lymphfunc_ncit_c85185_val, AssayResultEnum):
            self.lymphfunc_ncit_c85185_val = AssayResultEnum(self.lymphfunc_ncit_c85185_val)

        if self.lymphfunc_ncit_c34541 is not None and not isinstance(self.lymphfunc_ncit_c34541, DiphtheriaTestEnum):
            self.lymphfunc_ncit_c34541 = DiphtheriaTestEnum(self.lymphfunc_ncit_c34541)

        if self.lymphfunc_ncit_c34541_val is not None and not isinstance(self.lymphfunc_ncit_c34541_val, AssayResultEnum):
            self.lymphfunc_ncit_c34541_val = AssayResultEnum(self.lymphfunc_ncit_c34541_val)

        if self.lymphfunc_ncit_c77163 is not None and not isinstance(self.lymphfunc_ncit_c77163, CandidaTestEnum):
            self.lymphfunc_ncit_c77163 = CandidaTestEnum(self.lymphfunc_ncit_c77163)

        if self.lymphfunc_ncit_c77163_val is not None and not isinstance(self.lymphfunc_ncit_c77163_val, AssayResultEnum):
            self.lymphfunc_ncit_c77163_val = AssayResultEnum(self.lymphfunc_ncit_c77163_val)

        if self.lymphfunc_ncit_c116203 is not None and not isinstance(self.lymphfunc_ncit_c116203, NKCytotoxicityTestEnum):
            self.lymphfunc_ncit_c116203 = NKCytotoxicityTestEnum(self.lymphfunc_ncit_c116203)

        if self.lymphfunc_ncit_c116203_val is not None and not isinstance(self.lymphfunc_ncit_c116203_val, AssayResultEnum):
            self.lymphfunc_ncit_c116203_val = AssayResultEnum(self.lymphfunc_ncit_c116203_val)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystemsContainer(YAMLRoot):
    """
    A container class for all code systems used in CIEINR.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["CodeSystemsContainer"]
    class_class_curie: ClassVar[str] = "cieinr:CodeSystemsContainer"
    class_name: ClassVar[str] = "CodeSystemsContainer"
    class_model_uri: ClassVar[URIRef] = CIEINR.CodeSystemsContainer

    ncbi_taxon: Union[str, "NCBITaxon"] = None
    snomedct: Union[str, "SNOMEDCT"] = None
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
    bioportal: Union[str, "BIOPORTAL"] = None
    iuis: Union[str, "IUIS"] = None

# Enumerations
class LymphfuncTestEnum(EnumDefinitionImpl):
    """
    Options for lymphocyte function test timing.
    """
    ncit_c199317 = PermissibleValue(
        text="ncit_c199317",
        description="Test before the time of diagnosis (to remove)")
    ncit_c158810 = PermissibleValue(
        text="ncit_c158810",
        description="Test at time of Diagnosis (to remove)")
    ncit_c100059 = PermissibleValue(
        text="ncit_c100059",
        description="Test after diagnosis (to remove)")

    _defn = EnumDefinition(
        name="LymphfuncTestEnum",
        description="Options for lymphocyte function test timing.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="Before the time of diagnosis of IEI and initiation of any treatment, if available"))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="Most recent test"))

class PHATestEnum(EnumDefinitionImpl):
    """
    PHA (phytohemagglutinin) test.
    """
    ncit_c88791 = PermissibleValue(
        text="ncit_c88791",
        description="PHA (phytohemagglutinin)")

    _defn = EnumDefinition(
        name="PHATestEnum",
        description="PHA (phytohemagglutinin) test.",
    )

class AntiCD3CD28TestEnum(EnumDefinitionImpl):
    """
    Anti-CD3/CD28 Antibody test.
    """
    ncit_c74017 = PermissibleValue(
        text="ncit_c74017",
        description="Anti-CD3/CD28 Antibody")

    _defn = EnumDefinition(
        name="AntiCD3CD28TestEnum",
        description="Anti-CD3/CD28 Antibody test.",
    )

class ConATestEnum(EnumDefinitionImpl):
    """
    ConA (concanavalin A) test.
    """
    ncit_c88774 = PermissibleValue(
        text="ncit_c88774",
        description="ConA (concanavalin A)")

    _defn = EnumDefinition(
        name="ConATestEnum",
        description="ConA (concanavalin A) test.",
    )

class PWMTestEnum(EnumDefinitionImpl):
    """
    PWM (pokeweed mitogen) test.
    """
    ncit_c88789 = PermissibleValue(
        text="ncit_c88789",
        description="PWM (pokeweed mitogen)")

    _defn = EnumDefinition(
        name="PWMTestEnum",
        description="PWM (pokeweed mitogen) test.",
    )

class SpaTestEnum(EnumDefinitionImpl):
    """
    SpA (Staph Aureus Protein A) test.
    """
    ncit_c17166 = PermissibleValue(
        text="ncit_c17166",
        description="SpA (Staph Aureus Protein A)")

    _defn = EnumDefinition(
        name="SpaTestEnum",
        description="SpA (Staph Aureus Protein A) test.",
    )

class TetanusTestEnum(EnumDefinitionImpl):
    """
    Tetanus test.
    """
    ncit_c85185 = PermissibleValue(
        text="ncit_c85185",
        description="Tetanus")

    _defn = EnumDefinition(
        name="TetanusTestEnum",
        description="Tetanus test.",
    )

class DiphtheriaTestEnum(EnumDefinitionImpl):
    """
    Diphtheria test.
    """
    ncit_c34541 = PermissibleValue(
        text="ncit_c34541",
        description="Diphtheria")

    _defn = EnumDefinition(
        name="DiphtheriaTestEnum",
        description="Diphtheria test.",
    )

class CandidaTestEnum(EnumDefinitionImpl):
    """
    Candida test.
    """
    ncit_c77163 = PermissibleValue(
        text="ncit_c77163",
        description="Candida")

    _defn = EnumDefinition(
        name="CandidaTestEnum",
        description="Candida test.",
    )

class NKCytotoxicityTestEnum(EnumDefinitionImpl):
    """
    NK cell Cytotoxicity test.
    """
    ncit_c116203 = PermissibleValue(
        text="ncit_c116203",
        description="NK cell Cytotoxicity")

    _defn = EnumDefinition(
        name="NKCytotoxicityTestEnum",
        description="NK cell Cytotoxicity test.",
    )

class AssayResultEnum(EnumDefinitionImpl):
    """
    Possible assay results.
    """
    ncit_c48190 = PermissibleValue(
        text="ncit_c48190",
        description="Absent")
    ncit_c54722 = PermissibleValue(
        text="ncit_c54722",
        description="Low")
    ncit_c14165 = PermissibleValue(
        text="ncit_c14165",
        description="Normal")

    _defn = EnumDefinition(
        name="AssayResultEnum",
        description="Possible assay results.",
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
        code_set_version="2024-09-01",
    )

class MONDO(EnumDefinitionImpl):
    """
    Monarch Disease Ontology
    """
    _defn = EnumDefinition(
        name="MONDO",
        description="Monarch Disease Ontology",
        code_set_version="2024-09-03",
    )

class HP(EnumDefinitionImpl):
    """
    Human Phenotype Ontology
    """
    _defn = EnumDefinition(
        name="HP",
        description="Human Phenotype Ontology",
        code_set_version="2024-08-13",
    )

class LOINC(EnumDefinitionImpl):
    """
    Logical Observation Identifiers Names and Codes
    """
    _defn = EnumDefinition(
        name="LOINC",
        description="Logical Observation Identifiers Names and Codes",
        code_set_version="2.78",
    )

class OMIM(EnumDefinitionImpl):
    """
    Online Mendelian Inheritance
    """
    _defn = EnumDefinition(
        name="OMIM",
        description="Online Mendelian Inheritance",
        code_set_version="2024-09-12",
    )

class ORPHA(EnumDefinitionImpl):
    """
    Orphanet Rare Disease Ontology
    """
    _defn = EnumDefinition(
        name="ORPHA",
        description="Orphanet Rare Disease Ontology",
        code_set_version="2024-09-12",
    )

class NCIT(EnumDefinitionImpl):
    """
    NCI Thesaurus OBO Edition
    """
    _defn = EnumDefinition(
        name="NCIT",
        description="NCI Thesaurus OBO Edition",
        code_set_version="24.04e",
    )

class UO(EnumDefinitionImpl):
    """
    Units of Measurement Ontology
    """
    _defn = EnumDefinition(
        name="UO",
        description="Units of Measurement Ontology",
        code_set_version="2024-09-12",
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
        code_set_version="2024-09-01",
    )

class ICD10CM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, Clinical Modification
    """
    _defn = EnumDefinition(
        name="ICD10CM",
        description="International Classification of Diseases, Tenth Revision, Clinical Modification",
        code_set_version="2024-09-01",
    )

class BIOPORTAL(EnumDefinitionImpl):
    """
    BioPortal ontology repository
    """
    _defn = EnumDefinition(
        name="BIOPORTAL",
        description="BioPortal ontology repository",
        code_set_version="2024-09-01",
    )

class IUIS(EnumDefinitionImpl):
    """
    International Union of Immunological Societies Classification
    """
    _defn = EnumDefinition(
        name="IUIS",
        description="International Union of Immunological Societies Classification",
        code_set_version="2024",
    )

# Slots
class slots:
    pass

slots.lymphfunc_test = Slot(uri=CIEINR.lymphfunc_test, name="lymphfunc_test", curie=CIEINR.curie('lymphfunc_test'),
                   model_uri=CIEINR.lymphfunc_test, domain=None, range=Optional[Union[str, "LymphfuncTestEnum"]])

slots.lymphfunc_date = Slot(uri=CIEINR.lymphfunc_date, name="lymphfunc_date", curie=CIEINR.curie('lymphfunc_date'),
                   model_uri=CIEINR.lymphfunc_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.lymphfunc_ncit_c88791 = Slot(uri=CIEINR.lymphfunc_ncit_c88791, name="lymphfunc_ncit_c88791", curie=CIEINR.curie('lymphfunc_ncit_c88791'),
                   model_uri=CIEINR.lymphfunc_ncit_c88791, domain=None, range=Optional[Union[str, "PHATestEnum"]])

slots.lymphfunc_ncit_c88791_val = Slot(uri=CIEINR.lymphfunc_ncit_c88791_val, name="lymphfunc_ncit_c88791_val", curie=CIEINR.curie('lymphfunc_ncit_c88791_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c88791_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c74017 = Slot(uri=CIEINR.lymphfunc_ncit_c74017, name="lymphfunc_ncit_c74017", curie=CIEINR.curie('lymphfunc_ncit_c74017'),
                   model_uri=CIEINR.lymphfunc_ncit_c74017, domain=None, range=Optional[Union[str, "AntiCD3CD28TestEnum"]])

slots.lymphfunc_ncit_c74017_val = Slot(uri=CIEINR.lymphfunc_ncit_c74017_val, name="lymphfunc_ncit_c74017_val", curie=CIEINR.curie('lymphfunc_ncit_c74017_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c74017_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c88774 = Slot(uri=CIEINR.lymphfunc_ncit_c88774, name="lymphfunc_ncit_c88774", curie=CIEINR.curie('lymphfunc_ncit_c88774'),
                   model_uri=CIEINR.lymphfunc_ncit_c88774, domain=None, range=Optional[Union[str, "ConATestEnum"]])

slots.lymphfunc_ncit_c88774_val = Slot(uri=CIEINR.lymphfunc_ncit_c88774_val, name="lymphfunc_ncit_c88774_val", curie=CIEINR.curie('lymphfunc_ncit_c88774_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c88774_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c88789 = Slot(uri=CIEINR.lymphfunc_ncit_c88789, name="lymphfunc_ncit_c88789", curie=CIEINR.curie('lymphfunc_ncit_c88789'),
                   model_uri=CIEINR.lymphfunc_ncit_c88789, domain=None, range=Optional[Union[str, "PWMTestEnum"]])

slots.lymphfunc_ncit_c88789_val = Slot(uri=CIEINR.lymphfunc_ncit_c88789_val, name="lymphfunc_ncit_c88789_val", curie=CIEINR.curie('lymphfunc_ncit_c88789_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c88789_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c17166 = Slot(uri=CIEINR.lymphfunc_ncit_c17166, name="lymphfunc_ncit_c17166", curie=CIEINR.curie('lymphfunc_ncit_c17166'),
                   model_uri=CIEINR.lymphfunc_ncit_c17166, domain=None, range=Optional[Union[str, "SpaTestEnum"]])

slots.lymphfunc_ncit_c17166_val = Slot(uri=CIEINR.lymphfunc_ncit_c17166_val, name="lymphfunc_ncit_c17166_val", curie=CIEINR.curie('lymphfunc_ncit_c17166_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c17166_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c85185 = Slot(uri=CIEINR.lymphfunc_ncit_c85185, name="lymphfunc_ncit_c85185", curie=CIEINR.curie('lymphfunc_ncit_c85185'),
                   model_uri=CIEINR.lymphfunc_ncit_c85185, domain=None, range=Optional[Union[str, "TetanusTestEnum"]])

slots.lymphfunc_ncit_c85185_val = Slot(uri=CIEINR.lymphfunc_ncit_c85185_val, name="lymphfunc_ncit_c85185_val", curie=CIEINR.curie('lymphfunc_ncit_c85185_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c85185_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c34541 = Slot(uri=CIEINR.lymphfunc_ncit_c34541, name="lymphfunc_ncit_c34541", curie=CIEINR.curie('lymphfunc_ncit_c34541'),
                   model_uri=CIEINR.lymphfunc_ncit_c34541, domain=None, range=Optional[Union[str, "DiphtheriaTestEnum"]])

slots.lymphfunc_ncit_c34541_val = Slot(uri=CIEINR.lymphfunc_ncit_c34541_val, name="lymphfunc_ncit_c34541_val", curie=CIEINR.curie('lymphfunc_ncit_c34541_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c34541_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c77163 = Slot(uri=CIEINR.lymphfunc_ncit_c77163, name="lymphfunc_ncit_c77163", curie=CIEINR.curie('lymphfunc_ncit_c77163'),
                   model_uri=CIEINR.lymphfunc_ncit_c77163, domain=None, range=Optional[Union[str, "CandidaTestEnum"]])

slots.lymphfunc_ncit_c77163_val = Slot(uri=CIEINR.lymphfunc_ncit_c77163_val, name="lymphfunc_ncit_c77163_val", curie=CIEINR.curie('lymphfunc_ncit_c77163_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c77163_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.lymphfunc_ncit_c116203 = Slot(uri=CIEINR.lymphfunc_ncit_c116203, name="lymphfunc_ncit_c116203", curie=CIEINR.curie('lymphfunc_ncit_c116203'),
                   model_uri=CIEINR.lymphfunc_ncit_c116203, domain=None, range=Optional[Union[str, "NKCytotoxicityTestEnum"]])

slots.lymphfunc_ncit_c116203_val = Slot(uri=CIEINR.lymphfunc_ncit_c116203_val, name="lymphfunc_ncit_c116203_val", curie=CIEINR.curie('lymphfunc_ncit_c116203_val'),
                   model_uri=CIEINR.lymphfunc_ncit_c116203_val, domain=None, range=Optional[Union[str, "AssayResultEnum"]])

slots.codeSystemsContainer__ncbi_taxon = Slot(uri=CIEINR.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=CIEINR.curie('ncbi_taxon'),
                   model_uri=CIEINR.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

slots.codeSystemsContainer__snomedct = Slot(uri=CIEINR.snomedct, name="codeSystemsContainer__snomedct", curie=CIEINR.curie('snomedct'),
                   model_uri=CIEINR.codeSystemsContainer__snomedct, domain=None, range=Union[str, "SNOMEDCT"])

slots.codeSystemsContainer__mondo = Slot(uri=CIEINR.mondo, name="codeSystemsContainer__mondo", curie=CIEINR.curie('mondo'),
                   model_uri=CIEINR.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

slots.codeSystemsContainer__hpo = Slot(uri=CIEINR.hpo, name="codeSystemsContainer__hpo", curie=CIEINR.curie('hpo'),
                   model_uri=CIEINR.codeSystemsContainer__hpo, domain=None, range=Union[str, "HP"])

slots.codeSystemsContainer__loinc = Slot(uri=CIEINR.loinc, name="codeSystemsContainer__loinc", curie=CIEINR.curie('loinc'),
                   model_uri=CIEINR.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

slots.codeSystemsContainer__omim = Slot(uri=CIEINR.omim, name="codeSystemsContainer__omim", curie=CIEINR.curie('omim'),
                   model_uri=CIEINR.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

slots.codeSystemsContainer__orpha = Slot(uri=CIEINR.orpha, name="codeSystemsContainer__orpha", curie=CIEINR.curie('orpha'),
                   model_uri=CIEINR.codeSystemsContainer__orpha, domain=None, range=Union[str, "ORPHA"])

slots.codeSystemsContainer__ncit = Slot(uri=CIEINR.ncit, name="codeSystemsContainer__ncit", curie=CIEINR.curie('ncit'),
                   model_uri=CIEINR.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

slots.codeSystemsContainer__uo = Slot(uri=CIEINR.uo, name="codeSystemsContainer__uo", curie=CIEINR.curie('uo'),
                   model_uri=CIEINR.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

slots.codeSystemsContainer__hgnc = Slot(uri=CIEINR.hgnc, name="codeSystemsContainer__hgnc", curie=CIEINR.curie('hgnc'),
                   model_uri=CIEINR.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

slots.codeSystemsContainer__hgvs = Slot(uri=CIEINR.hgvs, name="codeSystemsContainer__hgvs", curie=CIEINR.curie('hgvs'),
                   model_uri=CIEINR.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

slots.codeSystemsContainer__ga4gh = Slot(uri=CIEINR.ga4gh, name="codeSystemsContainer__ga4gh", curie=CIEINR.curie('ga4gh'),
                   model_uri=CIEINR.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

slots.codeSystemsContainer__hl7fhir = Slot(uri=CIEINR.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=CIEINR.curie('hl7fhir'),
                   model_uri=CIEINR.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

slots.codeSystemsContainer__icd11 = Slot(uri=CIEINR.icd11, name="codeSystemsContainer__icd11", curie=CIEINR.curie('icd11'),
                   model_uri=CIEINR.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

slots.codeSystemsContainer__icd10cm = Slot(uri=CIEINR.icd10cm, name="codeSystemsContainer__icd10cm", curie=CIEINR.curie('icd10cm'),
                   model_uri=CIEINR.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

slots.codeSystemsContainer__bioportal = Slot(uri=CIEINR.bioportal, name="codeSystemsContainer__bioportal", curie=CIEINR.curie('bioportal'),
                   model_uri=CIEINR.codeSystemsContainer__bioportal, domain=None, range=Union[str, "BIOPORTAL"])

slots.codeSystemsContainer__iuis = Slot(uri=CIEINR.iuis, name="codeSystemsContainer__iuis", curie=CIEINR.curie('iuis'),
                   model_uri=CIEINR.codeSystemsContainer__iuis, domain=None, range=Union[str, "IUIS"])
