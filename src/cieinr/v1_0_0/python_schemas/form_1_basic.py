# Auto generated from form_1_basic.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-20T18:28:50
# Schema: basic_form
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/limkml_schemas/form_1_basic.yaml
# description: Basic form containing IEI diagnosis information for Phenopackets export
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

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MONDO = CurieNamespace('MONDO', 'https://purl.obolibrary.org/obo/MONDO_')
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
class BasicForm(YAMLRoot):
    """
    The basic form containing the IEI diagnosis information needed for Phenopackets export.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["BasicForm"]
    class_class_curie: ClassVar[str] = "cieinr:BasicForm"
    class_name: ClassVar[str] = "BasicForm"
    class_model_uri: ClassVar[URIRef] = CIEINR.BasicForm

    basic_form_complete: Union[str, "CompletionStatusEnumBasicForm"] = None
    iei_deficiency_basic: Optional[Union[str, "IUIS2024MONDOEnum"]] = None
    igrt_basic: Optional[Union[str, "IGRTStatusEnumBasicForm"]] = None
    hct_basic_form: Optional[Union[str, "HCTStatusEnumBasicForm"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.basic_form_complete):
            self.MissingRequiredField("basic_form_complete")
        if not isinstance(self.basic_form_complete, CompletionStatusEnumBasicForm):
            self.basic_form_complete = CompletionStatusEnumBasicForm(self.basic_form_complete)

        if self.iei_deficiency_basic is not None and not isinstance(self.iei_deficiency_basic, IUIS2024MONDOEnum):
            self.iei_deficiency_basic = IUIS2024MONDOEnum(self.iei_deficiency_basic)

        if self.igrt_basic is not None and not isinstance(self.igrt_basic, IGRTStatusEnumBasicForm):
            self.igrt_basic = IGRTStatusEnumBasicForm(self.igrt_basic)

        if self.hct_basic_form is not None and not isinstance(self.hct_basic_form, HCTStatusEnumBasicForm):
            self.hct_basic_form = HCTStatusEnumBasicForm(self.hct_basic_form)

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
class CompletionStatusEnumBasicForm(EnumDefinitionImpl):
    """
    Enumeration for form completion status
    """
    _defn = EnumDefinition(
        name="CompletionStatusEnumBasicForm",
        description="""Enumeration for form completion status""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
            PermissibleValue(
                text="0",
                description="Incomplete"))
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="Unverified"))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="Complete"))

class IGRTStatusEnumBasicForm(EnumDefinitionImpl):
    """
    Enumeration for Immunoglobulin replacement therapy status in the basic form
    """
    ncit_c62710 = PermissibleValue(
        text="ncit_c62710",
        description="Immunoglobulin Therapy")

    _defn = EnumDefinition(
        name="IGRTStatusEnumBasicForm",
        description="""Enumeration for Immunoglobulin replacement therapy status in the basic form""",
    )

class HCTStatusEnumBasicForm(EnumDefinitionImpl):
    """
    Enumeration for Hematopoietic cell transplantation status in the basic form
    """
    ncit_c15431 = PermissibleValue(
        text="ncit_c15431",
        description="Hematopoietic Cell Transplantation")

    _defn = EnumDefinition(
        name="HCTStatusEnumBasicForm",
        description="""Enumeration for Hematopoietic cell transplantation status in the basic form""",
    )

