# Auto generated from rarelink_6_1_genetic_findings.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:59:13
# Schema: rarelink_6_1_genetic_findings
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_6_1_genetic_findings.yaml
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
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None


# Namespaces
GA4GH = CurieNamespace('GA4GH', 'https://ga4gh.org/')
HGNC = CurieNamespace('HGNC', 'https://bioportal.bioontology.org/ontologies/HGNC/')
LOINC = CurieNamespace('LOINC', 'https://loinc.org/')
MONDO = CurieNamespace('MONDO', 'https://purl.obolibrary.org/obo/MONDO_')
OMIM = CurieNamespace('OMIM', 'https://omim.org/entry/')
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
class GeneticFindings(YAMLRoot):
    """
    Captures details about genetic findings and associated metadata like genomic diagnoses, interpretation, zygosity,
    clinical significance, and more.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["GeneticFindings"]
    class_class_curie: ClassVar[str] = "rarelink:GeneticFindings"
    class_name: ClassVar[str] = "GeneticFindings"
    class_model_uri: ClassVar[URIRef] = RARELINK.GeneticFindings

    genetic_diagnosis_code: str = None
    rarelink_6_1_genetic_findings_complete: str = None
    snomedct_106221001_mondo: Optional[str] = None
    snomedct_106221001_omim_p: Optional[str] = None
    ga4gh_progress_status: Optional[Union[str, "InterpretationProgressStatus"]] = None
    ga4gh_interp_status: Optional[Union[str, "InterpretationStatus"]] = None
    loinc_81304_8: Optional[Union[str, "StructuralVariantMethod"]] = None
    loinc_81304_8_other: Optional[str] = None
    loinc_62374_4: Optional[Union[str, "ReferenceGenome"]] = None
    loinc_lp7824_8: Optional[str] = None
    variant_expression: Optional[Union[str, "VariantExpressionType"]] = None
    loinc_81290_9: Optional[str] = None
    loinc_48004_6: Optional[str] = None
    loinc_48005_3: Optional[str] = None
    variant_validation: Optional[Union[bool, Bool]] = None
    loinc_48018_6: Optional[str] = None
    loinc_53034_5: Optional[Union[str, "Zygosity"]] = None
    loinc_53034_5_other: Optional[str] = None
    loinc_48002_0: Optional[Union[str, "GenomicSourceClass"]] = None
    loinc_48019_4: Optional[Union[str, "DNAChangeType"]] = None
    loinc_48019_4_other: Optional[str] = None
    loinc_53037_8: Optional[Union[str, "ClinicalSignificance"]] = None
    ga4gh_therap_action: Optional[Union[str, "TherapeuticActionability"]] = None
    loinc_93044_6: Optional[Union[str, "LevelOfEvidence"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genetic_diagnosis_code):
            self.MissingRequiredField("genetic_diagnosis_code")
        if not isinstance(self.genetic_diagnosis_code, str):
            self.genetic_diagnosis_code = str(self.genetic_diagnosis_code)

        if self._is_empty(self.rarelink_6_1_genetic_findings_complete):
            self.MissingRequiredField("rarelink_6_1_genetic_findings_complete")
        if not isinstance(self.rarelink_6_1_genetic_findings_complete, str):
            self.rarelink_6_1_genetic_findings_complete = str(self.rarelink_6_1_genetic_findings_complete)

        if self.snomedct_106221001_mondo is not None and not isinstance(self.snomedct_106221001_mondo, str):
            self.snomedct_106221001_mondo = str(self.snomedct_106221001_mondo)

        if self.snomedct_106221001_omim_p is not None and not isinstance(self.snomedct_106221001_omim_p, str):
            self.snomedct_106221001_omim_p = str(self.snomedct_106221001_omim_p)

        if self.ga4gh_progress_status is not None and not isinstance(self.ga4gh_progress_status, InterpretationProgressStatus):
            self.ga4gh_progress_status = InterpretationProgressStatus(self.ga4gh_progress_status)

        if self.ga4gh_interp_status is not None and not isinstance(self.ga4gh_interp_status, InterpretationStatus):
            self.ga4gh_interp_status = InterpretationStatus(self.ga4gh_interp_status)

        if self.loinc_81304_8 is not None and not isinstance(self.loinc_81304_8, StructuralVariantMethod):
            self.loinc_81304_8 = StructuralVariantMethod(self.loinc_81304_8)

        if self.loinc_81304_8_other is not None and not isinstance(self.loinc_81304_8_other, str):
            self.loinc_81304_8_other = str(self.loinc_81304_8_other)

        if self.loinc_62374_4 is not None and not isinstance(self.loinc_62374_4, ReferenceGenome):
            self.loinc_62374_4 = ReferenceGenome(self.loinc_62374_4)

        if self.loinc_lp7824_8 is not None and not isinstance(self.loinc_lp7824_8, str):
            self.loinc_lp7824_8 = str(self.loinc_lp7824_8)

        if self.variant_expression is not None and not isinstance(self.variant_expression, VariantExpressionType):
            self.variant_expression = VariantExpressionType(self.variant_expression)

        if self.loinc_81290_9 is not None and not isinstance(self.loinc_81290_9, str):
            self.loinc_81290_9 = str(self.loinc_81290_9)

        if self.loinc_48004_6 is not None and not isinstance(self.loinc_48004_6, str):
            self.loinc_48004_6 = str(self.loinc_48004_6)

        if self.loinc_48005_3 is not None and not isinstance(self.loinc_48005_3, str):
            self.loinc_48005_3 = str(self.loinc_48005_3)

        if self.variant_validation is not None and not isinstance(self.variant_validation, Bool):
            self.variant_validation = Bool(self.variant_validation)

        if self.loinc_48018_6 is not None and not isinstance(self.loinc_48018_6, str):
            self.loinc_48018_6 = str(self.loinc_48018_6)

        if self.loinc_53034_5 is not None and not isinstance(self.loinc_53034_5, Zygosity):
            self.loinc_53034_5 = Zygosity(self.loinc_53034_5)

        if self.loinc_53034_5_other is not None and not isinstance(self.loinc_53034_5_other, str):
            self.loinc_53034_5_other = str(self.loinc_53034_5_other)

        if self.loinc_48002_0 is not None and not isinstance(self.loinc_48002_0, GenomicSourceClass):
            self.loinc_48002_0 = GenomicSourceClass(self.loinc_48002_0)

        if self.loinc_48019_4 is not None and not isinstance(self.loinc_48019_4, DNAChangeType):
            self.loinc_48019_4 = DNAChangeType(self.loinc_48019_4)

        if self.loinc_48019_4_other is not None and not isinstance(self.loinc_48019_4_other, str):
            self.loinc_48019_4_other = str(self.loinc_48019_4_other)

        if self.loinc_53037_8 is not None and not isinstance(self.loinc_53037_8, ClinicalSignificance):
            self.loinc_53037_8 = ClinicalSignificance(self.loinc_53037_8)

        if self.ga4gh_therap_action is not None and not isinstance(self.ga4gh_therap_action, TherapeuticActionability):
            self.ga4gh_therap_action = TherapeuticActionability(self.ga4gh_therap_action)

        if self.loinc_93044_6 is not None and not isinstance(self.loinc_93044_6, LevelOfEvidence):
            self.loinc_93044_6 = LevelOfEvidence(self.loinc_93044_6)

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
class InterpretationProgressStatus(EnumDefinitionImpl):

    ga4gh_unknown_progress = PermissibleValue(
        text="ga4gh_unknown_progress",
        description="No information is available about the diagnosis",
        meaning=GA4GH["unknown_progress"])
    ga4gh_in_progress = PermissibleValue(
        text="ga4gh_in_progress",
        description="Additional differential diagnostic work is in progress",
        meaning=GA4GH["in_progress"])
    ga4gh_completed = PermissibleValue(
        text="ga4gh_completed",
        description="The work on the interpretation is complete",
        meaning=GA4GH["completed"])
    ga4gh_solved = PermissibleValue(
        text="ga4gh_solved",
        description="The interpretation is complete and definitive diagnosis made",
        meaning=GA4GH["solved"])
    ga4gh_unsolved = PermissibleValue(
        text="ga4gh_unsolved",
        description="The interpretation is complete but no definitive diagnosis",
        meaning=GA4GH["unsolved"])

    _defn = EnumDefinition(
        name="InterpretationProgressStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class InterpretationStatus(EnumDefinitionImpl):

    ga4gh_unknown_status = PermissibleValue(
        text="ga4gh_unknown_status",
        description="No information available about the status",
        meaning=GA4GH["unknown_status"])
    ga4gh_rejected = PermissibleValue(
        text="ga4gh_rejected",
        description="Variant not related to the diagnosis",
        meaning=GA4GH["rejected"])
    ga4gh_candidate = PermissibleValue(
        text="ga4gh_candidate",
        description="Variant possibly related to the diagnosis",
        meaning=GA4GH["candidate"])
    ga4gh_contributory = PermissibleValue(
        text="ga4gh_contributory",
        description="Variant related to the diagnosis",
        meaning=GA4GH["contributory"])
    ga4gh_causative = PermissibleValue(
        text="ga4gh_causative",
        description="Variant causative of the diagnosis",
        meaning=GA4GH["causative"])

    _defn = EnumDefinition(
        name="InterpretationStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class StructuralVariantMethod(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StructuralVariantMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la26406-1",
            PermissibleValue(
                text="loinc_la26406-1",
                description="Karyotyping",
                meaning=LOINC["LA26406-1"]))
        setattr(cls, "loinc_la26404-6",
            PermissibleValue(
                text="loinc_la26404-6",
                description="FISH",
                meaning=LOINC["LA26404-6"]))
        setattr(cls, "loinc_la26418-6",
            PermissibleValue(
                text="loinc_la26418-6",
                description="PCR",
                meaning=LOINC["LA26418-6"]))
        setattr(cls, "loinc_la26419-4",
            PermissibleValue(
                text="loinc_la26419-4",
                description="qPCR (real-time PCR)",
                meaning=LOINC["LA26419-4"]))
        setattr(cls, "loinc_la26400-4",
            PermissibleValue(
                text="loinc_la26400-4",
                description="SNP array",
                meaning=LOINC["LA26400-4"]))
        setattr(cls, "loinc_la26813-8",
            PermissibleValue(
                text="loinc_la26813-8",
                description="Restriction fragment length polymorphism (RFLP)",
                meaning=LOINC["LA26813-8"]))
        setattr(cls, "loinc_la26810-4",
            PermissibleValue(
                text="loinc_la26810-4",
                description="DNA hybridization",
                meaning=LOINC["LA26810-4"]))
        setattr(cls, "loinc_la26398-0",
            PermissibleValue(
                text="loinc_la26398-0",
                description="Sequencing",
                meaning=LOINC["LA26398-0"]))
        setattr(cls, "loinc_la26415-2",
            PermissibleValue(
                text="loinc_la26415-2",
                description="MLPA",
                meaning=LOINC["LA26415-2"]))
        setattr(cls, "loinc_la46-8",
            PermissibleValue(
                text="loinc_la46-8",
                description="Other",
                meaning=LOINC["LA46-8"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class ReferenceGenome(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ReferenceGenome",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la14032-9",
            PermissibleValue(
                text="loinc_la14032-9",
                description="NCBI Build 34 (hg16)",
                meaning=LOINC["LA14032-9"]))
        setattr(cls, "loinc_la14029-5",
            PermissibleValue(
                text="loinc_la14029-5",
                description="GRCh37 (hg19)",
                meaning=LOINC["LA14029-5"]))
        setattr(cls, "loinc_la14030-3",
            PermissibleValue(
                text="loinc_la14030-3",
                description="NCBI Build 36.1 (hg18)",
                meaning=LOINC["LA14030-3"]))
        setattr(cls, "loinc_la14031-1",
            PermissibleValue(
                text="loinc_la14031-1",
                description="NCBI Build 35 (hg17)",
                meaning=LOINC["LA14031-1"]))
        setattr(cls, "loinc_la26806-2",
            PermissibleValue(
                text="loinc_la26806-2",
                description="GRCh38 (hg38)",
                meaning=LOINC["LA26806-2"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class VariantExpressionType(EnumDefinitionImpl):

    ghgvs = PermissibleValue(
        text="ghgvs",
        description="Genomic DNA change [g.HGVS]",
        meaning=RARELINK["g.HGVS"])
    chgvs = PermissibleValue(
        text="chgvs",
        description="Sequence DNA change [c.HGVS]",
        meaning=RARELINK["c.HGVS"])
    phgvs = PermissibleValue(
        text="phgvs",
        description="Amino Acid Change [p.HGVS]",
        meaning=RARELINK["p.HGVS"])

    _defn = EnumDefinition(
        name="VariantExpressionType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class Zygosity(EnumDefinitionImpl):

    loinc_53034_5_other = PermissibleValue(
        text="loinc_53034_5_other",
        description="Other",
        meaning=LOINC["53034-5"])

    _defn = EnumDefinition(
        name="Zygosity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la6705-3",
            PermissibleValue(
                text="loinc_la6705-3",
                description="Homozygous",
                meaning=LOINC["LA6705-3"]))
        setattr(cls, "loinc_la6706-1",
            PermissibleValue(
                text="loinc_la6706-1",
                description="(simple) Heterozygous",
                meaning=LOINC["LA6706-1"]))
        setattr(cls, "loinc_la26217-2",
            PermissibleValue(
                text="loinc_la26217-2",
                description="Compound heterozygous",
                meaning=LOINC["LA26217-2"]))
        setattr(cls, "loinc_la26220-6",
            PermissibleValue(
                text="loinc_la26220-6",
                description="Double heterozygous",
                meaning=LOINC["LA26220-6"]))
        setattr(cls, "loinc_la6707-9",
            PermissibleValue(
                text="loinc_la6707-9",
                description="Hemizygous",
                meaning=LOINC["LA6707-9"]))
        setattr(cls, "loinc_la6703-8",
            PermissibleValue(
                text="loinc_la6703-8",
                description="Heteroplasmic",
                meaning=LOINC["LA6703-8"]))
        setattr(cls, "loinc_la6704-6",
            PermissibleValue(
                text="loinc_la6704-6",
                description="Homoplasmic",
                meaning=LOINC["LA6704-6"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class GenomicSourceClass(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GenomicSourceClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la6683-2",
            PermissibleValue(
                text="loinc_la6683-2",
                description="Germline",
                meaning=LOINC["LA6683-2"]))
        setattr(cls, "loinc_la6684-0",
            PermissibleValue(
                text="loinc_la6684-0",
                description="Somatic",
                meaning=LOINC["LA6684-0"]))
        setattr(cls, "loinc_la10429-1",
            PermissibleValue(
                text="loinc_la10429-1",
                description="Fetal",
                meaning=LOINC["LA10429-1"]))
        setattr(cls, "loinc_la18194-3",
            PermissibleValue(
                text="loinc_la18194-3",
                description="Likely germline",
                meaning=LOINC["LA18194-3"]))
        setattr(cls, "loinc_la18195-0",
            PermissibleValue(
                text="loinc_la18195-0",
                description="Likely somatic",
                meaning=LOINC["LA18195-0"]))
        setattr(cls, "loinc_la18196-8",
            PermissibleValue(
                text="loinc_la18196-8",
                description="Likely fetal",
                meaning=LOINC["LA18196-8"]))
        setattr(cls, "loinc_la18197-6",
            PermissibleValue(
                text="loinc_la18197-6",
                description="Unknown genomic origin",
                meaning=LOINC["LA18197-6"]))
        setattr(cls, "loinc_la26807-0",
            PermissibleValue(
                text="loinc_la26807-0",
                description="De novo",
                meaning=LOINC["LA26807-0"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class DNAChangeType(EnumDefinitionImpl):

    loinc_48019_4_other = PermissibleValue(
        text="loinc_48019_4_other",
        description="Other",
        meaning=LOINC["48019-4"])

    _defn = EnumDefinition(
        name="DNAChangeType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la9658-1",
            PermissibleValue(
                text="loinc_la9658-1",
                description="Wild type",
                meaning=LOINC["LA9658-1"]))
        setattr(cls, "loinc_la6692-3",
            PermissibleValue(
                text="loinc_la6692-3",
                description="Deletion",
                meaning=LOINC["LA6692-3"]))
        setattr(cls, "loinc_la6686-5",
            PermissibleValue(
                text="loinc_la6686-5",
                description="Duplication",
                meaning=LOINC["LA6686-5"]))
        setattr(cls, "loinc_la6687-3",
            PermissibleValue(
                text="loinc_la6687-3",
                description="Insertion",
                meaning=LOINC["LA6687-3"]))
        setattr(cls, "loinc_la6688-1",
            PermissibleValue(
                text="loinc_la6688-1",
                description="Insertion/Deletion",
                meaning=LOINC["LA6688-1"]))
        setattr(cls, "loinc_la6689-9",
            PermissibleValue(
                text="loinc_la6689-9",
                description="Inversion",
                meaning=LOINC["LA6689-9"]))
        setattr(cls, "loinc_la6690-7",
            PermissibleValue(
                text="loinc_la6690-7",
                description="Substitution",
                meaning=LOINC["LA6690-7"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class ClinicalSignificance(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ClinicalSignificance",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la6668-3",
            PermissibleValue(
                text="loinc_la6668-3",
                description="Pathogenic",
                meaning=LOINC["LA6668-3"]))
        setattr(cls, "loinc_la26332-9",
            PermissibleValue(
                text="loinc_la26332-9",
                description="Likely pathogenic",
                meaning=LOINC["LA26332-9"]))
        setattr(cls, "loinc_la26333-7",
            PermissibleValue(
                text="loinc_la26333-7",
                description="Uncertain significance",
                meaning=LOINC["LA26333-7"]))
        setattr(cls, "loinc_la26334-5",
            PermissibleValue(
                text="loinc_la26334-5",
                description="Likely benign",
                meaning=LOINC["LA26334-5"]))
        setattr(cls, "loinc_la6675-8",
            PermissibleValue(
                text="loinc_la6675-8",
                description="Benign",
                meaning=LOINC["LA6675-8"]))
        setattr(cls, "loinc_la4489-6",
            PermissibleValue(
                text="loinc_la4489-6",
                description="Unknown",
                meaning=LOINC["LA4489-6"]))
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class TherapeuticActionability(EnumDefinitionImpl):

    ga4gh_unknown_actionability = PermissibleValue(
        text="ga4gh_unknown_actionability",
        description="No therapeutic actionability available",
        meaning=GA4GH["unknown_actionability"])
    ga4gh_not_actionable = PermissibleValue(
        text="ga4gh_not_actionable",
        description="No therapeutic actionability",
        meaning=GA4GH["not_actionable"])
    ga4gh_actionable = PermissibleValue(
        text="ga4gh_actionable",
        description="Therapeutically actionable",
        meaning=GA4GH["actionable"])

    _defn = EnumDefinition(
        name="TherapeuticActionability",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class LevelOfEvidence(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LevelOfEvidence",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la30200-2",
            PermissibleValue(
                text="loinc_la30200-2",
                description="Very strong evidence pathogenic",
                meaning=LOINC["LA30200-2"]))
        setattr(cls, "loinc_la30201-0",
            PermissibleValue(
                text="loinc_la30201-0",
                description="Strong evidence pathogenic",
                meaning=LOINC["LA30201-0"]))
        setattr(cls, "loinc_la30202-8",
            PermissibleValue(
                text="loinc_la30202-8",
                description="Moderate evidence pathogenic",
                meaning=LOINC["LA30202-8"]))
        setattr(cls, "loinc_la30203-6",
            PermissibleValue(
                text="loinc_la30203-6",
                description="Supporting evidence pathogenic",
                meaning=LOINC["LA30203-6"]))
        setattr(cls, "loinc_la30204-4",
            PermissibleValue(
                text="loinc_la30204-4",
                description="Supporting evidence benign",
                meaning=LOINC["LA30204-4"]))
        setattr(cls, "loinc_la30205-1",
            PermissibleValue(
                text="loinc_la30205-1",
                description="Strong evidence benign",
                meaning=LOINC["LA30205-1"]))
        setattr(cls, "loinc_la30206-9",
            PermissibleValue(
                text="loinc_la30206-9",
                description="Stand-alone evidence pathogenic",
                meaning=LOINC["LA30206-9"]))
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

class MONDO(EnumDefinitionImpl):  # noqa: F811
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

class OMIM(EnumDefinitionImpl):  # noqa: F811
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

class HGNC(EnumDefinitionImpl):  # noqa: F811
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

slots.genetic_diagnosis_code = Slot(uri=RARELINK.genetic_diagnosis_code, name="genetic_diagnosis_code", curie=RARELINK.curie('genetic_diagnosis_code'),
                   model_uri=RARELINK.genetic_diagnosis_code, domain=None, range=str)

slots.snomedct_106221001_mondo = Slot(uri=RARELINK.snomedct_106221001_mondo, name="snomedct_106221001_mondo", curie=RARELINK.curie('snomedct_106221001_mondo'),
                   model_uri=RARELINK.snomedct_106221001_mondo, domain=None, range=Optional[str])

slots.snomedct_106221001_omim_p = Slot(uri=RARELINK.snomedct_106221001_omim_p, name="snomedct_106221001_omim_p", curie=RARELINK.curie('snomedct_106221001_omim_p'),
                   model_uri=RARELINK.snomedct_106221001_omim_p, domain=None, range=Optional[str])

slots.ga4gh_progress_status = Slot(uri=RARELINK.ga4gh_progress_status, name="ga4gh_progress_status", curie=RARELINK.curie('ga4gh_progress_status'),
                   model_uri=RARELINK.ga4gh_progress_status, domain=None, range=Optional[Union[str, "InterpretationProgressStatus"]])

slots.ga4gh_interp_status = Slot(uri=RARELINK.ga4gh_interp_status, name="ga4gh_interp_status", curie=RARELINK.curie('ga4gh_interp_status'),
                   model_uri=RARELINK.ga4gh_interp_status, domain=None, range=Optional[Union[str, "InterpretationStatus"]])

slots.loinc_81304_8 = Slot(uri=RARELINK.loinc_81304_8, name="loinc_81304_8", curie=RARELINK.curie('loinc_81304_8'),
                   model_uri=RARELINK.loinc_81304_8, domain=None, range=Optional[Union[str, "StructuralVariantMethod"]])

slots.loinc_81304_8_other = Slot(uri=RARELINK.loinc_81304_8_other, name="loinc_81304_8_other", curie=RARELINK.curie('loinc_81304_8_other'),
                   model_uri=RARELINK.loinc_81304_8_other, domain=None, range=Optional[str])

slots.loinc_62374_4 = Slot(uri=RARELINK.loinc_62374_4, name="loinc_62374_4", curie=RARELINK.curie('loinc_62374_4'),
                   model_uri=RARELINK.loinc_62374_4, domain=None, range=Optional[Union[str, "ReferenceGenome"]])

slots.loinc_lp7824_8 = Slot(uri=RARELINK.loinc_lp7824_8, name="loinc_lp7824_8", curie=RARELINK.curie('loinc_lp7824_8'),
                   model_uri=RARELINK.loinc_lp7824_8, domain=None, range=Optional[str])

slots.variant_expression = Slot(uri=RARELINK.variant_expression, name="variant_expression", curie=RARELINK.curie('variant_expression'),
                   model_uri=RARELINK.variant_expression, domain=None, range=Optional[Union[str, "VariantExpressionType"]])

slots.loinc_81290_9 = Slot(uri=RARELINK.loinc_81290_9, name="loinc_81290_9", curie=RARELINK.curie('loinc_81290_9'),
                   model_uri=RARELINK.loinc_81290_9, domain=None, range=Optional[str])

slots.loinc_48004_6 = Slot(uri=RARELINK.loinc_48004_6, name="loinc_48004_6", curie=RARELINK.curie('loinc_48004_6'),
                   model_uri=RARELINK.loinc_48004_6, domain=None, range=Optional[str])

slots.loinc_48005_3 = Slot(uri=RARELINK.loinc_48005_3, name="loinc_48005_3", curie=RARELINK.curie('loinc_48005_3'),
                   model_uri=RARELINK.loinc_48005_3, domain=None, range=Optional[str])

slots.variant_validation = Slot(uri=RARELINK.variant_validation, name="variant_validation", curie=RARELINK.curie('variant_validation'),
                   model_uri=RARELINK.variant_validation, domain=None, range=Optional[Union[bool, Bool]])

slots.loinc_48018_6 = Slot(uri=RARELINK.loinc_48018_6, name="loinc_48018_6", curie=RARELINK.curie('loinc_48018_6'),
                   model_uri=RARELINK.loinc_48018_6, domain=None, range=Optional[str])

slots.loinc_53034_5 = Slot(uri=RARELINK.loinc_53034_5, name="loinc_53034_5", curie=RARELINK.curie('loinc_53034_5'),
                   model_uri=RARELINK.loinc_53034_5, domain=None, range=Optional[Union[str, "Zygosity"]])

slots.loinc_53034_5_other = Slot(uri=RARELINK.loinc_53034_5_other, name="loinc_53034_5_other", curie=RARELINK.curie('loinc_53034_5_other'),
                   model_uri=RARELINK.loinc_53034_5_other, domain=None, range=Optional[str])

slots.loinc_48002_0 = Slot(uri=RARELINK.loinc_48002_0, name="loinc_48002_0", curie=RARELINK.curie('loinc_48002_0'),
                   model_uri=RARELINK.loinc_48002_0, domain=None, range=Optional[Union[str, "GenomicSourceClass"]])

slots.loinc_48019_4 = Slot(uri=RARELINK.loinc_48019_4, name="loinc_48019_4", curie=RARELINK.curie('loinc_48019_4'),
                   model_uri=RARELINK.loinc_48019_4, domain=None, range=Optional[Union[str, "DNAChangeType"]])

slots.loinc_48019_4_other = Slot(uri=RARELINK.loinc_48019_4_other, name="loinc_48019_4_other", curie=RARELINK.curie('loinc_48019_4_other'),
                   model_uri=RARELINK.loinc_48019_4_other, domain=None, range=Optional[str])

slots.loinc_53037_8 = Slot(uri=RARELINK.loinc_53037_8, name="loinc_53037_8", curie=RARELINK.curie('loinc_53037_8'),
                   model_uri=RARELINK.loinc_53037_8, domain=None, range=Optional[Union[str, "ClinicalSignificance"]])

slots.ga4gh_therap_action = Slot(uri=RARELINK.ga4gh_therap_action, name="ga4gh_therap_action", curie=RARELINK.curie('ga4gh_therap_action'),
                   model_uri=RARELINK.ga4gh_therap_action, domain=None, range=Optional[Union[str, "TherapeuticActionability"]])

slots.loinc_93044_6 = Slot(uri=RARELINK.loinc_93044_6, name="loinc_93044_6", curie=RARELINK.curie('loinc_93044_6'),
                   model_uri=RARELINK.loinc_93044_6, domain=None, range=Optional[Union[str, "LevelOfEvidence"]])

slots.rarelink_6_1_genetic_findings_complete = Slot(uri=RARELINK.rarelink_6_1_genetic_findings_complete, name="rarelink_6_1_genetic_findings_complete", curie=RARELINK.curie('rarelink_6_1_genetic_findings_complete'),
                   model_uri=RARELINK.rarelink_6_1_genetic_findings_complete, domain=None, range=str)

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