class IUIS2024MONDOEnum(EnumDefinitionImpl):
    """
    Enumeration of Inborn Errors of Immunity based on IUIS 2024 classification
    """
    mondo_0800045 = PermissibleValue(
        text="mondo_0800045",
        description="A20 deficiency - TNFAIP3",
        meaning=MONDO["0800045"])
    mondo_0014561 = PermissibleValue(
        text="mondo_0014561",
        description="3-Methylglutaconic aciduria (AR) - CLPB",
        meaning=MONDO["0014561"])
    mondo_0859237 = PermissibleValue(
        text="mondo_0859237",
        description="3-Methylglutaconic aciduria (AD) - CLPB",
        meaning=MONDO["0859237"])
    mondo_0007818 = PermissibleValue(
        text="mondo_0007818",
        description="AD-HIES Job syndrome - STAT3",
        meaning=MONDO["0007818"])
    mondo_0007064 = PermissibleValue(
        text="mondo_0007064",
        description="Adenosine deaminase (ADA) deficiency - ADA",
        meaning=MONDO["0007064"])
    mondo_0011528 = PermissibleValue(
        text="mondo_0011528",
        description="AID deficiency - AICDA",
        meaning=MONDO["0011528"])
    mondo_0014306 = PermissibleValue(
        text="mondo_0014306",
        description="ADA2 deficiency - ADA2",
        meaning=MONDO["0014306"])
    mondo_0013693 = PermissibleValue(
        text="mondo_0013693",
        description="ADAM17 deficiency - ADAM17",
        meaning=MONDO["0013693"])
    mondo_0014007 = PermissibleValue(
        text="mondo_0014007",
        description="ADAR1 deficiency (AGS6) - ADAR1",
        meaning=MONDO["0014007"])
    mondo_0033554 = PermissibleValue(
        text="mondo_0033554",
        description="Activated RAC2 defect - RAC2",
        meaning=MONDO["0033554"])
    mondo_0014230 = PermissibleValue(
        text="mondo_0014230",
        description="ACT1 deficiency - TRAF3IP2",
        meaning=MONDO["0014230"])
    mondo_0014659 = PermissibleValue(
        text="mondo_0014659",
        description="Acute liver failure due to NBAS deficiency - NBAS",
        meaning=MONDO["0014659"])
    mondo_0011953 = PermissibleValue(
        text="mondo_0011953",
        description="Acute necrotizing encephalopathy - RANBP2",
        meaning=MONDO["0011953"])
    mondo_0035370 = PermissibleValue(
        text="mondo_0035370",
        description="ALPI deficiency - ALPI",
        meaning=MONDO["0035370"])
    mondo_0011383 = PermissibleValue(
        text="mondo_0011383",
        description="ALPS-Caspase10 - CASP10",
        meaning=MONDO["0011383"])
    mondo_0011804 = PermissibleValue(
        text="mondo_0011804",
        description="ALPS-Caspase 8 - CASP8",
        meaning=MONDO["0011804"])
    mondo_0011158 = PermissibleValue(
        text="mondo_0011158",
        description="ALPS-FAS (AD / AR) - TNFRSF6",
        meaning=MONDO["0011158"])
    alps_faslg = PermissibleValue(
        text="alps_faslg",
        description="ALPS-FASLG - TNFSF6",
        meaning=CIEINR["alps_faslg"])
    mondo_0009411 = PermissibleValue(
        text="mondo_0009411",
        description="APECED (APS-1), autoimmune polyendocrinopathy with candidiasis and ectodermal dystrophy - AIRE",
        meaning=MONDO["0009411"])
    mondo_0014494 = PermissibleValue(
        text="mondo_0014494",
        description="AP1S3 deficiency - AP1S3",
        meaning=MONDO["0014494"])
    mondo_0032763 = PermissibleValue(
        text="mondo_0032763",
        description="ARHGEF1 deficiency - ARHGEF1",
        meaning=MONDO["0032763"])
    mondo_0957920 = PermissibleValue(
        text="mondo_0957920",
        description="ARPC5 deficiency - ARPC5",
        meaning=MONDO["0957920"])
    mondo_0060583 = PermissibleValue(
        text="mondo_0060583",
        description="ARPC1B deficiency - ARPC1B",
        meaning=MONDO["0060583"])
    mondo_0014958 = PermissibleValue(
        text="mondo_0014958",
        description="ATAD3A deficiency (AD) - ATAD3A",
        meaning=MONDO["0014958"])
    mondo_0032931 = PermissibleValue(
        text="mondo_0032931",
        description="ATAD3A deficiency (AR) - ATAD3A",
        meaning=MONDO["0032931"])
    atg4a_deficiency = PermissibleValue(
        text="atg4a_deficiency",
        description="ATG4A - ATG4A",
        meaning=CIEINR["atg4a_deficiency"])
    mondo_0016419 = PermissibleValue(
        text="mondo_0016419",
        description="Ataxia-telangiectasia - ATM",
        meaning=MONDO["0016419"])
    mondo_0008840 = PermissibleValue(
        text="mondo_0008840",
        description="Ataxia-telangiectasia - ATM",
        meaning=MONDO["0008840"])
    mondo_0008038 = PermissibleValue(
        text="mondo_0008038",
        description="Ataxia Pancytopenia Syndrome - SAMD9L",
        meaning=MONDO["0008038"])
    mondo_0010504 = PermissibleValue(
        text="mondo_0010504",
        description="ATP6AP1 deficiency - ATP6AP1",
        meaning=MONDO["0010504"])
    mondo_0009308 = PermissibleValue(
        text="mondo_0009308",
        description="Autosomal recessive CGD p22phox - CYBA",
        meaning=MONDO["0009308"])
    mondo_0030066 = PermissibleValue(
        text="mondo_0030066",
        description="Autosomal recessive CGD EROS - CYBC1",
        meaning=MONDO["0030066"])
    mondo_0009310 = PermissibleValue(
        text="mondo_0009310",
        description="Autosomal recessive CGD p67phox - NCF2",
        meaning=MONDO["0009310"])
    mondo_0013507 = PermissibleValue(
        text="mondo_0013507",
        description="Autosomal recessive CGD p40phox - NCF4",
        meaning=MONDO["0013507"])
    mondo_0009309 = PermissibleValue(
        text="mondo_0009309",
        description="Autosomal recessive CGD p47phox - NCF1",
        meaning=MONDO["0009309"])
    mondo_0009039 = PermissibleValue(
        text="mondo_0009039",
        description="Baller-Gerold Syndrome - RECQL4",
        meaning=MONDO["0009039"])
    mondo_0013284 = PermissibleValue(
        text="mondo_0013284",
        description="BAFF receptor deficiency - TNFRSF13C",
        meaning=MONDO["0013284"])
    mondo_0032723 = PermissibleValue(
        text="mondo_0032723",
        description="BACH2 deficiency - BACH2",
        meaning=MONDO["0032723"])
    mondo_0009470 = PermissibleValue(
        text="mondo_0009470",
        description="b actin deficiency - ACTB",
        meaning=MONDO["0009470"])
    mondo_0010543 = PermissibleValue(
        text="mondo_0010543",
        description="Barth Syndrome (3-Methylglutaconic aciduria type II) - TAZ",
        meaning=MONDO["0010543"])
    mondo_0014981 = PermissibleValue(
        text="mondo_0014981",
        description="BCL11B deficiency - BCL11B",
        meaning=MONDO["0014981"])
    mondo_0014491 = PermissibleValue(
        text="mondo_0014491",
        description="BCL10 deficiency - BCL10",
        meaning=MONDO["0014491"])
    mondo_0014645 = PermissibleValue(
        text="mondo_0014645",
        description="CARD11 GOF - CARD11",
        meaning=MONDO["0014645"])
    mondo_0013289 = PermissibleValue(
        text="mondo_0013289",
        description="BLNK deficiency - BLNK",
        meaning=MONDO["0013289"])
    mondo_0008876 = PermissibleValue(
        text="mondo_0008876",
        description="Bloom Syndrome - BLM",
        meaning=MONDO["0008876"])
    mondo_0008523 = PermissibleValue(
        text="mondo_0008523",
        description="Blau syndrome - NOD2",
        meaning=MONDO["0008523"])
    mondo_0014317 = PermissibleValue(
        text="mondo_0014317",
        description="BMFS2 (Hebo deficiency) - ERCC6L2",
        meaning=MONDO["0014317"])
    mondo_0013851 = PermissibleValue(
        text="mondo_0013851",
        description="BMFS1 (SRP72-deficiency) - SRP72",
        meaning=MONDO["0013851"])
    mondo_0032573 = PermissibleValue(
        text="mondo_0032573",
        description="BMFS5 - TP53",
        meaning=MONDO["0032573"])
    mondo_0010421 = PermissibleValue(
        text="mondo_0010421",
        description="BTK deficiency, X-linked agammaglobulinemia (XLA) - BTK",
        meaning=MONDO["0010421"])
    mondo_0030378 = PermissibleValue(
        text="mondo_0030378",
        description="C2orf69 deficiency - C2orf69",
        meaning=MONDO["0030378"])
    mondo_0958182 = PermissibleValue(
        text="mondo_0958182",
        description="C1q deficiency due to defects in C1QA - C1QA",
        meaning=MONDO["0958182"])
    mondo_0958187 = PermissibleValue(
        text="mondo_0958187",
        description="C1q deficiency due to defects in C1QB - C1QB",
        meaning=MONDO["0958187"])
    mondo_0958188 = PermissibleValue(
        text="mondo_0958188",
        description="C1q deficiency due to defects in C1QC - C1QC",
        meaning=MONDO["0958188"])
    mondo_0009005 = PermissibleValue(
        text="mondo_0009005",
        description="C1r deficiency - C1R",
        meaning=MONDO["0009005"])
    mondo_0020684 = PermissibleValue(
        text="mondo_0020684",
        description="C1r Periodontal Ehlers Danlos - C1R",
        meaning=MONDO["0020684"])
    mondo_0013419 = PermissibleValue(
        text="mondo_0013419",
        description="C1s deficiency - C1S",
        meaning=MONDO["0013419"])
    mondo_0014954 = PermissibleValue(
        text="mondo_0014954",
        description="C1s Periodontal Ehlers Danlos - C1S",
        meaning=MONDO["0014954"])
    mondo_0009006 = PermissibleValue(
        text="mondo_0009006",
        description="C2 deficiency - C2",
        meaning=MONDO["0009006"])
    mondo_0013417 = PermissibleValue(
        text="mondo_0013417",
        description="C3 deficiency (LOF) - C3",
        meaning=MONDO["0013417"])
    mondo_0013043 = PermissibleValue(
        text="mondo_0013043",
        description="C3 GOF - C3",
        meaning=MONDO["0013043"])
    mondo_0033946 = PermissibleValue(
        text="mondo_0033946",
        description="C1 inhibitor deficiency - SERPING1",
        meaning=MONDO["0033946"])
    complete_c4_deficiency = PermissibleValue(
        text="complete_c4_deficiency",
        description="Complete C4 deficiency - C4A & C4B",
        meaning=CIEINR["complete_c4_deficiency"])
    mondo_0012295 = PermissibleValue(
        text="mondo_0012295",
        description="C5 deficiency - C5",
        meaning=MONDO["0012295"])
    mondo_0012908 = PermissibleValue(
        text="mondo_0012908",
        description="C6 deficiency - C6",
        meaning=MONDO["0012908"])
    mondo_0012412 = PermissibleValue(
        text="mondo_0012412",
        description="C7 deficiency - C7",
        meaning=MONDO["0012412"])
    mondo_0013422 = PermissibleValue(
        text="mondo_0013422",
        description="C8a deficiency - C8A",
        meaning=MONDO["0013422"])
    mondo_0013421 = PermissibleValue(
        text="mondo_0013421",
        description="C8b deficiency - C8B",
        meaning=MONDO["0013421"])
    c8g_deficiency = PermissibleValue(
        text="c8g_deficiency",
        description="C8g deficiency - C8G",
        meaning=CIEINR["c8g_deficiency"])
    mondo_0013445 = PermissibleValue(
        text="mondo_0013445",
        description="C9 deficiency - C9",
        meaning=MONDO["0013445"])
    mondo_0011269 = PermissibleValue(
        text="mondo_0011269",
        description="CAMPS (CARD14 mediated psoriasis) - CARD14",
        meaning=MONDO["0011269"])
    mondo_0008905 = PermissibleValue(
        text="mondo_0008905",
        description="CARD9 deficiency - CARD9",
        meaning=MONDO["0008905"])
    mondo_0054697 = PermissibleValue(
        text="mondo_0054697",
        description="CARD11 DN LOF - CARD11",
        meaning=MONDO["0054697"])
    mondo_0014081 = PermissibleValue(
        text="mondo_0014081",
        description="CARD11 deficiency (LOF) - CARD11",
        meaning=MONDO["0014081"])
    cd137_deficiency_41bb = PermissibleValue(
        text="cd137_deficiency_41bb",
        description="CD137 deficiency (41BB) - TNFRSF9",
        meaning=CIEINR["cd137_deficiency_41bb"])
    cd28_deficiency = PermissibleValue(
        text="cd28_deficiency",
        description="CD28 deficiency - CD28",
        meaning=CIEINR["cd28_deficiency"])
    mondo_0014054 = PermissibleValue(
        text="mondo_0014054",
        description="CD27 deficiency - CD27",
        meaning=MONDO["0014054"])
    mondo_0014313 = PermissibleValue(
        text="mondo_0014313",
        description="CD16 deficiency - FCGR3A",
        meaning=MONDO["0014313"])
    mondo_0013283 = PermissibleValue(
        text="mondo_0013283",
        description="CD19 deficiency - CD19",
        meaning=MONDO["0013283"])
    mondo_0013285 = PermissibleValue(
        text="mondo_0013285",
        description="CD20 deficiency - CD20",
        meaning=MONDO["0013285"])
    mondo_0013862 = PermissibleValue(
        text="mondo_0013862",
        description="CD21 deficiency - CD21",
        meaning=MONDO["0013862"])
    mondo_0011664 = PermissibleValue(
        text="mondo_0011664",
        description="CD25 deficiency - IL2RA",
        meaning=MONDO["0011664"])
    mondo_0032782 = PermissibleValue(
        text="mondo_0032782",
        description="CD122 deficiency - IL2RB",
        meaning=MONDO["0032782"])
    mondo_0013286 = PermissibleValue(
        text="mondo_0013286",
        description="CD81 deficiency - CD81",
        meaning=MONDO["0013286"])
    mondo_0800104 = PermissibleValue(
        text="mondo_0800104",
        description="CD45 deficiency - PTPRC",
        meaning=MONDO["0800104"])
    mondo_0034054 = PermissibleValue(
        text="mondo_0034054",
        description="CD70 deficiency - CD70",
        meaning=MONDO["0034054"])
    mondo_0012161 = PermissibleValue(
        text="mondo_0012161",
        description="CD8 deficiency - CD8A",
        meaning=MONDO["0012161"])
    mondo_0009174 = PermissibleValue(
        text="mondo_0009174",
        description="CD55 deficiency (CHAPEL disease) - CD55",
        meaning=MONDO["0009174"])
    mondo_0957388 = PermissibleValue(
        text="mondo_0957388",
        description="CBLB deficiency - CBLB",
        meaning=MONDO["0957388"])
    mondo_0009060 = PermissibleValue(
        text="mondo_0009060",
        description="CCR2 deficiency - CCR2",
        meaning=MONDO["0009060"])
    mondo_0014757 = PermissibleValue(
        text="mondo_0014757",
        description="CDC42 defects - CDC42",
        meaning=MONDO["0014757"])
    mondo_0014276 = PermissibleValue(
        text="mondo_0014276",
        description="CD3g deficiency - CD3G",
        meaning=MONDO["0014276"])
    mondo_0014280 = PermissibleValue(
        text="mondo_0014280",
        description="CD3d deficiency - CD3D",
        meaning=MONDO["0014280"])
    mondo_0014278 = PermissibleValue(
        text="mondo_0014278",
        description="CD3e deficiency - CD3E",
        meaning=MONDO["0014278"])
    mondo_0012426 = PermissibleValue(
        text="mondo_0012426",
        description="CD3z deficiency - CD247",
        meaning=MONDO["0012426"])
    mondo_0044207 = PermissibleValue(
        text="mondo_0044207",
        description="CEBPE defects - CEBPE",
        meaning=MONDO["0044207"])
    mondo_0012650 = PermissibleValue(
        text="mondo_0012650",
        description="Cernunnos/XLF deficiency - NHEJ1",
        meaning=MONDO["0012650"])
    charge_syndrome_sema3e = PermissibleValue(
        text="charge_syndrome_sema3e",
        description="CHARGE syndrome due to SEMA3E deficiency - SEMA3E",
        meaning=CIEINR["charge_syndrome_sema3e"])
    mondo_0008965 = PermissibleValue(
        text="mondo_0008965",
        description="CHARGE syndrome due to CHD7 deficiency - CHD7",
        meaning=MONDO["0008965"])
    mondo_0008963 = PermissibleValue(
        text="mondo_0008963",
        description="Chediak-Higashi syndrome - LYST",
        meaning=MONDO["0008963"])
    mondo_0007315 = PermissibleValue(
        text="mondo_0007315",
        description="Cherubism - SH3BP2",
        meaning=MONDO["0007315"])
    mondo_0007838 = PermissibleValue(
        text="mondo_0007838",
        description="Chromosome 11q deletion syndrome (Jacobsen syndrome) - 11q23del",
        meaning=MONDO["0007838"])
    mondo_0011055 = PermissibleValue(
        text="mondo_0011055",
        description="Chromosome 10p13-p14 deletion Syndrome (10p13-p14DS) - Del10p13-p14",
        meaning=MONDO["0011055"])
    mondo_0008564 = PermissibleValue(
        text="mondo_0008564",
        description="""Chromosome 22q11.2 deletion Syndrome (22q11.2DS) (AKA DiGeorge/velocardiofacial syndrome) - Large (3Mb) deletion of 22q11.2""",
        meaning=MONDO["0008564"])
    mondo_0032644 = PermissibleValue(
        text="mondo_0032644",
        description="CIB1 deficiency - CIB1",
        meaning=MONDO["0032644"])
    mondo_0011405 = PermissibleValue(
        text="mondo_0011405",
        description="Clericuzio syndrome (Poikiloderma with neutropenia) - USB1",
        meaning=MONDO["0011405"])
    mondo_0012676 = PermissibleValue(
        text="mondo_0012676",
        description="CLCN7 deficiency associated osteopetrosis (AR) - CLCN7",
        meaning=MONDO["0012676"])
    mondo_0008156 = PermissibleValue(
        text="mondo_0008156",
        description="CLCN7 deficiency associated osteopetrosis (AD) - CLCN7",
        meaning=MONDO["0008156"])
    mondo_0024564 = PermissibleValue(
        text="mondo_0024564",
        description="Coats plus syndrome due to CTC1 deficiency - CTC1",
        meaning=MONDO["0024564"])
    mondo_0015026 = PermissibleValue(
        text="mondo_0015026",
        description="Coats plus syndrome due to STN1 deficiency - STN1",
        meaning=MONDO["0015026"])
    mondo_0008999 = PermissibleValue(
        text="mondo_0008999",
        description="Cohen syndrome - VPS13B",
        meaning=MONDO["0008999"])
    mondo_0009595 = PermissibleValue(
        text="mondo_0009595",
        description="Cartilage hair hypoplasia (CHH) - RMRP",
        meaning=MONDO["0009595"])
    mondo_0054698 = PermissibleValue(
        text="mondo_0054698",
        description="""CANDLE (chronic atypical neutrophilic dermatitis with lipodystrophy) Gene (PSMB8) (AD / AR) - PSMB8""",
        meaning=MONDO["0054698"])
    mondo_0030931 = PermissibleValue(
        text="mondo_0030931",
        description="CANDLE (chronic atypical neutrophilic dermatitis with lipodystrophy) (Gene PSMG2) - PSMG2",
        meaning=MONDO["0030931"])
    mondo_0019093 = PermissibleValue(
        text="mondo_0019093",
        description="Specific antibody deficiency with normal Ig levels and normal B cells - Unknown",
        meaning=MONDO["0019093"])
    mondo_0014168 = PermissibleValue(
        text="mondo_0014168",
        description="Coronin-1A deficiency - CORO1A",
        meaning=MONDO["0014168"])
    mondo_0800136 = PermissibleValue(
        text="mondo_0800136",
        description="COPG1 deficiency - COPG1",
        meaning=MONDO["0800136"])
    mondo_0014629 = PermissibleValue(
        text="mondo_0014629",
        description="COPA defect - COPA",
        meaning=MONDO["0014629"])
    mondo_0958177 = PermissibleValue(
        text="mondo_0958177",
        description="CRMO3 IL1R1 disorder - IL1R1",
        meaning=MONDO["0958177"])
    mondo_0010424 = PermissibleValue(
        text="mondo_0010424",
        description="Congenital pulmonary alveolar proteinosis due to CSF2RA mutations - CSF2RA",
        meaning=MONDO["0010424"])
    mondo_0013712 = PermissibleValue(
        text="mondo_0013712",
        description="Congenital pulmonary alveolar proteinosis due to CSF2RB mutations - CSF2RB",
        meaning=MONDO["0013712"])
    mondo_0030798 = PermissibleValue(
        text="mondo_0030798",
        description="CTNNBL1 deficiency - CTNNBL1",
        meaning=MONDO["0030798"])
    mondo_0014391 = PermissibleValue(
        text="mondo_0014391",
        description="CTPS1 deficiency - CTPS1",
        meaning=MONDO["0014391"])
    mondo_0014493 = PermissibleValue(
        text="mondo_0014493",
        description="CTLA4 deficiency (ALPSV) - CTLA4",
        meaning=MONDO["0014493"])
    mondo_0030374 = PermissibleValue(
        text="mondo_0030374",
        description="CXCR2 deficiency - CXCR2",
        meaning=MONDO["0030374"])
    mondo_0009061 = PermissibleValue(
        text="mondo_0009061",
        description="Cystic fibrosis - CFTR",
        meaning=MONDO["0009061"])
    cvid_no_genedef_specified = PermissibleValue(
        text="cvid_no_genedef_specified",
        description="Common variable immune deficiency with no gene defect specified (CVID) - Unknown",
        meaning=CIEINR["cvid_no_genedef_specified"])
    mondo_0800134 = PermissibleValue(
        text="mondo_0800134",
        description="CRACR2A deficiency - CRACR2A",
        meaning=MONDO["0800134"])
    dbf4_deficiency = PermissibleValue(
        text="dbf4_deficiency",
        description="DBF4 deficiency - DBF4",
        meaning=CIEINR["dbf4_deficiency"])
    mondo_0030334 = PermissibleValue(
        text="mondo_0030334",
        description="DBR1 deficiency - DBR1",
        meaning=MONDO["0030334"])
    mondo_0011225 = PermissibleValue(
        text="mondo_0011225",
        description="DCLRE1C (Artemis) deficiency - DCLRE1C",
        meaning=MONDO["0011225"])
    mondo_0030457 = PermissibleValue(
        text="mondo_0030457",
        description="DEF6 deficiency - DEF6",
        meaning=MONDO["0030457"])
    mondo_0007485 = PermissibleValue(
        text="mondo_0007485",
        description="DKCA1 - TERC",
        meaning=MONDO["0007485"])
    mondo_0013521 = PermissibleValue(
        text="mondo_0013521",
        description="DKCA2 - TERT",
        meaning=MONDO["0013521"])
    mondo_0013522 = PermissibleValue(
        text="mondo_0013522",
        description="DKCA3 - TINF2",
        meaning=MONDO["0013522"])
    mondo_0014076 = PermissibleValue(
        text="mondo_0014076",
        description="DKCA4 - RTEL1",
        meaning=MONDO["0014076"])
    mondo_0014690 = PermissibleValue(
        text="mondo_0014690",
        description="DKCA6 (AD / AR) - ACD",
        meaning=MONDO["0014690"])
    mondo_0009136 = PermissibleValue(
        text="mondo_0009136",
        description="DKCB1 - NOLA3",
        meaning=MONDO["0009136"])
    mondo_0013519 = PermissibleValue(
        text="mondo_0013519",
        description="DKCB2 - NOLA2",
        meaning=MONDO["0013519"])
    mondo_0013520 = PermissibleValue(
        text="mondo_0013520",
        description="DKCB3 - WRAP53",
        meaning=MONDO["0013520"])
    mondo_0027353 = PermissibleValue(
        text="mondo_0027353",
        description="DKCB4 - TERT",
        meaning=MONDO["0027353"])
    mondo_0014600 = PermissibleValue(
        text="mondo_0014600",
        description="DKCB6 - PARN",
        meaning=MONDO["0014600"])
    mondo_0010584 = PermissibleValue(
        text="mondo_0010584",
        description="DKCX1 - DKC1",
        meaning=MONDO["0010584"])
    mondo_0859319 = PermissibleValue(
        text="mondo_0859319",
        description="DKC DCLRE1B - DCLRE1B",
        meaning=MONDO["0859319"])
    mondo_0013021 = PermissibleValue(
        text="mondo_0013021",
        description="DIRA (Deficiency of the Interleukin 1 Receptor Antagonist) - IL1RN",
        meaning=MONDO["0013021"])
    mondo_0013626 = PermissibleValue(
        text="mondo_0013626",
        description="DITRA (Deficiency of IL-36 receptor antagonist) - IL36RN",
        meaning=MONDO["0013626"])
    mondo_0014714 = PermissibleValue(
        text="mondo_0014714",
        description="DIAPH1 deficiency - DIAPH1",
        meaning=MONDO["0014714"])
    mondo_0957494 = PermissibleValue(
        text="mondo_0957494",
        description="DOCK11 deficiency - DOCK11",
        meaning=MONDO["0957494"])
    mondo_0014637 = PermissibleValue(
        text="mondo_0014637",
        description="DOCK2 deficiency - DOCK2",
        meaning=MONDO["0014637"])
    mondo_0009478 = PermissibleValue(
        text="mondo_0009478",
        description="DOCK8 deficiency - DOCK8",
        meaning=MONDO["0009478"])
    mondo_0957229 = PermissibleValue(
        text="mondo_0957229",
        description="DPP9 deficiency - DPP9",
        meaning=MONDO["0957229"])
    mondo_0011686 = PermissibleValue(
        text="mondo_0011686",
        description="DNA ligase IV deficiency - LIG4",
        meaning=MONDO["0011686"])
    mondo_0014423 = PermissibleValue(
        text="mondo_0014423",
        description="DNA PKcs deficiency - PRKDC",
        meaning=MONDO["0014423"])
    mondo_0013743 = PermissibleValue(
        text="mondo_0013743",
        description="DNASE1L3 deficiency - DNASE1L3",
        meaning=MONDO["0013743"])
    mondo_0800132 = PermissibleValue(
        text="mondo_0800132",
        description="DNASE2 deficiency - DNASE2",
        meaning=MONDO["0800132"])
    dnjac21_deficiency = PermissibleValue(
        text="dnjac21_deficiency",
        description="Schwachman Diamond syndrome due to DNAJC21 deficiency - DNAJC21",
        meaning=CIEINR["dnjac21_deficiency"])
    mondo_0032806 = PermissibleValue(
        text="mondo_0032806",
        description="EDA-ID due to IKBA GOF - NFKBIA",
        meaning=MONDO["0032806"])
    mondo_0020740 = PermissibleValue(
        text="mondo_0020740",
        description="EDA-ID due to NEMO/IKBKG deficiency (ectodermal dysplasia, immune deficiency) - IKBKG",
        meaning=MONDO["0020740"])
    mondo_0032599 = PermissibleValue(
        text="mondo_0032599",
        description="EDA-ID due to IKBKB GOF mutation - IKBKB",
        meaning=MONDO["0032599"])
    mondo_0042490 = PermissibleValue(
        text="mondo_0042490",
        description="Elastase deficiency (SCN1) - ELANE",
        meaning=MONDO["0042490"])
    mondo_0024770 = PermissibleValue(
        text="mondo_0024770",
        description="ELF deficiency - ELF4",
        meaning=MONDO["0024770"])
    mondo_0044205 = PermissibleValue(
        text="mondo_0044205",
        description="Schwachman Diamond syndrome due to EFL1 deficiency - EFL1",
        meaning=MONDO["0044205"])
    mondo_0958120 = PermissibleValue(
        text="mondo_0958120",
        description="ERBIN deficiency - ERBIN",
        meaning=MONDO["0958120"])
    mondo_0100045 = PermissibleValue(
        text="mondo_0100045",
        description="EVER1 deficiency - TMC6",
        meaning=MONDO["0100045"])
    mondo_0032614 = PermissibleValue(
        text="mondo_0032614",
        description="EVER2 deficiency - TMC8",
        meaning=MONDO["0032614"])
    mondo_0014758 = PermissibleValue(
        text="mondo_0014758",
        description="EVI1, MECOM deficiency - MECOM",
        meaning=MONDO["0014758"])
    mondo_0013408 = PermissibleValue(
        text="mondo_0013408",
        description="FADD deficiency - FADD",
        meaning=MONDO["0013408"])
    faap24_deficiency = PermissibleValue(
        text="faap24_deficiency",
        description="FAAP24 deficiency - FAAP24",
        meaning=CIEINR["faap24_deficiency"])
    mondo_0012350 = PermissibleValue(
        text="mondo_0012350",
        description="Factor H deficiency (AR / AD) - CFH",
        meaning=MONDO["0012350"])
    factor_h_related_prot_def = PermissibleValue(
        text="factor_h_related_prot_def",
        description="Factor H –related protein deficiencies - CFHR1",
        meaning=CIEINR["factor_h_related_prot_def"])
    mondo_0012594 = PermissibleValue(
        text="mondo_0012594",
        description="Factor I deficiency (AR) - CFI",
        meaning=MONDO["0012594"])
    mondo_0013041 = PermissibleValue(
        text="mondo_0013041",
        description="Factor I deficiency (AD) - CFI",
        meaning=MONDO["0013041"])
    mondo_0013042 = PermissibleValue(
        text="mondo_0013042",
        description="Factor B GOF (AD) - CFB",
        meaning=MONDO["0013042"])
    mondo_0014255 = PermissibleValue(
        text="mondo_0014255",
        description="Factor B LOF (AR) - CFB",
        meaning=MONDO["0014255"])
    mondo_0013487 = PermissibleValue(
        text="mondo_0013487",
        description="Factor D deficiency - CFD",
        meaning=MONDO["0013487"])
    mondo_0007601 = PermissibleValue(
        text="mondo_0007601",
        description="Familial Mediterranean fever (AD) - MEFV",
        meaning=MONDO["0007601"])
    mondo_0009572 = PermissibleValue(
        text="mondo_0009572",
        description="Familial Mediterranean fever (AR) - MEFV",
        meaning=MONDO["0009572"])
    mondo_0007349 = PermissibleValue(
        text="mondo_0007349",
        description="Familial cold autoinflammatory syndrome 1 - NLRP3",
        meaning=MONDO["0007349"])
    mondo_0012724 = PermissibleValue(
        text="mondo_0012724",
        description="Familial cold autoinflammatory syndrome 2 - NLRP12",
        meaning=MONDO["0012724"])
    mondo_0013766 = PermissibleValue(
        text="mondo_0013766",
        description="familial cold autoinflammatory syndrome 3 - PLCG2",
        meaning=MONDO["0013766"])
    mondo_0009215 = PermissibleValue(
        text="mondo_0009215",
        description="Fanconi Anemia Type A - FANCA",
        meaning=MONDO["0009215"])
    mondo_0010351 = PermissibleValue(
        text="mondo_0010351",
        description="Fanconi Anemia Type B - FANCB",
        meaning=MONDO["0010351"])
    mondo_0009213 = PermissibleValue(
        text="mondo_0009213",
        description="Fanconi Anemia Type C - FANCC",
        meaning=MONDO["0009213"])
    mondo_0009214 = PermissibleValue(
        text="mondo_0009214",
        description="Fanconi Anemia Type D2 - FANCD2",
        meaning=MONDO["0009214"])
    mondo_0011584 = PermissibleValue(
        text="mondo_0011584",
        description="Fanconi Anemia Type D1 - BRCA2",
        meaning=MONDO["0011584"])
    mondo_0010953 = PermissibleValue(
        text="mondo_0010953",
        description="Fanconi Anemia Type E - FANCE",
        meaning=MONDO["0010953"])
    mondo_0011325 = PermissibleValue(
        text="mondo_0011325",
        description="Fanconi Anemia Type F - FANCF",
        meaning=MONDO["0011325"])
    mondo_0013565 = PermissibleValue(
        text="mondo_0013565",
        description="Fanconi Anemia Type G - XRCC9",
        meaning=MONDO["0013565"])
    mondo_0012186 = PermissibleValue(
        text="mondo_0012186",
        description="Fanconi Anemia Type I - FANCI",
        meaning=MONDO["0012186"])
    mondo_0012187 = PermissibleValue(
        text="mondo_0012187",
        description="Fanconi Anemia Type J - BRIP1",
        meaning=MONDO["0012187"])
    mondo_0013566 = PermissibleValue(
        text="mondo_0013566",
        description="Fanconi Anemia Type L - FANCL",
        meaning=MONDO["0013566"])
    mondo_0054862 = PermissibleValue(
        text="mondo_0054862",
        description="Fanconi Anemia Type M - FANCM",
        meaning=MONDO["0054862"])
    mondo_0012565 = PermissibleValue(
        text="mondo_0012565",
        description="Fanconi Anemia Type N - PALB2",
        meaning=MONDO["0012565"])
    mondo_0013248 = PermissibleValue(
        text="mondo_0013248",
        description="Fanconi Anemia Type O - RAD51C",
        meaning=MONDO["0013248"])
    mondo_0013499 = PermissibleValue(
        text="mondo_0013499",
        description="Fanconi Anemia Type P - SLX4",
        meaning=MONDO["0013499"])
    mondo_0014108 = PermissibleValue(
        text="mondo_0014108",
        description="Fanconi Anemia Type Q - ERCC4",
        meaning=MONDO["0014108"])
    mondo_0014986 = PermissibleValue(
        text="mondo_0014986",
        description="Fanconi Anemia Type R - RAD51",
        meaning=MONDO["0014986"])
    mondo_0054748 = PermissibleValue(
        text="mondo_0054748",
        description="Fanconi Anemia Type S - BRCA1",
        meaning=MONDO["0054748"])
    mondo_0014638 = PermissibleValue(
        text="mondo_0014638",
        description="Fanconi Anemia Type T - UBE2T",
        meaning=MONDO["0014638"])
    mondo_0014987 = PermissibleValue(
        text="mondo_0014987",
        description="Fanconi Anemia Type U - XRCC2",
        meaning=MONDO["0014987"])
    mondo_0014985 = PermissibleValue(
        text="mondo_0014985",
        description="Fanconi Anemia Type V - MAD2L2",
        meaning=MONDO["0014985"])
    mondo_0044325 = PermissibleValue(
        text="mondo_0044325",
        description="Fanconia Anemia Type W - RFWD3",
        meaning=MONDO["0044325"])
    mondo_0030898 = PermissibleValue(
        text="mondo_0030898",
        description="FCHO1 deficiency - FCHO1",
        meaning=MONDO["0030898"])
    mondo_0008260 = PermissibleValue(
        text="mondo_0008260",
        description="FERMT1 deficiency (Kindler syndrome) - FERMT1",
        meaning=MONDO["0008260"])
    mondo_0013467 = PermissibleValue(
        text="mondo_0013467",
        description="Ficolin 3 deficiency - FCN3",
        meaning=MONDO["0013467"])
    flt3l_deficiency = PermissibleValue(
        text="flt3l_deficiency",
        description="FLT3L deficiency - FLT3LG",
        meaning=CIEINR["flt3l_deficiency"])
    mondo_0957955 = PermissibleValue(
        text="mondo_0957955",
        description="Folate malabsorption - SLC19A1",
        meaning=MONDO["0957955"])
    mondo_0958194 = PermissibleValue(
        text="mondo_0958194",
        description="FOXI3 Haploinsufficiency - FOXI3",
        meaning=MONDO["0958194"])
    mondo_0011132 = PermissibleValue(
        text="mondo_0011132",
        description="Winged helix FOXN1 deficiency (Nude SCID) - FOXN1",
        meaning=MONDO["0011132"])
    mondo_0032928 = PermissibleValue(
        text="mondo_0032928",
        description="FOXN1 Haplosufficiency - FOXN1",
        meaning=MONDO["0032928"])
    mondo_0030528 = PermissibleValue(
        text="mondo_0030528",
        description="FNIP1 deficiency - FNIP1",
        meaning=MONDO["0030528"])
    mondo_0010480 = PermissibleValue(
        text="mondo_0010480",
        description="G6PD deficiency Class I - G6PD",
        meaning=MONDO["0010480"])
    mondo_0012930 = PermissibleValue(
        text="mondo_0012930",
        description="G6PC3 deficiency (SCN4) - G6PC3",
        meaning=MONDO["0012930"])
    mondo_0014865 = PermissibleValue(
        text="mondo_0014865",
        description="G-CSF receptor deficiency - CSF3R",
        meaning=MONDO["0014865"])
    mondo_0013607 = PermissibleValue(
        text="mondo_0013607",
        description="GATA2 deficiency (MonoMac syndrome) - GATA2",
        meaning=MONDO["0013607"])
    mondo_0010315 = PermissibleValue(
        text="mondo_0010315",
        description="gc deficiency (common gamma chain SCID, CD132 deficiency) - IL2RG",
        meaning=MONDO["0010315"])
    mondo_0013139 = PermissibleValue(
        text="mondo_0013139",
        description="GFI 1 deficiency (SCN2) - GFI1",
        meaning=MONDO["0013139"])
    mondo_0011922 = PermissibleValue(
        text="mondo_0011922",
        description="GFI 1 deficiency (SCN2) - GFI1",
        meaning=MONDO["0011922"])
    mondo_0030397 = PermissibleValue(
        text="mondo_0030397",
        description="GIMAP5 deficiency - GIMAP5",
        meaning=MONDO["0030397"])
    gimap6_deficiency = PermissibleValue(
        text="gimap6_deficiency",
        description="GIMAP6 deficiency - GIMAP6",
        meaning=CIEINR["gimap6_deficiency"])
    gins4_deficiency = PermissibleValue(
        text="gins4_deficiency",
        description="GINS4 deficiency - GINS4",
        meaning=CIEINR["gins4_deficiency"])
    mondo_0009288 = PermissibleValue(
        text="mondo_0009288",
        description="Glycogen storage disease type 1b - G6PT1",
        meaning=MONDO["0009288"])
    mondo_0011872 = PermissibleValue(
        text="mondo_0011872",
        description="Griscelli syndrome, type 2 - RAB27A",
        meaning=MONDO["0011872"])
    gtf3a_deficiency = PermissibleValue(
        text="gtf3a_deficiency",
        description="GTF3A deficiency - GTF3A",
        meaning=CIEINR["gtf3a_deficiency"])
    mondo_0012548 = PermissibleValue(
        text="mondo_0012548",
        description="HAX1 deficiency (Kostmann Disease) (SCN3) - HAX1",
        meaning=MONDO["0012548"])
    mondo_0033551 = PermissibleValue(
        text="mondo_0033551",
        description="HEM1 (NCKAP1L) deficiency - NCKAP1L",
        meaning=MONDO["0033551"])
    mondo_0009337 = PermissibleValue(
        text="mondo_0009337",
        description="Hennekam-lymphangiectasia-lymphedema syndrome due to CCBE1 deficiency - CCBE1",
        meaning=MONDO["0009337"])
    mondo_0014454 = PermissibleValue(
        text="mondo_0014454",
        description="Hennekam-lymphangiectasia-lymphedema syndrome due to FAT4 deficiency - FAT4",
        meaning=MONDO["0014454"])
    mondo_0011997 = PermissibleValue(
        text="mondo_0011997",
        description="Hermansky-Pudlak syndrome, type 2 - AP3B1",
        meaning=MONDO["0011997"])
    mondo_0014885 = PermissibleValue(
        text="mondo_0014885",
        description="Hermansky-Pudlak syndrome, type 10 - AP3D1",
        meaning=MONDO["0014885"])
    mondo_0800140 = PermissibleValue(
        text="mondo_0800140",
        description="ITPKB deficiency - ITPKB",
        meaning=MONDO["0800140"])
    mondo_0009305 = PermissibleValue(
        text="mondo_0009305",
        description="HYOU1 deficiency - HYOU1",
        meaning=MONDO["0009305"])
    mondo_0013536 = PermissibleValue(
        text="mondo_0013536",
        description="Isolated congenital asplenia (ICA) due to HMOX deficiency - HMOX1",
        meaning=MONDO["0013536"])
    mondo_0012243 = PermissibleValue(
        text="mondo_0012243",
        description="Hoffman syndrome/TOP2B deficiency - TOP2B",
        meaning=MONDO["0012243"])
    mondo_0011273 = PermissibleValue(
        text="mondo_0011273",
        description="""Hyperpigmentation hypertrichosis, histiocytosis-lymphadenopathy plus syndrome SLC29A3 mutation - SLC29A3""",
        meaning=MONDO["0011273"])
    mondo_0011864 = PermissibleValue(
        text="mondo_0011864",
        description="ICOS deficiency - ICOS",
        meaning=MONDO["0011864"])
    mondo_0970993 = PermissibleValue(
        text="mondo_0970993",
        description="ICOLG deficiency - ICOSLG",
        meaning=MONDO["0970993"])
    mondo_0033541 = PermissibleValue(
        text="mondo_0033541",
        description="IFNG deficiency - IFNG",
        meaning=MONDO["0033541"])
    mondo_0030970 = PermissibleValue(
        text="mondo_0030970",
        description="IFNAR1 deficiency - IFNAR1",
        meaning=MONDO["0030970"])
    mondo_0014727 = PermissibleValue(
        text="mondo_0014727",
        description="IFNAR2 deficiency - IFNAR2",
        meaning=MONDO["0014727"])
    mondo_0014828 = PermissibleValue(
        text="mondo_0014828",
        description="Immunodeficiency with centromeric instability and facial anomalies (ICF3) - CDCA7",
        meaning=MONDO["0014828"])
    mondo_0009454 = PermissibleValue(
        text="mondo_0009454",
        description="Immunodeficiency with centromeric instability and facial anomalies (ICF1) - DNMT3B",
        meaning=MONDO["0009454"])
    mondo_0013553 = PermissibleValue(
        text="mondo_0013553",
        description="Immunodeficiency with centromeric instability and facial anomalies (ICF2) - ZBTB24",
        meaning=MONDO["0013553"])
    mondo_0014829 = PermissibleValue(
        text="mondo_0014829",
        description="Immunodeficiency with centromeric instability and facial anomalies (ICF4) - HELLS",
        meaning=MONDO["0014829"])
    mondo_0800030 = PermissibleValue(
        text="mondo_0800030",
        description="Immunodeficiency with multiple intestinal atresias - TTC7A",
        meaning=MONDO["0800030"])
    mondo_0044312 = PermissibleValue(
        text="mondo_0044312",
        description="Immunoskeletal dysplasia with neurodevelopmental abnormalities (EXTL3 Deficiency) - EXTL3",
        meaning=MONDO["0044312"])
    mondo_0014810 = PermissibleValue(
        text="mondo_0014810",
        description="IKAROS haplosufficiency / GOF / deficiency - IKZF1",
        meaning=MONDO["0014810"])
    ikzf2_dn = PermissibleValue(
        text="ikzf2_dn",
        description="IKZF2 DN - IKZF2",
        meaning=CIEINR["ikzf2_dn"])
    mondo_0800139 = PermissibleValue(
        text="mondo_0800139",
        description="IKZF2 deficiency (AD / AR) - IKZF2",
        meaning=MONDO["0800139"])
    mondo_0030333 = PermissibleValue(
        text="mondo_0030333",
        description="AIOLOS deficiency - IKZF3",
        meaning=MONDO["0030333"])
    mondo_0014267 = PermissibleValue(
        text="mondo_0014267",
        description="IKBKB deficiency (AR) - IKBKB",
        meaning=MONDO["0014267"])
    ikbke_deficiency = PermissibleValue(
        text="ikbke_deficiency",
        description="IKBKE deficiency - IKBKE",
        meaning=CIEINR["ikbke_deficiency"])
    mondo_0012163 = PermissibleValue(
        text="mondo_0012163",
        description="IL7Ra deficiency - IL7R",
        meaning=MONDO["0012163"])
    mondo_0009413 = PermissibleValue(
        text="mondo_0009413",
        description="TACI deficiency (IL-21 deficiency) - TNFRSF13B",
        meaning=MONDO["0009413"])
    mondo_0014082 = PermissibleValue(
        text="mondo_0014082",
        description="IL-21R deficiency - IL21R",
        meaning=MONDO["0014082"])
    mondo_0014338 = PermissibleValue(
        text="mondo_0014338",
        description="IL-21 deficiency - IL21",
        meaning=MONDO["0014338"])
    mondo_0013153 = PermissibleValue(
        text="mondo_0013153",
        description="IL-10Ra deficiency - IL10RA",
        meaning=MONDO["0013153"])
    mondo_0012941 = PermissibleValue(
        text="mondo_0012941",
        description="IL-10Rb deficiency - IL10RB",
        meaning=MONDO["0012941"])
    mondo_0016542 = PermissibleValue(
        text="mondo_0016542",
        description="IL-10 deficiency - IL10",
        meaning=MONDO["0016542"])
    mondo_0013503 = PermissibleValue(
        text="mondo_0013503",
        description="IL-17F deficiency - IL17F",
        meaning=MONDO["0013503"])
    mondo_0013500 = PermissibleValue(
        text="mondo_0013500",
        description="IL-17RA deficiency - IL17RA",
        meaning=MONDO["0013500"])
    mondo_0014642 = PermissibleValue(
        text="mondo_0014642",
        description="IL-17RC deficiency - IL17RC",
        meaning=MONDO["0014642"])
    mondo_0032809 = PermissibleValue(
        text="mondo_0032809",
        description="IL-18BP deficiency - IL18BP",
        meaning=MONDO["0032809"])
    mondo_0030069 = PermissibleValue(
        text="mondo_0030069",
        description="IL6 receptor deficiency - IL6R",
        meaning=MONDO["0030069"])
    mondo_0800131 = PermissibleValue(
        text="mondo_0800131",
        description="IL6 signal transducer (IL6ST) deficiency (AR) - IL6ST",
        meaning=MONDO["0800131"])
    mondo_0032796 = PermissibleValue(
        text="mondo_0032796",
        description="IL6 signal transducer (IL6ST) deficiency (AD) - IL6ST",
        meaning=MONDO["0032796"])
    il_12rb2_deficiency = PermissibleValue(
        text="il_12rb2_deficiency",
        description="IL-12Rb2 deficiency - IL12RB2",
        meaning=CIEINR["il_12rb2_deficiency"])
    mondo_0013954 = PermissibleValue(
        text="mondo_0013954",
        description="IL-12p40 (IL-12 and IL-23) deficiency - IL12B",
        meaning=MONDO["0013954"])
    mondo_0013955 = PermissibleValue(
        text="mondo_0013955",
        description="IL-12 and IL-23 receptor b1 chain deficiency - IL12RB1",
        meaning=MONDO["0013955"])
    il_23r_deficiency = PermissibleValue(
        text="il_23r_deficiency",
        description="IL-23R deficiency - IL23R",
        meaning=CIEINR["il_23r_deficiency"])
    il_27ra_deficiency = PermissibleValue(
        text="il_27ra_deficiency",
        description="IL-27RA deficiency - IL27RA",
        meaning=CIEINR["il_27ra_deficiency"])
    mondo_0019464 = PermissibleValue(
        text="mondo_0019464",
        description="Ig heavy chain mutations and deletions - 14q32 deletion or mutation",
        meaning=MONDO["0019464"])
    mondo_0013288 = PermissibleValue(
        text="mondo_0013288",
        description="Iga deficiency - CD79A",
        meaning=MONDO["0013288"])
    mondo_0012987 = PermissibleValue(
        text="mondo_0012987",
        description="Igb deficiency - CD79B",
        meaning=MONDO["0012987"])
    mondo_0001341 = PermissibleValue(
        text="mondo_0001341",
        description="Selective IgA deficiency - Unknown",
        meaning=MONDO["0001341"])
    mondo_0001901 = PermissibleValue(
        text="mondo_0001901",
        description="Isolated IgG subclass deficiency - Unknown",
        meaning=MONDO["0001901"])
    mondo_0013576 = PermissibleValue(
        text="mondo_0013576",
        description="Kappa chain deficiency / IgG subclass deficiency with IgA deficiency - IGKC",
        meaning=MONDO["0013576"])
    mondo_0018039 = PermissibleValue(
        text="mondo_0018039",
        description="Selective IgM deficiency - Unknown",
        meaning=MONDO["0018039"])
    mondo_0014680 = PermissibleValue(
        text="mondo_0014680",
        description="IRF3 deficiency - IRF3",
        meaning=MONDO["0014680"])
    mondo_0958011 = PermissibleValue(
        text="mondo_0958011",
        description="IRF1 deficiency - IRF1",
        meaning=MONDO["0958011"])
    mondo_0054691 = PermissibleValue(
        text="mondo_0054691",
        description="IRF2BP2 deficiency - IRF2BP2",
        meaning=MONDO["0054691"])
    irf4_haplosufficiency = PermissibleValue(
        text="irf4_haplosufficiency",
        description="IRF4 haplosufficiency - IRF4",
        meaning=CIEINR["irf4_haplosufficiency"])
    irf4_multimorphic_r95t = PermissibleValue(
        text="irf4_multimorphic_r95t",
        description="IRF4 multimorphic R95T - IRF4",
        meaning=CIEINR["irf4_multimorphic_r95t"])
    mondo_0013957 = PermissibleValue(
        text="mondo_0013957",
        description="IRF8 deficiency (AD) - IRF8",
        meaning=MONDO["0013957"])
    mondo_0009194 = PermissibleValue(
        text="mondo_0009194",
        description="IRF8 deficiency (AR) - IRF8",
        meaning=MONDO["0009194"])
    mondo_0014597 = PermissibleValue(
        text="mondo_0014597",
        description="IRF7 deficiency - IRF7",
        meaning=MONDO["0014597"])
    mondo_0032848 = PermissibleValue(
        text="mondo_0032848",
        description="IRF9 deficiency - IRF9",
        meaning=MONDO["0032848"])
    irak1_deficiency = PermissibleValue(
        text="irak1_deficiency",
        description="IRAK1 deficiency - IRAK1",
        meaning=CIEINR["irak1_deficiency"])
    mondo_0011888 = PermissibleValue(
        text="mondo_0011888",
        description="IRAK4 deficiency - IRAK4",
        meaning=MONDO["0011888"])
    irak4_disorder = PermissibleValue(
        text="irak4_disorder",
        description="IRAK4 disorder - IRAK4",
        meaning=CIEINR["irak4_disorder"])
    ire1a_deficiency = PermissibleValue(
        text="ire1a_deficiency",
        description="IRE1a deficiency - ERN1",
        meaning=CIEINR["ire1a_deficiency"])
    mondo_0014502 = PermissibleValue(
        text="mondo_0014502",
        description="ISG15 deficiency - ISG15",
        meaning=MONDO["0014502"])
    mondo_0013081 = PermissibleValue(
        text="mondo_0013081",
        description="ITK deficiency - ITK",
        meaning=MONDO["0013081"])
    mondo_0859311 = PermissibleValue(
        text="mondo_0859311",
        description="ITPR3 - ITPR3",
        meaning=MONDO["0859311"])
    mondo_0013245 = PermissibleValue(
        text="mondo_0013245",
        description="ITCH deficiency - ITCH",
        meaning=MONDO["0013245"])
    mondo_0033558 = PermissibleValue(
        text="mondo_0033558",
        description="JAK1 GOF / LOF - JAK1",
        meaning=MONDO["0033558"])
    mondo_0010938 = PermissibleValue(
        text="mondo_0010938",
        description="JAK3 deficiency - JAK3",
        meaning=MONDO["0010938"])
    mondo_0014456 = PermissibleValue(
        text="mondo_0014456",
        description="JAGN1 deficiency - JAGN1",
        meaning=MONDO["0014456"])
    mondo_0010465 = PermissibleValue(
        text="mondo_0010465",
        description="Kabuki Syndrome 2 due to KDM6A deficiency - KDM6A",
        meaning=MONDO["0010465"])
    mondo_0007843 = PermissibleValue(
        text="mondo_0007843",
        description="Kabuki Syndrome 1 due to KMT2D deficiency - KMT2D (MLL2)",
        meaning=MONDO["0007843"])
    mondo_0030893 = PermissibleValue(
        text="mondo_0030893",
        description="KARS1 deficiency - KARS1",
        meaning=MONDO["0030893"])
    mondo_0044721 = PermissibleValue(
        text="mondo_0044721",
        description="LAT deficiency - LAT",
        meaning=MONDO["0044721"])
    mondo_0030693 = PermissibleValue(
        text="mondo_0030693",
        description="Ligase I deficiency - LIG1",
        meaning=MONDO["0030693"])
    mondo_0013863 = PermissibleValue(
        text="mondo_0013863",
        description="LRBA deficiency - LRBA",
        meaning=MONDO["0013863"])
    mondo_0007293 = PermissibleValue(
        text="mondo_0007293",
        description="Leukocyte adhesion deficiency type 1 (LAD1) - ITGB2",
        meaning=MONDO["0007293"])
    mondo_0009953 = PermissibleValue(
        text="mondo_0009953",
        description="Leukocyte adhesion deficiency type 2 (LAD2) - SLC35C1",
        meaning=MONDO["0009953"])
    mondo_0013016 = PermissibleValue(
        text="mondo_0013016",
        description="Leukocyte adhesion deficiency type 3 (LAD3) - FERMT3",
        meaning=MONDO["0013016"])
    mondo_0030366 = PermissibleValue(
        text="mondo_0030366",
        description="LITAF deficiency - Unknown",
        meaning=MONDO["0030366"])
    mondo_0012212 = PermissibleValue(
        text="mondo_0012212",
        description="Loeys Dietz syndrome due to TGFBR1 deficiency - TGFBR1",
        meaning=MONDO["0012212"])
    mondo_0012427 = PermissibleValue(
        text="mondo_0012427",
        description="Loeys Dietz syndrome due to TGFBR2 deficiency - TGFBR2",
        meaning=MONDO["0012427"])
    mondo_0018643 = PermissibleValue(
        text="mondo_0018643",
        description="Localized juvenile periodontitis - FPR1",
        meaning=MONDO["0018643"])
    mondo_0013287 = PermissibleValue(
        text="mondo_0013287",
        description="l5 deficiency - IGLL1",
        meaning=MONDO["0013287"])
    mondo_0009109 = PermissibleValue(
        text="mondo_0009109",
        description="Lysinuric protein intolerance SLC7A7 deficiency - SLC7A7",
        meaning=MONDO["0009109"])
    mondo_0957271 = PermissibleValue(
        text="mondo_0957271",
        description="LYN GOF disease - LYN",
        meaning=MONDO["0957271"])
    mondo_0010389 = PermissibleValue(
        text="mondo_0010389",
        description="""gp91 phox deficiency Macrophage /  X-linked chronic granulomatous disease (CGD), gp91phox - CYBB""",
        meaning=MONDO["0010389"])
    mondo_0013040 = PermissibleValue(
        text="mondo_0013040",
        description="Membrane Cofactor Protein (CD46) deficiency (AD / AR) - CD46",
        meaning=MONDO["0013040"])
    mondo_0012858 = PermissibleValue(
        text="mondo_0012858",
        description="Membrane Attack Complex Inhibitor (CD59) deficiency - CD59",
        meaning=MONDO["0012858"])
    mondo_0013423 = PermissibleValue(
        text="mondo_0013423",
        description="MASP2 deficiency - MASP2",
        meaning=MONDO["0013423"])
    mondo_0014197 = PermissibleValue(
        text="mondo_0014197",
        description="MALT1 deficiency - MALT1",
        meaning=MONDO["0014197"])
    mondo_0020729 = PermissibleValue(
        text="mondo_0020729",
        description="m heavy chain deficiency - IGHM",
        meaning=MONDO["0020729"])
    mondo_0800141 = PermissibleValue(
        text="mondo_0800141",
        description="MAN2B2 deficiency - MAN2B2",
        meaning=MONDO["0800141"])
    mondo_0011629 = PermissibleValue(
        text="mondo_0011629",
        description="Mannosyl-oligosaccharide glucosidase deficiency (MOGS) - MOGS (GCS1)",
        meaning=MONDO["0011629"])
    map1lc3b2_deficiency = PermissibleValue(
        text="map1lc3b2_deficiency",
        description="MAP1LC3B2 - MAP1LC3B2",
        meaning=CIEINR["map1lc3b2_deficiency"])
    mondo_0800142 = PermissibleValue(
        text="mondo_0800142",
        description="MAPK8 deficiency - MAPK8",
        meaning=MONDO["0800142"])
    mondo_0030266 = PermissibleValue(
        text="mondo_0030266",
        description="MCM10 deficiency - MCM10",
        meaning=MONDO["0030266"])
    mondo_0012383 = PermissibleValue(
        text="mondo_0012383",
        description="MCM4 deficiency - MCM4",
        meaning=MONDO["0012383"])
    md2_deficiency = PermissibleValue(
        text="md2_deficiency",
        description="MD2 deficiency - LY96",
        meaning=CIEINR["md2_deficiency"])
    mondo_0958030 = PermissibleValue(
        text="mondo_0958030",
        description="MCTS1 deficiency - MCTS1",
        meaning=MONDO["0958030"])
    mondo_0060611 = PermissibleValue(
        text="mondo_0060611",
        description="Methylene-tetrahydrofolate dehydrogenase 1 (MTHFD1) deficiency - MTHFD1",
        meaning=MONDO["0060611"])
    mondo_0009849 = PermissibleValue(
        text="mondo_0009849",
        description="Mevalonate kinase deficiency (Hyper IgD syndrome) - MVK",
        meaning=MONDO["0009849"])
    mondo_0009434 = PermissibleValue(
        text="mondo_0009434",
        description="MHC class I deficiency - B2M",
        meaning=MONDO["0009434"])
    mondo_0971006 = PermissibleValue(
        text="mondo_0971006",
        description="MHC class I deficiency (TAP1) - TAP1",
        meaning=MONDO["0971006"])
    mondo_0971011 = PermissibleValue(
        text="mondo_0971011",
        description="MHC class I deficiency (TAP2) - TAP2",
        meaning=MONDO["0971011"])
    mondo_0971012 = PermissibleValue(
        text="mondo_0971012",
        description="MHC class I deficiency (TAPBP) - TAPBP",
        meaning=MONDO["0971012"])
    mondo_0971005 = PermissibleValue(
        text="mondo_0971005",
        description="MHC class II deficiency group A - CIITA",
        meaning=MONDO["0971005"])
    mondo_0971013 = PermissibleValue(
        text="mondo_0971013",
        description="MHC class II deficiency group B - RFXANK",
        meaning=MONDO["0971013"])
    mondo_0971014 = PermissibleValue(
        text="mondo_0971014",
        description="MHC class II deficiency group C - RFX5",
        meaning=MONDO["0971014"])
    mondo_0971015 = PermissibleValue(
        text="mondo_0971015",
        description="MHC class II deficiency group D - RFXAP",
        meaning=MONDO["0971015"])
    mondo_0010514 = PermissibleValue(
        text="mondo_0010514",
        description="Moesin deficiency - MSN",
        meaning=MONDO["0010514"])
    mondo_0008871 = PermissibleValue(
        text="mondo_0008871",
        description="MOPD1 deficiency (Roifman syndrome) - RNU4ATAC",
        meaning=MONDO["0008871"])
    mondo_0030841 = PermissibleValue(
        text="mondo_0030841",
        description="MSH6 - MSH6",
        meaning=MONDO["0030841"])
    mondo_0013934 = PermissibleValue(
        text="mondo_0013934",
        description="MST1 deficiency - STK4",
        meaning=MONDO["0013934"])
    mondo_0008633 = PermissibleValue(
        text="mondo_0008633",
        description="Muckle-Wells syndrome - NLRP3",
        meaning=MONDO["0008633"])
    mondo_0012839 = PermissibleValue(
        text="mondo_0012839",
        description="MyD88 deficiency - MYD88",
        meaning=MONDO["0012839"])
    mondo_0020856 = PermissibleValue(
        text="mondo_0020856",
        description="MYSM1 deficiency - MYSM1",
        meaning=MONDO["0020856"])
    mondo_0012316 = PermissibleValue(
        text="mondo_0012316",
        description="Majeed syndrome - LPIN2",
        meaning=MONDO["0012316"])
    mondo_0007728 = PermissibleValue(
        text="mondo_0007728",
        description="NCSTN deficiency hidradenitis suppurativa - NCSTN",
        meaning=MONDO["0007728"])
    mondo_0007686 = PermissibleValue(
        text="mondo_0007686",
        description="NBEAL2 deficiency - NBEAL2",
        meaning=MONDO["0007686"])
    mondo_0030013 = PermissibleValue(
        text="mondo_0030013",
        description="Neutropenia with combined immune deficiency due to MKL1 deficiency - MRTFA",
        meaning=MONDO["0030013"])
    nfat5_haploinsufficiency = PermissibleValue(
        text="nfat5_haploinsufficiency",
        description="NFAT5 haploinsufficiency - NFAT5",
        meaning=CIEINR["nfat5_haploinsufficiency"])
    mondo_0859369 = PermissibleValue(
        text="mondo_0859369",
        description="NFAT1 deficiency - NFATC2",
        meaning=MONDO["0859369"])
    nfatc1_deficiency = PermissibleValue(
        text="nfatc1_deficiency",
        description="NFATC1 deficiency - NFATC1",
        meaning=CIEINR["nfatc1_deficiency"])
    mondo_0014697 = PermissibleValue(
        text="mondo_0014697",
        description="NFKB1 deficiency - NFKB1",
        meaning=MONDO["0014697"])
    mondo_0014260 = PermissibleValue(
        text="mondo_0014260",
        description="NFKB2 deficiency - NFKB2",
        meaning=MONDO["0014260"])
    mondo_0060591 = PermissibleValue(
        text="mondo_0060591",
        description="NFE2L2 GOF - NFE2L2",
        meaning=MONDO["0060591"])
    mondo_0957535 = PermissibleValue(
        text="mondo_0957535",
        description="NIK deficiency - MAP3K14",
        meaning=MONDO["0957535"])
    mondo_0060457 = PermissibleValue(
        text="mondo_0060457",
        description="NLRP1 deficiency (AR) - NLRP1",
        meaning=MONDO["0060457"])
    mondo_0014089 = PermissibleValue(
        text="mondo_0014089",
        description="NLRP1 GOF (AD) - NLRP1",
        meaning=MONDO["0014089"])
    mondo_0011776 = PermissibleValue(
        text="mondo_0011776",
        description="""Neonatal onset multisystem inflammatory disease (NOMID) or chronic infantile neurologic cutaneous and articular syndrome (CINCA) - NLRP3""",
        meaning=MONDO["0011776"])
    nos2_deficiency = PermissibleValue(
        text="nos2_deficiency",
        description="NOS2 deficiency - NOS2",
        meaning=CIEINR["nos2_deficiency"])
    mondo_0014984 = PermissibleValue(
        text="mondo_0014984",
        description="NSMCE3 deficiency - NSMCE3",
        meaning=MONDO["0014984"])
    mondo_0009623 = PermissibleValue(
        text="mondo_0009623",
        description="Nijmegen breakage syndrome - NBN",
        meaning=MONDO["0009623"])
    nudcd3_deficiency = PermissibleValue(
        text="nudcd3_deficiency",
        description="NUDCD3 deficiency - NUDCD3",
        meaning=CIEINR["nudcd3_deficiency"])
    mondo_0020840 = PermissibleValue(
        text="mondo_0020840",
        description="OAS1 deficiency / GOF - OAS1",
        meaning=MONDO["0020840"])
    oas2_deficiency = PermissibleValue(
        text="oas2_deficiency",
        description="OAS2 deficiency - OAS2",
        meaning=CIEINR["oas2_deficiency"])
    mondo_0009817 = PermissibleValue(
        text="mondo_0009817",
        description="OSTM1 deficiency associated osteopetrosis - OSTM1",
        meaning=MONDO["0009817"])
    mondo_0031030 = PermissibleValue(
        text="mondo_0031030",
        description="Otulin deficiency - OTULIN",
        meaning=MONDO["0031030"])
    otulin_haplosufficiency = PermissibleValue(
        text="otulin_haplosufficiency",
        description="Otulin haplosufficiency - OTULIN",
        meaning=CIEINR["otulin_haplosufficiency"])
    mondo_0014912 = PermissibleValue(
        text="mondo_0014912",
        description="Otulipenia/ORAS - OTULIN",
        meaning=MONDO["0014912"])
    mondo_0014268 = PermissibleValue(
        text="mondo_0014268",
        description="OX40 deficiency - TNFRSF4",
        meaning=MONDO["0014268"])
    mondo_0014389 = PermissibleValue(
        text="mondo_0014389",
        description="HOIL1 deficiency - RBCK1",
        meaning=MONDO["0014389"])
    mondo_0957981 = PermissibleValue(
        text="mondo_0957981",
        description="HOIP deficiency - RNF31",
        meaning=MONDO["0957981"])
    mondo_0014383 = PermissibleValue(
        text="mondo_0014383",
        description="ORAI-1 deficiency - ORAI1",
        meaning=MONDO["0014383"])
    mondo_0012559 = PermissibleValue(
        text="mondo_0012559",
        description="P14/LAMTOR2 deficiency - LAMTOR2",
        meaning=MONDO["0012559"])
    mondo_0010455 = PermissibleValue(
        text="mondo_0010455",
        description="PAX1 deficiency - PAX1",
        meaning=MONDO["0010455"])
    mondo_0100299 = PermissibleValue(
        text="mondo_0100299",
        description="PAX5 deficiency - PAX5",
        meaning=MONDO["0100299"])
    mondo_0011462 = PermissibleValue(
        text="mondo_0011462",
        description="""Pyogenic sterile arthritis, pyoderma gangrenosum, acne (PAPA) syndrome, hyperzincemia and hypercalprotectinemia - PSTPIP1""",
        meaning=MONDO["0011462"])
    mondo_0009490 = PermissibleValue(
        text="mondo_0009490",
        description="Papillon-Lefèvre Syndrome - CTSC",
        meaning=MONDO["0009490"])
    mondo_0021571 = PermissibleValue(
        text="mondo_0021571",
        description="PD1 deficiency - PDCD1",
        meaning=MONDO["0021571"])
    pd_l1_deficiency = PermissibleValue(
        text="pd_l1_deficiency",
        description="PD-L1 deficiency - CD274",
        meaning=CIEINR["pd_l1_deficiency"])
    mondo_0011337 = PermissibleValue(
        text="mondo_0011337",
        description="Perforin deficiency (FHL2) - PRF1",
        meaning=MONDO["0011337"])
    mondo_0014353 = PermissibleValue(
        text="mondo_0014353",
        description="PGM3 deficiency - PGM3",
        meaning=MONDO["0014353"])
    mondo_0957497 = PermissibleValue(
        text="mondo_0957497",
        description="Pansclerotic morphea - STAT4",
        meaning=MONDO["0957497"])
    mondo_0023655 = PermissibleValue(
        text="mondo_0023655",
        description="PIK3CD deficiency (AR) - PIK3CD",
        meaning=MONDO["0023655"])
    mondo_0014222 = PermissibleValue(
        text="mondo_0014222",
        description="PIK3CD mutation (GOF) APDS1 (AD) - PIK3CD GOF",
        meaning=MONDO["0014222"])
    mondo_0030717 = PermissibleValue(
        text="mondo_0030717",
        description="PIK3CG deficiency - PIK3CG",
        meaning=MONDO["0030717"])
    mondo_0014083 = PermissibleValue(
        text="mondo_0014083",
        description="PIK3R1 deficiency (AR) - PIK3R1",
        meaning=MONDO["0014083"])
    mondo_0014453 = PermissibleValue(
        text="mondo_0014453",
        description="PIK3R1 deficiency (LOF) APDS2 - PIK3R1",
        meaning=MONDO["0014453"])
    mondo_0012679 = PermissibleValue(
        text="mondo_0012679",
        description="PLEKHM1 deficiency associated osteopetrosis - PLEKHM1",
        meaning=MONDO["0012679"])
    mondo_0957790 = PermissibleValue(
        text="mondo_0957790",
        description="PLCG1 GOF disease - PLCG1",
        meaning=MONDO["0957790"])
    mondo_0013944 = PermissibleValue(
        text="mondo_0013944",
        description="""PLAID (PLCg2 associated antibody deficiency and immune dysregulation) or APLAID (c2120A>C) - PLCG2""",
        meaning=MONDO["0013944"])
    mondo_0030843 = PermissibleValue(
        text="mondo_0030843",
        description="PMS2 Deficiency - PMS2",
        meaning=MONDO["0030843"])
    mondo_0970994 = PermissibleValue(
        text="mondo_0970994",
        description="Polymerase d 1 deficiency - POLD1",
        meaning=MONDO["0970994"])
    pold2_deficiency = PermissibleValue(
        text="pold2_deficiency",
        description="Polymerase d 2 deficiency - POLD2",
        meaning=CIEINR["pold2_deficiency"])
    pold3_deficiency = PermissibleValue(
        text="pold3_deficiency",
        description="Polymerase d 3 deficiency - POLD3",
        meaning=CIEINR["pold3_deficiency"])
    mondo_0014058 = PermissibleValue(
        text="mondo_0014058",
        description="POLE1 (Polymerase ε subunit 1) deficiency (FILS syndrome) - POLE1",
        meaning=MONDO["0014058"])
    mondo_0800128 = PermissibleValue(
        text="mondo_0800128",
        description="POLE2 (Polymerase ε subunit 2) deficiency - POLE2",
        meaning=MONDO["0800128"])
    mondo_0009910 = PermissibleValue(
        text="mondo_0009910",
        description="RNA polymerase III deficiency due to POLR3A defects - POLR3A",
        meaning=MONDO["0009910"])
    polr3c_deficiency = PermissibleValue(
        text="polr3c_deficiency",
        description="RNA polymerase III deficiency due to POLR3C defects - POLR3C",
        meaning=CIEINR["polr3c_deficiency"])
    mondo_0030813 = PermissibleValue(
        text="mondo_0030813",
        description="RNA polymerase III deficiency due to POLR3F defects - POLR3F",
        meaning=MONDO["0030813"])
    mondo_0800146 = PermissibleValue(
        text="mondo_0800146",
        description="POU2AF1 deficiency - POU2AF1",
        meaning=MONDO["0800146"])
    mondo_0054700 = PermissibleValue(
        text="mondo_0054700",
        description="PRAID - POMP",
        meaning=MONDO["0054700"])
    mondo_0030924 = PermissibleValue(
        text="mondo_0030924",
        description="PRAAS- CANDLE (PSMB10) - PSMB10",
        meaning=MONDO["0030924"])
    mondo_0054699 = PermissibleValue(
        text="mondo_0054699",
        description="PRAAS- CANDLE (PSMB4) - PSMB4",
        meaning=MONDO["0054699"])
    mondo_0968983 = PermissibleValue(
        text="mondo_0968983",
        description="PRAAS -like condition (AD, AR, and various) - PSMB9",
        meaning=MONDO["0968983"])
    mondo_0971001 = PermissibleValue(
        text="mondo_0971001",
        description="PSMB10 associated Omenn Syndrome - PSMB10",
        meaning=MONDO["0971001"])
    mondo_0054591 = PermissibleValue(
        text="mondo_0054591",
        description="PSMD12 disorder - PSMD12",
        meaning=MONDO["0054591"])
    mondo_0024516 = PermissibleValue(
        text="mondo_0024516",
        description="PSEN deficiency hidradenitis suppurativa - PSEN",
        meaning=MONDO["0024516"])
    mondo_0013397 = PermissibleValue(
        text="mondo_0013397",
        description="PSENEN deficiency hidradenitis suppurativa - PSENEN",
        meaning=MONDO["0013397"])
    pten_deficiency = PermissibleValue(
        text="pten_deficiency",
        description="PTEN Deficiency (LOF) - PTEN",
        meaning=CIEINR["pten_deficiency"])
    ptcra_deficiency = PermissibleValue(
        text="ptcra_deficiency",
        description="PTCRA deficiency - PTCRA",
        meaning=CIEINR["ptcra_deficiency"])
    mondo_0010713 = PermissibleValue(
        text="mondo_0010713",
        description="Properdin deficiency - CFP",
        meaning=MONDO["0010713"])
    mondo_0008221 = PermissibleValue(
        text="mondo_0008221",
        description="Prolidase deficiency - PEPD",
        meaning=MONDO["0008221"])
    mondo_0013171 = PermissibleValue(
        text="mondo_0013171",
        description="Purine nucleoside phosphorylase (PNP) deficiency - PNP",
        meaning=MONDO["0013171"])
    mondo_0030529 = PermissibleValue(
        text="mondo_0030529",
        description="Pu.1 deficiency - SPI1",
        meaning=MONDO["0030529"])
    mondo_0000572 = PermissibleValue(
        text="mondo_0000572",
        description="RAG1 deficiency - RAG1",
        meaning=MONDO["0000572"])
    mondo_0000573 = PermissibleValue(
        text="mondo_0000573",
        description="RAG2 deficiency - RAG2",
        meaning=MONDO["0000573"])
    mondo_0033555 = PermissibleValue(
        text="mondo_0033555",
        description="RAC2 deficiency (AR) - RAC2",
        meaning=MONDO["0033555"])
    mondo_0011988 = PermissibleValue(
        text="mondo_0011988",
        description="Rac 2 deficiency (LOF) - RAC2",
        meaning=MONDO["0011988"])
    mondo_0013118 = PermissibleValue(
        text="mondo_0013118",
        description="RAD50 deficiency - RAD50",
        meaning=MONDO["0013118"])
    mondo_0032803 = PermissibleValue(
        text="mondo_0032803",
        description="RASGRP1 deficiency - RASGRP1",
        meaning=MONDO["0032803"])
    mondo_0030498 = PermissibleValue(
        text="mondo_0030498",
        description="c-Rel deficiency - REL",
        meaning=MONDO["0030498"])
    mondo_0032659 = PermissibleValue(
        text="mondo_0032659",
        description="RelA haplosufficiency - RELA",
        meaning=MONDO["0032659"])
    mondo_0054696 = PermissibleValue(
        text="mondo_0054696",
        description="RelB deficiency - RELB",
        meaning=MONDO["0054696"])
    rela_interferonopathy = PermissibleValue(
        text="rela_interferonopathy",
        description="RELA interferonopathy - RELA",
        meaning=MONDO["0032659"])
    mondo_0800147 = PermissibleValue(
        text="mondo_0800147",
        description="RHOG deficiency - RHOG",
        meaning=MONDO["0800147"])
    mondo_0029134 = PermissibleValue(
        text="mondo_0029134",
        description="RLTPR (CARMIL2) deficiency - CARMIL2",
        meaning=MONDO["0029134"])
    mondo_0017925 = PermissibleValue(
        text="mondo_0017925",
        description="Rhoh Deficiency - RHOH",
        meaning=MONDO["0017925"])
    mondo_0020849 = PermissibleValue(
        text="mondo_0020849",
        description="RIPK1 deficiency (AR) - RIPK1",
        meaning=MONDO["0020849"])
    mondo_0030018 = PermissibleValue(
        text="mondo_0030018",
        description="RIPK1 deficiency (AD) - RIPK1",
        meaning=MONDO["0030018"])
    ripk3_deficiency = PermissibleValue(
        text="ripk3_deficiency",
        description="RIPK3 deficiency - RIPK3",
        meaning=CIEINR["ripk3_deficiency"])
    mondo_0009973 = PermissibleValue(
        text="mondo_0009973",
        description="Reticular dysgenesis - AK2",
        meaning=MONDO["0009973"])
    mondo_0013999 = PermissibleValue(
        text="mondo_0013999",
        description="Retinal dystrophy, optic nerve oedema, splenomegaly, anhidrosis, and headache (ROSAH) - ALPK1",
        meaning=MONDO["0013999"])
    mondo_0014710 = PermissibleValue(
        text="mondo_0014710",
        description="RORgt deficiency - RORC",
        meaning=MONDO["0014710"])
    mondo_0011098 = PermissibleValue(
        text="mondo_0011098",
        description="RNASEL deficiency - RNASEL",
        meaning=MONDO["0011098"])
    mondo_0014367 = PermissibleValue(
        text="mondo_0014367",
        description="Aicardi-Goutieres syndrome 7 (AGS7) - IFIH1",
        meaning=MONDO["0014367"])
    mondo_0012472 = PermissibleValue(
        text="mondo_0012472",
        description="RNASEH2A deficiency, AGS4 - RNASEH2A",
        meaning=MONDO["0012472"])
    mondo_0012429 = PermissibleValue(
        text="mondo_0012429",
        description="RNASEH2B deficiency, AGS2 - RNASEH2B",
        meaning=MONDO["0012429"])
    mondo_0012471 = PermissibleValue(
        text="mondo_0012471",
        description="RNASEH2C deficiency, AGS3 - RNASEH2C",
        meaning=MONDO["0012471"])
    mondo_0012764 = PermissibleValue(
        text="mondo_0012764",
        description="RNF168 deficiency (RIDDLE Syndrome) - RNF168",
        meaning=MONDO["0012764"])
    mondo_0030362 = PermissibleValue(
        text="mondo_0030362",
        description="RNU7-1 deficiency - RNU7-1",
        meaning=MONDO["0030362"])
    mondo_0016369 = PermissibleValue(
        text="mondo_0016369",
        description="Rothmund-Thomson syndrome type 2 - RECQL4",
        meaning=MONDO["0016369"])
    mondo_0009955 = PermissibleValue(
        text="mondo_0009955",
        description="Rapadilino Syndrome - RECQL4",
        meaning=MONDO["0009955"])
    mondo_0010066 = PermissibleValue(
        text="mondo_0010066",
        description="Isolated congenital asplenia (ICA) due to RPSA deficiency - RPSA",
        meaning=MONDO["0010066"])
    mondo_0024781 = PermissibleValue(
        text="mondo_0024781",
        description="SASH3 deficiency - SASH3",
        meaning=MONDO["0024781"])
    mondo_0014888 = PermissibleValue(
        text="mondo_0014888",
        description="SAMD9 (GOF) - SAMD9",
        meaning=MONDO["0014888"])
    mondo_0013059 = PermissibleValue(
        text="mondo_0013059",
        description="SAMHD1 deficiency, AGS5 - SAMHD1",
        meaning=MONDO["0013059"])
    mondo_0958013 = PermissibleValue(
        text="mondo_0958013",
        description="SEC61A1 deficiency - SEC61A1",
        meaning=MONDO["0958013"])
    mondo_0044208 = PermissibleValue(
        text="mondo_0044208",
        description="SMARCD2 deficiency - SMARCD2",
        meaning=MONDO["0044208"])
    mondo_0030313 = PermissibleValue(
        text="mondo_0030313",
        description="SNORA31 deficiency - SNORA31",
        meaning=MONDO["0030313"])
    mondo_0800149 = PermissibleValue(
        text="mondo_0800149",
        description="TNFSF13 (APRIL) deficiency - TNFSF13",
        meaning=MONDO["0800149"])
    mondo_0008290 = PermissibleValue(
        text="mondo_0008290",
        description="PVMK deficiency - PMVK",
        meaning=MONDO["0008290"])
    mondo_0024551 = PermissibleValue(
        text="mondo_0024551",
        description="SH2D1A (SAP) deficiency (XLP1) - SH2D1A",
        meaning=MONDO["0024551"])
    mondo_0010296 = PermissibleValue(
        text="mondo_0010296",
        description="SH3KBP1 (CIN85) deficiency - SH3KBP1",
        meaning=MONDO["0010296"])
    sh2b3_deficiency = PermissibleValue(
        text="sh2b3_deficiency",
        description="SH2B3 deficiency - SH2B3",
        meaning=CIEINR["sh2b3_deficiency"])
    mondo_0968982 = PermissibleValue(
        text="mondo_0968982",
        description="SHARPIN deficiency - SHARPIN",
        meaning=MONDO["0968982"])
    mondo_0009458 = PermissibleValue(
        text="mondo_0009458",
        description="Schimke Immuno-osseous Dysplasia - SMARCAL1",
        meaning=MONDO["0009458"])
    sbds_deficiency = PermissibleValue(
        text="sbds_deficiency",
        description="Shwachman-Diamond Syndrome due to SBDS deficiency - SBDS",
        meaning=CIEINR["sbds_deficiency"])
    mondo_0009238 = PermissibleValue(
        text="mondo_0009238",
        description="SLC46A1/PCFT deficiency causing hereditary folate malabsorption - SLC46A1",
        meaning=MONDO["0009238"])
    mondo_0030519 = PermissibleValue(
        text="mondo_0030519",
        description="SLC39A7 (ZIP7) deficiency - SLC39A7",
        meaning=MONDO["0030519"])
    mondo_0030302 = PermissibleValue(
        text="mondo_0030302",
        description="SLP76 deficiency - LCP2",
        meaning=MONDO["0030302"])
    mondo_0014040 = PermissibleValue(
        text="mondo_0014040",
        description="SNX10 deficiency associated osteopetrosis - SNX10",
        meaning=MONDO["0014040"])
    mondo_0800130 = PermissibleValue(
        text="mondo_0800130",
        description="SOCS1 deficiency - SOCS1",
        meaning=MONDO["0800130"])
    mondo_0030448 = PermissibleValue(
        text="mondo_0030448",
        description="SPPL2a deficiency - SPPL2A",
        meaning=MONDO["0030448"])
    mondo_0009842 = PermissibleValue(
        text="mondo_0009842",
        description="Specific granule deficiency - CEBPE",
        meaning=MONDO["0009842"])
    srp19_deficiency = PermissibleValue(
        text="srp19_deficiency",
        description="SRP19 deficiency - SRP19",
        meaning=CIEINR["srp19_deficiency"])
    mondo_0032899 = PermissibleValue(
        text="mondo_0032899",
        description="SRP54 deficiency - SRP54",
        meaning=MONDO["0032899"])
    srpra_deficiency = PermissibleValue(
        text="srpra_deficiency",
        description="SRPRA deficiency - SRPRA",
        meaning=CIEINR["srpra_deficiency"])
    mondo_0013008 = PermissibleValue(
        text="mondo_0013008",
        description="STIM1 deficiency - STIM1",
        meaning=MONDO["0013008"])
    mondo_0013599 = PermissibleValue(
        text="mondo_0013599",
        description="STAT1 GOF - STAT1",
        meaning=MONDO["0013599"])
    mondo_0013956 = PermissibleValue(
        text="mondo_0013956",
        description="STAT1 deficiency (AD LOF) - STAT1",
        meaning=MONDO["0013956"])
    mondo_0013427 = PermissibleValue(
        text="mondo_0013427",
        description="STAT1 deficiency (AR LOF) - STAT1",
        meaning=MONDO["0013427"])
    mondo_0014715 = PermissibleValue(
        text="mondo_0014715",
        description="STAT2 deficiency - STAT2",
        meaning=MONDO["0014715"])
    mondo_0030044 = PermissibleValue(
        text="mondo_0030044",
        description="STAT2 GOF - STAT2",
        meaning=MONDO["0030044"])
    mondo_0014414 = PermissibleValue(
        text="mondo_0014414",
        description="STAT3 GOF mutation - STAT3",
        meaning=MONDO["0014414"])
    mondo_0100211 = PermissibleValue(
        text="mondo_0100211",
        description="STAT5b deficiency (AR) - STAT5B",
        meaning=MONDO["0100211"])
    mondo_0100219 = PermissibleValue(
        text="mondo_0100219",
        description="STAT5b deficiency (AD) - STAT5B",
        meaning=MONDO["0100219"])
    mondo_0957807 = PermissibleValue(
        text="mondo_0957807",
        description="STAT6 disorder - STAT6",
        meaning=MONDO["0957807"])
    mondo_0033203 = PermissibleValue(
        text="mondo_0033203",
        description="SGPL1 deficiency - SGPL1",
        meaning=MONDO["0033203"])
    mondo_0011336 = PermissibleValue(
        text="mondo_0011336",
        description="Syntaxin 11 deficiency (FHL4) - STX11",
        meaning=MONDO["0011336"])
    mondo_0013135 = PermissibleValue(
        text="mondo_0013135",
        description="STXBP2 / Munc18-2 deficiency (FHL5) - STXBP2",
        meaning=MONDO["0013135"])
    mondo_0030308 = PermissibleValue(
        text="mondo_0030308",
        description="SYK disease - SYK",
        meaning=MONDO["0030308"])
    mondo_0013818 = PermissibleValue(
        text="mondo_0013818",
        description="Tricho-hepato-enteric syndrome due to SKIV2L mutations - SKIV2L",
        meaning=MONDO["0013818"])
    mondo_0009735 = PermissibleValue(
        text="mondo_0009735",
        description="Comel-Netherton syndrome - SPINK5",
        meaning=MONDO["0009735"])
    mondo_0054754 = PermissibleValue(
        text="mondo_0054754",
        description="TBK1 deficiency (AD) - TBK1",
        meaning=MONDO["0054754"])
    mondo_0800148 = PermissibleValue(
        text="mondo_0800148",
        description="TBK1 deficiency (AR) - TBK1",
        meaning=MONDO["0800148"])
    mondo_0030483 = PermissibleValue(
        text="mondo_0030483",
        description="TBX21 deficiency - TBX21",
        meaning=MONDO["0030483"])
    mondo_0014160 = PermissibleValue(
        text="mondo_0014160",
        description="TCRα deficiency - TRAC",
        meaning=MONDO["0014160"])
    mondo_0030858 = PermissibleValue(
        text="mondo_0030858",
        description="TET2 deficiency - TET2",
        meaning=MONDO["0030858"])
    mondo_0014760 = PermissibleValue(
        text="mondo_0014760",
        description="TFRC deficiency - TFRC",
        meaning=MONDO["0014760"])
    mondo_0013723 = PermissibleValue(
        text="mondo_0013723",
        description="TIRAP deficiency - TIRAP",
        meaning=MONDO["0013723"])
    mondo_0800187 = PermissibleValue(
        text="mondo_0800187",
        description="TLR3 deficiency (AD / AR) - TLR3",
        meaning=MONDO["0800187"])
    mondo_0859083 = PermissibleValue(
        text="mondo_0859083",
        description="TLR7 deficiency (AD) - TLR7",
        meaning=MONDO["0859083"])
    mondo_0026767 = PermissibleValue(
        text="mondo_0026767",
        description="TLR7 deficiency (X-Linked) - TLR7",
        meaning=MONDO["0026767"])
    mondo_0024777 = PermissibleValue(
        text="mondo_0024777",
        description="TLR8 disease - TLR8",
        meaning=MONDO["0024777"])
    tlr4_deficiency = PermissibleValue(
        text="tlr4_deficiency",
        description="TLR4 deficiency - TLR4",
        meaning=CIEINR["tlr4_deficiency"])
    mondo_0015698 = PermissibleValue(
        text="mondo_0015698",
        description="Transient hypogammaglobulinemia of infancy - Unknown",
        meaning=MONDO["0015698"])
    mondo_0010149 = PermissibleValue(
        text="mondo_0010149",
        description="Transcobalamin 2 deficiency - TCN2",
        meaning=MONDO["0010149"])
    mondo_0013920 = PermissibleValue(
        text="mondo_0013920",
        description="TRAF3 deficiency / haplosufficiency - TRAF3",
        meaning=MONDO["0013920"])
    mondo_0012931 = PermissibleValue(
        text="mondo_0012931",
        description="Trypanosomiasis susceptibility - APOL1",
        meaning=MONDO["0012931"])
    mondo_0013921 = PermissibleValue(
        text="mondo_0013921",
        description="TRIF deficiency (AD / AR) - TICAM1",
        meaning=MONDO["0013921"])
    mondo_0035362 = PermissibleValue(
        text="mondo_0035362",
        description="TRIM22 - TRIM22",
        meaning=MONDO["0035362"])
    mondo_0014487 = PermissibleValue(
        text="mondo_0014487",
        description="TRNT1 deficiency - TRNT1",
        meaning=MONDO["0014487"])
    tripeptidyl_peptidase_ii_deficiency = PermissibleValue(
        text="tripeptidyl_peptidase_ii_deficiency",
        description="Tripeptidyl-Peptidase II Deficiency - TPP2",
        meaning=CIEINR["tripeptidyl_peptidase_ii_deficiency"])
    mondo_0024541 = PermissibleValue(
        text="mondo_0024541",
        description="Tricho-hepato-enteric syndrome due to TTC37 mutations - TTC37",
        meaning=MONDO["0024541"])
    mondo_0009815 = PermissibleValue(
        text="mondo_0009815",
        description="TCIRG1 deficiency associated osteopetrosis - TCIRG1",
        meaning=MONDO["0009815"])
    mondo_0007727 = PermissibleValue(
        text="mondo_0007727",
        description="TNF receptor-associated periodic syndrome (TRAPS) - TNFRSF1A",
        meaning=MONDO["0007727"])
    mondo_0012859 = PermissibleValue(
        text="mondo_0012859",
        description="TNFRSF11A deficiency associated osteopetrosis - TNFRSF11A",
        meaning=MONDO["0012859"])
    mondo_0009816 = PermissibleValue(
        text="mondo_0009816",
        description="TNFSF11 deficiency associated osteopetrosis - TNFSF11",
        meaning=MONDO["0009816"])
    tweak_deficiency = PermissibleValue(
        text="tweak_deficiency",
        description="TWEAK deficiency - TNFSF12",
        meaning=CIEINR["tweak_deficiency"])
    mondo_0012682 = PermissibleValue(
        text="mondo_0012682",
        description="Tyk2 deficiency / P1104A TYK2 homozygosity - TYK2",
        meaning=MONDO["0012682"])
    mondo_0012146 = PermissibleValue(
        text="mondo_0012146",
        description="UNC13D / Munc13-4 deficiency (FHL3) - UNC13D",
        meaning=MONDO["0012146"])
    mondo_0011971 = PermissibleValue(
        text="mondo_0011971",
        description="UNG deficiency - UNG",
        meaning=MONDO["0011971"])
    mondo_0024563 = PermissibleValue(
        text="mondo_0024563",
        description="UNC93B1 deficiency - UNC93B1",
        meaning=MONDO["0024563"])
    mondo_0018828 = PermissibleValue(
        text="mondo_0018828",
        description="USP18 deficiency - USP18",
        meaning=MONDO["0018828"])
    mondo_0009452 = PermissibleValue(
        text="mondo_0009452",
        description="Vici syndrome due to EPG5 deficiency - EPG5",
        meaning=MONDO["0009452"])
    mondo_0009338 = PermissibleValue(
        text="mondo_0009338",
        description="Hepatic veno-occlusive disease with immunodeficiency (VODI) - SP110",
        meaning=MONDO["0009338"])
    mondo_0014118 = PermissibleValue(
        text="mondo_0014118",
        description="VPS45 deficiency (SCN5) - VPS45",
        meaning=MONDO["0014118"])
    mondo_0007883 = PermissibleValue(
        text="mondo_0007883",
        description="WDR1 deficiency (Lazy leukocyte) - WDR1",
        meaning=MONDO["0007883"])
    mondo_0010518 = PermissibleValue(
        text="mondo_0010518",
        description="Wiskott-Aldrich syndrome (WAS LOF) - WAS",
        meaning=MONDO["0010518"])
    mondo_0013779 = PermissibleValue(
        text="mondo_0013779",
        description="WIP deficiency - WIPF1",
        meaning=MONDO["0013779"])
    mondo_8000006 = PermissibleValue(
        text="mondo_8000006",
        description="WHIM (Warts, Hypogammaglobulinemia, infections, Myelokathexis) syndrome - CXCR4",
        meaning=MONDO["8000006"])
    mondo_0011518 = PermissibleValue(
        text="mondo_0011518",
        description="Widemann-Steiner syndrome - KMT2A",
        meaning=MONDO["0011518"])
    mondo_0010385 = PermissibleValue(
        text="mondo_0010385",
        description="XIAP deficiency (XLP2) - XIAP",
        meaning=MONDO["0010385"])
    mondo_0010523 = PermissibleValue(
        text="mondo_0010523",
        description="X-linked reticulate pigmentary disorder-POLA1 - POLA1",
        meaning=MONDO["0010523"])
    mondo_0010294 = PermissibleValue(
        text="mondo_0010294",
        description="X-linked neutropenia/myelodysplasia WAS GOF - WAS",
        meaning=MONDO["0010294"])
    mondo_0010023 = PermissibleValue(
        text="mondo_0010023",
        description="ZAP-70 deficiency (ZAP70 LOF) - ZAP70",
        meaning=MONDO["0010023"])
    mondo_0014861 = PermissibleValue(
        text="mondo_0014861",
        description="ZAP70 combined hypomorphic GOF - ZAP70",
        meaning=MONDO["0014861"])
    mondo_0032654 = PermissibleValue(
        text="mondo_0032654",
        description="ZNF341 deficiency AR-HIES - ZNF341",
        meaning=MONDO["0032654"])
    mondo_0030491 = PermissibleValue(
        text="mondo_0030491",
        description="ZNFX1 deficiency - ZNFX1",
        meaning=MONDO["0030491"])

    _defn = EnumDefinition(
        name="IUIS2024MONDOEnum",
        description="""Enumeration of Inborn Errors of Immunity based on IUIS 2024 classification""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "4-1_bbl_deficiency",
            PermissibleValue(
                text="4-1_bbl_deficiency",
                description="4-1 BBL deficiency - TNFSF9",
                meaning=CIEINR["4-1_bbl_deficiency"]))

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

slots.iei_deficiency_basic = Slot(uri=CIEINR.iei_deficiency_basic, name="iei_deficiency_basic", curie=CIEINR.curie('iei_deficiency_basic'),
                   model_uri=CIEINR.iei_deficiency_basic, domain=None, range=Optional[Union[str, "IUIS2024MONDOEnum"]])

slots.igrt_basic = Slot(uri=CIEINR.igrt_basic, name="igrt_basic", curie=CIEINR.curie('igrt_basic'),
                   model_uri=CIEINR.igrt_basic, domain=None, range=Optional[Union[str, "IGRTStatusEnumBasicForm"]])

slots.hct_basic_form = Slot(uri=CIEINR.hct_basic_form, name="hct_basic_form", curie=CIEINR.curie('hct_basic_form'),
                   model_uri=CIEINR.hct_basic_form, domain=None, range=Optional[Union[str, "HCTStatusEnumBasicForm"]])

slots.basic_form_complete = Slot(uri=CIEINR.basic_form_complete, name="basic_form_complete", curie=CIEINR.curie('basic_form_complete'),
                   model_uri=CIEINR.basic_form_complete, domain=None, range=Union[str, "CompletionStatusEnumBasicForm"])

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
