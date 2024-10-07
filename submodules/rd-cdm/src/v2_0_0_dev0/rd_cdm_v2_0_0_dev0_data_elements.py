from src.data_model.data_elements import DataElement
from src.data_model.value_set import ValueSet
from src.data_model.base_types import Coding, Date, Code, String, Integer, Identifier, Value
from src.data_model.codesystems import CodeSystems

# Define CodeSystems
SNOMED = CodeSystems.SNOMED
HL7FHIR = CodeSystems.HL7FHIR
GA4GH = CodeSystems.GA4GH
LOINC = CodeSystems.LOINC
CustomCode = CodeSystems.CustomCode
HP = CodeSystems.HP
ECO = CodeSystems.ECO
NCIT = CodeSystems.NCIT

class DATA_ELEMENTS_VERSIONS_V2_0_0_dev0:
    """Data elements definitions for version 2_0_0_dev0."""

    # 1. Formal Criteria
    data_elements = [
        DataElement(
            ordinal="1.1",
            section="1. Formal Criteria",
            elementName="Pseudonym",
            elementCode=Coding(system=SNOMED, code="422549004"),
            elementCodeSystem=SNOMED,
            dataType=Identifier,
            dataSpecification=["n/a"],
            valueSet=None,
            fhirExpression_v4_0_1="Patient.identifier.value",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.id",
            recommendedDataSpec_phenopackets="string",
            description="The (local) patient-related identification code."
        ),
        DataElement(
            ordinal="1.2",
            section="1. Formal Criteria",
            elementName="Date of Admission",
            elementCode=Coding(system=SNOMED, code="399423000"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet=None,
            fhirExpression_v4_0_1="Encounter.period.start",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.time_at_last_encounter",
            recommendedDataSpec_phenopackets="TimeElement",
            description="The date of admission or data capture of the individual."
        ),
#_______________________________________________________________________________

        # 2. Personal Information
        DataElement(
            ordinal="2.1",
            section="2. Personal Information",
            elementName="Date of Birth",
            elementCode=Coding(system=SNOMED, code="184099003"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY", "YYYY-MM", "YYYY-MM-DD"],
            valueSet=None,
            fhirExpression_v4_0_1="Patient.birthDate",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.date_of_birth",
            recommendedDataSpec_phenopackets="TimeElement",
            description="The individual's date of birth."
        ),
        DataElement(
            ordinal="2.2",
            section="2. Personal Information",
            elementName="Sex at Birth",
            elementCode=Coding(system=SNOMED, code="281053000"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Sex at Birth Value Set v2.0.0",
            fhirExpression_v4_0_1="Patient.extension:"
                                    "individual-recordedSexOrGender",
            recommendedDataSpec_fhir="Recorded Sex Or Gender Type",
            phenopacketSchemaElement_v2_0="Individual.sex",
            recommendedDataSpec_phenopackets="Sex",
            description="The individual's sex that was assigned at birth."
        ),
        DataElement(
            ordinal="2.3",
            section="2. Personal Information",
            elementName="Karyotypic Sex",
            elementCode=Coding(system=SNOMED, code="1296886006"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSc"],
            valueSet="Karyotypic Sex Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.value",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.karyotypic_sex",
            recommendedDataSpec_phenopackets="Karyotypic Sex",
            description="The chromosomal sex of an individual."
        ),
        DataElement(
            ordinal="2.4",
            section="2. Personal Information",
            elementName="Gender Identity",
            elementCode=Coding(system=SNOMED, code="263495000"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Gender Identity Value Set v2.0.0",
            fhirExpression_v4_0_1="Patient.extension:individual-genderIdentity",
            recommendedDataSpec_fhir="Gender Identity",
            phenopacketSchemaElement_v2_0="Individual.gender",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The self-assigned gender of the individual."
        ),
        DataElement(
            ordinal="2.5",
            section="2. Personal Information",
            elementName="Country of Birth",
            elementCode=Coding(system=SNOMED, code="370159000"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet=None,  
            fhirExpression_v4_0_1="Patient.extension:patient-birthPlace",
            recommendedDataSpec_fhir="DataType: Address",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The individual's country of birth."
        ),
#_______________________________________________________________________________
        
        # 3. Patient Status
        DataElement(
            ordinal="3.1",
            section="3. Patient Status",
            elementName="Vital Status",
            elementCode=Coding(system=SNOMED, code="278844005"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Vital Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Patient.deceased.deceasedBoolean|"
                                    "Observation.value",
            recommendedDataSpec_fhir="Boolean|Code",
            phenopacketSchemaElement_v2_0="Individual.VitalStatus.status",
            recommendedDataSpec_phenopackets="Value Set: VitalStatus.Status",
            description="The individual’s general clinical status or"
                        "vital status."
        ),
        DataElement(
            ordinal="3.2",
            section="3. Patient Status",
            elementName="Time of Death",
            elementCode=Coding(system=SNOMED, code="398299004"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY", "YYYY-MM", "YYYY-MM-DD"],
            valueSet=None,
            fhirExpression_v4_0_1="Patient.deceasedDateTime",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="Individual.VitalStatus.time_of_death",
            recommendedDataSpec_phenopackets="TimeElement",
            description="If deceased, the individual’s date of death."
        ),
        DataElement(
            ordinal="3.3",
            section="3. Patient Status",
            elementName="Cause of Death",
            elementCode=Coding(system=SNOMED, code="184305005"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["ICD-10CM"],
            valueSet=None,
            fhirExpression_v4_0_1="Observation.value.coding.code",
            recommendedDataSpec_fhir="Code|CodeableConcept",
            phenopacketSchemaElement_v2_0="Individual.VitalStatus.cause_of_death",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="If deceased, the individual’s primary cause of death."
        ),
        DataElement(
            ordinal="3.4",
            section="3. Patient Status",
            elementName="Age Category",
            elementCode=Coding(system=SNOMED, code="105727008"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Age Category Value Set v2.0.0", 
            fhirExpression_v4_0_1="Observation.value.coding.code",
            recommendedDataSpec_fhir="CodableConcept",
            phenopacketSchemaElement_v2_0="Individual.time_at_last_encounter",
            recommendedDataSpec_phenopackets="TimeElement",
            description="The individual's age category at the"
                        "time of data capture."
        ),
        DataElement(
            ordinal="3.5",
            section="3. Patient Status",
            elementName="Length of Gestation at Birth [weeks+days]",
            elementCode=Coding(system=SNOMED, code="412726003"),
            elementCodeSystem=SNOMED,
            dataType=String,
            dataSpecification=["XX+X"],
            valueSet=None,
            fhirExpression_v4_0_1="Observation.component:weeks.valueQuantity"
                                    "|Observation.component:days.valueQuantity",
            recommendedDataSpec_fhir="Quantity",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The duration of the pregnancy in weeks and days,"
                        "formatted as XX+X (weeks+days)."
        ),
        DataElement(
            ordinal="3.6",
            section="3. Patient Status",
            elementName="Undiagnosed RD Case",
            elementCode=Coding(system=SNOMED, code="723663001"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Undiagnosed RD Case Value Set v2.0.0",
            fhirExpression_v4_0_1="(Condition.code)",
            recommendedDataSpec_fhir="Code(e.g. ORDO:616874 - Rare disorder"
                                     "without a determined diagnosis after"
                                      "full investigation)",
            phenopacketSchemaElement_v2_0="(Disease.term)",
            recommendedDataSpec_phenopackets="(OntologyClass (e.g. ORDO:616874"
                                    " - Rare disorder without a determined"
                                    "diagnosis after full investigation))", 
            description="Identifies cases where an RD diagnosis has not"
                         "been established."
        ),
#_______________________________________________________________________________
       
        # 4. Care Pathway
        DataElement(
            ordinal="4.1",
            section="4. Care Pathway",
            elementName="Encounter Start",
            elementCode=Coding(system=HL7FHIR, code="encounter.period.start"),
            elementCodeSystem=HL7FHIR,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet=None,
            fhirExpression_v4_0_1="Encounter.period.start",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The beginning of an encounter of the individual."
        ),
        DataElement(
            ordinal="4.2",
            section="4. Care Pathway",
            elementName="Encounter End",
            elementCode=Coding(system=HL7FHIR, code="encounter.period.end"),
            elementCodeSystem=HL7FHIR,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet=None,
            fhirExpression_v4_0_1="Encounter.period.end",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The end of an encounter of the individual."
        ),
        DataElement(
            ordinal="4.3",
            section="4. Care Pathway",
            elementName="Encounter Status",
            elementCode=Coding(system=SNOMED, code="305058001"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Encounter Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Encounter.status",
            recommendedDataSpec_fhir="ValueSet: EncounterStatus",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The status of an encounter of the individual at the"
                        "time of data capture."
        ),
        DataElement(
            ordinal="4.4",
            section="4. Care Pathway",
            elementName="Encounter Class",
            elementCode=Coding(system=HL7FHIR, code="encounter.class"),
            elementCodeSystem=HL7FHIR,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Encounter Class Value Set v2.0.0",
            fhirExpression_v4_0_1="Encounter.class",
            recommendedDataSpec_fhir="ValueSet: EncounterClass",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The class of an encounter of the individual"
                        "at the time of data capture."
        ),
#_______________________________________________________________________________

        # 5. Disease
        DataElement(
            ordinal="5.1",
            section="5. Disease",
            elementName="Disease",
            elementCode=Coding(system=SNOMED, code="64572001"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=[
                "Ontology Class (MONDO, ORDO, ICD-10, ICD-11, OMIM_g, OMIM_p)"
            ],
            valueSet="n/a",
            fhirExpression_v4_0_1="Condition.code",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="Disease.term",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="A disease that the individual was affected by. If a"
                        "genetic diagnosis or subtypes were diagnosed, please"
                        "also provide the respective OMIM_g and OMIM_p codes."
        ),
        DataElement(
            ordinal="5.2",
            section="5. Disease",
            elementName="Verification Status",
            elementCode=Coding(system=LOINC, code="99498-8"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Verification Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.verificationStatus",
            recommendedDataSpec_fhir="ValueSet: Condition Verficication Status",
            phenopacketSchemaElement_v2_0="(Disease.excluded)",
            recommendedDataSpec_phenopackets="boolean",
            description="The verification status of the disease."
        ),
        DataElement(
            ordinal="5.3",
            section="5. Disease",
            elementName="Age at Onset",
            elementCode=Coding(system=SNOMED, code="424850005"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Age at Onset Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.onsetString or"
                                 "Observation.valueCodeableConcept",
            recommendedDataSpec_fhir="Disease.onset",
            phenopacketSchemaElement_v2_0="Disease.onset",
            recommendedDataSpec_phenopackets="Disease.onset",
            description="The age at the onset of the first symptoms"
                         "or signs of the disease."
        ),
        DataElement(
            ordinal="5.4",
            section="5. Disease",
            elementName="Date of Onset",
            elementCode=Coding(system=SNOMED, code="298059007"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Condition.onset",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="Disease.onset",
            recommendedDataSpec_phenopackets="TimeElement",
            description="The date at onset of first symptoms or"
                         "signs of the disease."
        ),
        DataElement(
            ordinal="5.5",
            section="5. Disease",
            elementName="Age at Diagnosis",
            elementCode=Coding(system=SNOMED, code="423493009"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Age at Diagnosis Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.value",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="(Disease.onset)",
            recommendedDataSpec_phenopackets="(TimeElement)",
            description="The individual’s age when the diagnosis was made."
        ),
        DataElement(
            ordinal="5.6",
            section="5. Disease",
            elementName="Date of Diagnosis",
            elementCode=Coding(system=SNOMED, code="432213005"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Condition.recordedDate",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="(Disease.onset)",
            recommendedDataSpec_phenopackets="(TimeElement)",
            description="The date on which the disease was determined."
        ),
        DataElement(
            ordinal="5.7",
            section="5. Disease",
            elementName="Body Site",
            elementCode=Coding(system=SNOMED, code="363698007"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Body Site Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.bodySite.coding:snomed-ct",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="Disease.primary_site",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The specific body site affected by disease is encoded"
                        "using all descendants of SCT Body Structure (123037004)."
        ),
        DataElement(
            ordinal="5.8",
            section="5. Disease",
            elementName="Clinical Status",
            elementCode=Coding(system=SNOMED, code="263493007"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Clinical Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.clinicalStatus",
            recommendedDataSpec_fhir="ValueSet: ClinicalStatus",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The clinical status of the disease indicates whether"
                        "it is active, inactive, or resolved."
        ),
        DataElement(
            ordinal="5.9",
            section="5. Disease",
            elementName="Severity",
            elementCode=Coding(system=SNOMED, code="246112005"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Severity Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.severity",
            recommendedDataSpec_fhir="ValueSet: ConditionSeverity",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The severity of the disease is categorised by"
                        "clinical evaluation."
        ),
        DataElement(
            ordinal="6.1.1",
            section="6. Genetic Findings",
            elementName="Genomic Diagnosis",
            elementCode=Coding(system=SNOMED, code="106221001"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["OMIM_p", "MONDO"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Condition.code",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="Interpretation.Diagnosis.disease",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The genomic diagnoses can correspond to the diagnosed"
                        "disease in (5.1) if the same OMIM codes are used."
        ),
        DataElement(
            ordinal="6.1.2",
            section="6. Genetic Findings",
            elementName="Progress Status of Interpretation",
            elementCode=Coding(system=GA4GH, code="progress_status"),
            elementCodeSystem=GA4GH,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Progress Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.extension",
            recommendedDataSpec_fhir="VS: GA4GH ProgressStatus",
            phenopacketSchemaElement_v2_0="Interpretation.progress_status",
            recommendedDataSpec_phenopackets="ValueSet: ProgressStatus",
            description="The interpretation has a ProgressStatus that refers to"
                        "the status of the attempted diagnosis."
        ),
        DataElement(
            ordinal="6.1.3",
            section="6. Genetic Findings",
            elementName="Interpretation Status",
            elementCode=Coding(system=GA4GH, code="interpretation_status"),
            elementCodeSystem=GA4GH,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Interpretation Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Condition.extension",
            recommendedDataSpec_fhir="VS: GA4GH InterpretationStatus",
            phenopacketSchemaElement_v2_0="GenomicInterpretation."
                                            "interpretation_status",
            recommendedDataSpec_phenopackets="ValueSet: InterpretationStatus",
            description="An enumeration that describes the conclusion made "
                        "about the genomic interpretation."
        ),
        DataElement(
            ordinal="6.1.4",
            section="6. Genetic Findings",
            elementName="Structural Variant Analysis Method",
            elementCode=Coding(system=LOINC, code="81304-8"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VS", "LOINC"],
            valueSet="Structural Variant Analysis Method Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.method",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The method used to analyse structural variants "
                        "in the genome."
        ),
        DataElement(
            ordinal="6.1.5",
            section="6. Genetic Findings",
            elementName="Reference Genome",
            elementCode=Coding(system=LOINC, code="62374-4"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Reference Genome Value Set v2.0.0",
            fhirExpression_v4_0_1="MolecularSequence.referenceSeqId",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="VariationDescriptor.vrs_ref_allele_seq",
            recommendedDataSpec_phenopackets="string",
            description="The reference genome used for analysing the "
                        "genetic variant."
        ),
        DataElement(
            ordinal="6.1.6",
            section="6. Genetic Findings",
            elementName="Genetic Mutation String",
            elementCode=Coding(system=LOINC, code="LP7824-8"),
            elementCodeSystem=LOINC,
            dataType=String,
            dataSpecification=["n/a"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.component:Variant.valueString",
            recommendedDataSpec_fhir="string",
            phenopacketSchemaElement_v2_0="VariationDescriptor.Extension.value",
            recommendedDataSpec_phenopackets="string",
            description="An unvalidated (HGVS) string that describes "
                        "the variant change"
        ),
        DataElement(
            ordinal="6.1.7",
            section="6. Genetic Findings",
            elementName="Genomic DNA Change",
            elementCode=Coding(system=LOINC, code="81290-9"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["g.HGVS"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.component:Variant.valueCode",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="VariationDescriptor.Expression.value",
            recommendedDataSpec_phenopackets="string",
            description="The specific change in the genomic DNA sequence encoded"
                        " with a validated g.HGVS expression."
        ),
        DataElement(
            ordinal="6.1.8",
            section="6. Genetic Findings",
            elementName="Sequence DNA Change",
            elementCode=Coding(system=LOINC, code="48004-6"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["c.HGVS"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.component:Variant.valueCode",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="VariationDescriptor.Expression.value",
            recommendedDataSpec_phenopackets="string",
            description="The specific change in the DNA sequence at the "
                        "nucleotide level with a validated c.HGVS expression."
        ),
        DataElement(
            ordinal="6.1.9",
            section="6. Genetic Findings",
            elementName="Amino Acid Change",
            elementCode=Coding(system=LOINC, code="48005-3"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["p.HGVS"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.component:Variant.valueCode",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="VariationDescriptor.Expression.value",
            recommendedDataSpec_phenopackets="string",
            description="The specific change in the amino acid sequence "
                        "resulting from agenetic variant as a validated "
                        "p.HGVS expression."
        ),
        DataElement(
            ordinal="6.1.10",
            section="6. Genetic Findings",
            elementName="Gene",
            elementCode=Coding(system=LOINC, code="48018-6"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["HGNC"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.component:Gene",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="GeneDescriptor.value_id",
            recommendedDataSpec_phenopackets="string",
            description="The specific gene or genes that were analysed "
                        "or identified in the study."
        ),
        DataElement(
            ordinal="6.1.11",
            section="6. Genetic Findings",
            elementName="Zygosity",
            elementCode=Coding(system=LOINC, code="53034-5"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VSe", "VSc", "LOINC"],
            valueSet="Zygosity Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.component:geneticsAllele.State",
            recommendedDataSpec_fhir="VS: Allelic State",
            phenopacketSchemaElement_v2_0="VariationDescriptor.allelic_state",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The zygosity of the genetic variant."
        ),
        DataElement(
            ordinal="6.1.12",
            section="6. Genetic Findings",
            elementName="Genomic Source Class",
            elementCode=Coding(system=LOINC, code="48002-0"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Genomic Source Class Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.component:GenomicSourceClass",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The classification of the genomic source, such as "
                        "germline, somatic, or other origins."
        ),
        DataElement(
            ordinal="6.1.13",
            section="6. Genetic Findings",
            elementName="DNA Change Type",
            elementCode=Coding(system=LOINC, code="48019-4"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="DNA Change Type Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.component:Variant.Type",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The variant’s type of DNA change, such as point "
                        "mutation, deletion, insertion, or other types."
        ),
        DataElement(
            ordinal="6.1.14",
            section="6. Genetic Findings",
            elementName="Clinical Significance [ACMG]",
            elementCode=Coding(system=LOINC, code="53037-8"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Clinical Significance ACMG Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.component:Variant.Interpretation",
            recommendedDataSpec_fhir="",
            phenopacketSchemaElement_v2_0="VariantInterpretation."
                                "acmg_pathogenicity_classification",
            recommendedDataSpec_phenopackets="ValueSet: "
                                "AcmgPathogenicityClassification",
            description="The clinical significance of the genetic variant, "
                        "indicating its impact on health and disease."
        ),
        DataElement(
            ordinal="6.1.15",
            section="6. Genetic Findings",
            elementName="Therapeutic Actionability",
            elementCode=Coding(system=GA4GH, code="therapeutic_actionability"),
            elementCodeSystem=GA4GH,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Therapeutic Actionability Value Set v2.0.0",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="VariantInterpretation."
                                         "therapeutic_actionability",
            recommendedDataSpec_phenopackets="ValueSet: TherapeuticActionability",
            description="An enumeration flagging the variant as being a "
                        "candidate for treatment or clinical intervention, "
                        "which could improve the clinical outcome."
        ),
        DataElement(
            ordinal="6.1.16",
            section="6. Genetic Findings",
            elementName="Clinical Annotation Level Of Evidence",
            elementCode=Coding(system=LOINC, code="93044-6"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Clinical Annotation Level Of Evidence Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.extension:Variant.Interpretation",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The level of evidence supporting the clinical "
                        "annotation of the genetic variant."
        ),
#_______________________________________________________________________________        
        # 6.2 Phenotypic Findings
        DataElement(
            ordinal="6.2.1",
            section="6. Phenotypic Feature",
            elementName="Phenotypic Feature",
            elementCode=Coding(system=SNOMED, code="8116006"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["HPO"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.code",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.type",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="An observed physical and clinical characteristic"
                         "encoded with HPO."
        ),
        DataElement(
            ordinal="6.2.2",
            section="6.2 Phenotypic Feature",
            elementName="Status",
            elementCode=Coding(system=SNOMED, code="363778006"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Phenotype Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.status",
            recommendedDataSpec_fhir="ValueSet: ObservationStatus",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.excluded",
            recommendedDataSpec_phenopackets="boolean",
            description="The current status of the phenotypic feature, "
                        "indicating whether it is confirmed or refuted."
        ),

        DataElement(
            ordinal="6.2.3",
            section="6. Phenotypic Feature",
            elementName="Determination Date",
            elementCode=Coding(system=SNOMED, 
                               code="439272007:704321009=363778006"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.effectiveDateTime",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.onset",
            recommendedDataSpec_phenopackets="TimeElement",
            description="The date on which the phenotypic feature was observed "
                        "or recorded. We recommend capturing the time a"
                         "characteristic was observed."
        ),

        DataElement(
            ordinal="6.2.4",
            section="6.2 Phenotypic Feature",
            elementName="Resolution Date",
            elementCode=Coding(system=HP, code="0034382"),
            elementCodeSystem=HP,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.effectiveDateTime",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.resolution",
            recommendedDataSpec_phenopackets="TimeElement",
            description="Time at which the feature resolved or abated."
        ),

        DataElement(
            ordinal="6.2.5",
            section="6.2 Phenotypic Feature",
            elementName="Onset Category",
            elementCode=Coding(system=HP, code="0003674"),
            elementCodeSystem=HP,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Onset Category Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.category",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.onset",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="Time at which the feature was first observed within "
                        " HPO onset categories."
        ),

        DataElement(
            ordinal="6.2.6",
            section="6.2 Phenotypic Feature",
            elementName="Temporal Pattern",
            elementCode=Coding(system=HP, code="0011008"),
            elementCodeSystem=HP,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Temporal Pattern Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.interpretation",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.modifiers",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The speed at which disease manifestations appear and "
                        "develop."
        ),

        DataElement(
            ordinal="6.2.7",
            section="6.2 Phenotypic Feature",
            elementName="Severity",
            elementCode=Coding(system=HP, code="0012824"),
            elementCodeSystem=HP,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Severity Value Set v2.0.0",
            fhirExpression_v4_0_1="Observation.interpretation",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.severity",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="A description of the severity of the feature."
        ),

        DataElement(
            ordinal="6.2.8",
            section="6. Phenotypic Feature",
            elementName="Modifiers",
            elementCode=Coding(system=GA4GH, code="phenotypicfeature.modifier"),
            elementCodeSystem=GA4GH,
            dataType=Code,
            dataSpecification=["OntologyClass (HPO, NCBITAXON, SCT)"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Suggested: Observation.extension",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.modifiers",
            recommendedDataSpec_phenopackets="list of OntologyClass",
            description="Any number of additional modifiers describing a" 
                        " specific phenotypic feature further, such as severity"
                        " (HP:0012824), clinical modifiers (HP:0012823), or"
                        " linking causative infectious agents using the"
                        " NCBITAXON Ontology."
        ),

        DataElement(
            ordinal="6.2.9",
            section="6.2 Phenotypic Feature",
            elementName="Evidence",
            elementCode=Coding(system=GA4GH, code="phenotypicfeature.evidence"),
            elementCodeSystem=GA4GH,
            dataType=Code,
            dataSpecification=["ECO"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.method",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="PhenotypicFeature.evidence",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The evidence for an assertion of the observation of a "
                        "type defined within the Evidence & Conclusion "
                        "Ontology (ECO)."
        ),
#_______________________________________________________________________________        
        # 6.3 Measurements

        DataElement(
            ordinal="6.3.1",
            section="6.3 Measurement",
            elementName="Assay",
            elementCode=Coding(system=NCIT, code="C60819"),
            elementCodeSystem=NCIT,
            dataType=Code,
            dataSpecification=["OntologyClass (e.g. LOINC)"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.code",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="Measurement.assay",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="A class that describes the assay used to produce"
                         "the measurement."                             
            ),

        DataElement(
            ordinal="6.3.2",
            section="6.3 Measurement",
            elementName="Value",
            elementCode=Coding(system=NCIT, code="C25712"),
            elementCodeSystem=NCIT,
            dataType=Value,
            dataSpecification=["float"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.value[x]",
            recommendedDataSpec_fhir="Quantity|integer",
            phenopacketSchemaElement_v2_0="Measurement.measurement_value",
            recommendedDataSpec_phenopackets="Quantity[double/float]",
            description="The result of the measurement."
        ),

        DataElement(
            ordinal="6.3.3",
            section="6.3 Measurement",
            elementName="Value Unit",
            elementCode=Coding(system=NCIT, code="C92571"),
            elementCodeSystem=NCIT,
            dataType=Code,
            dataSpecification=["UO"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.value[x].unit",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="Measurement.measurement_value",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The unit of the result's measurement."
        ),

        DataElement(
            ordinal="6.3.4",
            section="6.3 Measurement",
            elementName="Interpretation",
            elementCode=Coding(system=NCIT, code="C41255"),
            elementCodeSystem=NCIT,
            dataType=Code,
            dataSpecification=["NCIT"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.interpretation",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The interpretation of the measurement (e.g.: "
                        "Below/Within/Above age-related reference range, "
                        "Absent/Low/Normal, or Positive/Negative)."
        ),

        DataElement(
            ordinal="6.3.5",
            section="6.3 Measurement",
            elementName="Time Observed",
            elementCode=Coding(system=NCIT, code="C82577"),
            elementCodeSystem=NCIT,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Observation.effectiveDateTime",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="Measurement.time_observed",
            recommendedDataSpec_phenopackets="TimeElement",
            description="Time at which the measurement was performed."
        ),

        DataElement(
            ordinal="6.3.6",
            section="6.3 Measurement",
            elementName="Procedure",
            elementCode=Coding(system=SNOMED, code="122869004"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["OntologyClass (e.g. NCIT, SNOMED)"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Procedure.code",
            recommendedDataSpec_fhir="Measurement.procedure",
            phenopacketSchemaElement_v2_0="Measurement.procedure",
            recommendedDataSpec_phenopackets="Measurement.procedure",
            description="Clinical procedure performed to acquire the sample "
                        "used for the measurement."
        ),

#_______________________________________________________________________________
        # 6.4 Family History
        DataElement(
            ordinal="6.4.1",
            section="6.4 Family History",
            elementName="Family Member Pseudonym",
            elementCode=Coding(system=CustomCode, code="family_member_id"),
            elementCodeSystem=CustomCode,
            dataType=Identifier,
            dataSpecification=["n/a"],
            valueSet="n/a",
            fhirExpression_v4_0_1="FamilyMemberHistory.identifier",
            recommendedDataSpec_fhir="Identifier",
            phenopacketSchemaElement_v2_0="Family.Pedigree.Person.individual_id",
            recommendedDataSpec_phenopackets="string",
            description="A unique identifier or local pseudonym for the family"
                        "member."
        )   ,         
        DataElement(
            ordinal="6.4.2",
            section="6.4 Family History",
            elementName="Propositus/-a",
            elementCode=Coding(system=SNOMED, code="64245008"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Propositus Value Set v2.0.0",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="(Family.relatives → 1 Phenopacket "
                                            "per family member)",
            recommendedDataSpec_phenopackets="(Family.relatives → 1 Phenopacket"
                                            " per family member)",
            description="Is the individual the first affected family member who "
                        "seeks medical attention for a genetic disorder, leading"
                        " to the diagnosis of other family members. Disclaimer: "
                        "The SCT code for propositus (64245008) refers to any "
                        " gender."
        ),
        DataElement(
            ordinal="6.4.3",
            section="6.4 Family History",
            elementName="Relationship of the Individual to the Propositus",
            elementCode=Coding(system=SNOMED, code="408732007"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="Family Relationship To Index Case Value Set v2.0.0",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="(Family.relatives → 1 Phenopacket "
                                            "per family member)",
            recommendedDataSpec_phenopackets="(Family.relatives → 1 Phenopacket"
                                            " per family member)",
            description="Specifies the familial relationship of the individual "
                        "being evaluated to the propositus. Disclaimer: The "
                        "SNOMED code for propositus (64245008) refers to "
                        "any gender."
        ),
        DataElement(
            ordinal="6.4.4",
            section="6.4 Family History",
            elementName="Consanguinity",
            elementCode=Coding(system=SNOMED, code="842009"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Consanguinity Value Set v2.0.0",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Family.consanguinous_parents",
            recommendedDataSpec_phenopackets="boolean",
            description="The presence of a biological relationship between "
                        "parents who are related by blood, typically as first "
                        "or second cousins."
        ),
        DataElement(
            ordinal="6.4.5",
            section="6.4 Family History",
            elementName="Family Member Relationship",
            elementCode=Coding(system=SNOMED, code="444018008"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="FamilyMember Value Set v2.0.0",
            fhirExpression_v4_0_1="FamilyMemberHistory.relationship.coding",
            recommendedDataSpec_fhir="ValueSet: FamilyMember",
            phenopacketSchemaElement_v2_0="Family.Pedigree.Person.individual_id",
            recommendedDataSpec_phenopackets="string",
            description="Specifies the relationship of the selected family "
                        "member to the patient."
        ),
        DataElement(
            ordinal="6.4.6",
            section="6.4 Family",
            elementName="Family Member Record Status",
            elementCode=Coding(system=HL7FHIR, code="familymemberhistory.status"),
            elementCodeSystem=HL7FHIR,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="FamilyHistoryStatus Value Set v2.0.0",
            fhirExpression_v4_0_1="FamilyMemberHistory.status",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Specifies the record’s status of the family history of"
                        " a specific family member."
        ),        
        DataElement(
            ordinal="6.4.7",
            section="6.4 Family",
            elementName="Family Member Sex",
            elementCode=Coding(system=LOINC, code="54123-5"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["VSe", "VSc"],
            valueSet="AdministrativeGender Value Set v2.0.0",
            fhirExpression_v4_0_1="FamilyMemberHistory.sex",
            recommendedDataSpec_fhir="ValueSet: AdministrativeGender",
            phenopacketSchemaElement_v2_0="Family.Pedigree.Person.sex",
            recommendedDataSpec_phenopackets="ValueSet: Sex",
            description="Specifies the sex (or gender) of the specific family "
                        "member. If possible, the sex assigned at birth "
                        "should be selected."
        ),
        DataElement(
            ordinal="6.4.8",
            section="6.4 Family",
            elementName="Family Member Age",
            elementCode=Coding(system=LOINC, code="54141-7"),
            elementCodeSystem=LOINC,
            dataType=Integer,
            dataSpecification=["Integer"],
            valueSet="n/a",
            fhirExpression_v4_0_1="FamilyMemberHistory.ageAge",
            recommendedDataSpec_fhir="Age",
            phenopacketSchemaElement_v2_0="(Family.relatives → 1 Phenopacket "
                                            "per family member)",
            recommendedDataSpec_phenopackets="(Family.relatives → 1 Phenopacket"
                                            " per family member)",
            description="Records the current age of the selected family member."
        ),
        DataElement(
            ordinal="6.4.9",
            section="6.4 Family",
            elementName="Family Member Date of Birth",
            elementCode=Coding(system=LOINC, code="54124-3"),
            elementCodeSystem=LOINC,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="FamilyMemberHistory.bornDate",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="(Family.relatives → 1 Phenopacket "
                                            "per family member)",
            recommendedDataSpec_phenopackets="(Family.relatives → 1 Phenopacket"
                                            " per family member)",
            description="Records the date of birth of the selected family member."
        ),
        DataElement(
            ordinal="6.4.10",
            section="6.4 Family",
            elementName="Family Member Deceased",
            elementCode=Coding(system=SNOMED, code="740604001"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Deceased Value Set v2.0.0",
            fhirExpression_v4_0_1="FamilyMemberHistory.deceased.deceasedBoolean",
            recommendedDataSpec_fhir="boolean",
            phenopacketSchemaElement_v2_0="(Family.relatives → 1 Phenopacket "
                                            "per family member)",
            recommendedDataSpec_phenopackets="(Family.relatives → 1 Phenopacket"
                                            " per family member)",
            description="Indicates whether the selected family member is "
                        "deceased."
        ),
        DataElement(
            ordinal="6.4.11",
            section="6.4 Family",
            elementName="Family Member Cause of Death",
            elementCode=Coding(system=LOINC, code="54112-8"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["ICD10CM"],
            valueSet="n/a",
            fhirExpression_v4_0_1="FamilyMemberHistory.condition.code & "
                                  "FamilyMemberHistory.condition."
                                  "contributedToDeath",
            recommendedDataSpec_fhir="Code",
            phenopacketSchemaElement_v2_0="(Family.relatives → 1 Phenopacket "
                                            "per family member)",
            recommendedDataSpec_phenopackets="(Family.relatives → 1 Phenopacket"
                                            " per family member)",
            description="Records the cause of death of the selected deceased" 
                        "family member."
        ),
        DataElement(
            ordinal="6.4.12",
            section="6.4 Family",
            elementName="Family Member Deceased Age",
            elementCode=Coding(system=LOINC, code="92662-6"),
            elementCodeSystem=LOINC,
            dataType=Integer,
            dataSpecification=["Integer"],
            valueSet="n/a",
            fhirExpression_v4_0_1="FamilyMemberHistory.deceasedAge",
            recommendedDataSpec_fhir="Family.relatives",
            phenopacketSchemaElement_v2_0="Family.relatives",
            recommendedDataSpec_phenopackets="Family.relatives",
            description="Records the age at which the selected family"
                        " member died."
        ),
        DataElement(
            ordinal="6.4.13",
            section="6.4 Family",
            elementName="Family Member Disease",
            elementCode=Coding(system=LOINC, code="75315-2"),
            elementCodeSystem=LOINC,
            dataType=Code,
            dataSpecification=["Ontology Class", "ORDO", "ICD-10-CM", "ICD-11",
                               "MONDO", "OMIM_p"],
            valueSet="n/a",
            fhirExpression_v4_0_1="FamilyMemberHistory.condition.code",
            recommendedDataSpec_fhir="Family.relatives",
            phenopacketSchemaElement_v2_0="Family.relatives",
            recommendedDataSpec_phenopackets="Family.relatives",
            description="Indicates whether the selected family member is "
                        "affected by the same rare disease as the individual."
        ),
#_______________________________________________________________________________
        # 7 Consent
        DataElement(
            ordinal="7.1",
            section="7. Consent",
            elementName="Consent Status",
            elementCode=Coding(system=SNOMED, code="309370004"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VS"],
            valueSet="Consent Status Value Set v2.0.0",
            fhirExpression_v4_0_1="Consent.status",
            recommendedDataSpec_fhir="ValueSet: ConsentStatus",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Indicates the current status of the consent."
        ),
        DataElement(
            ordinal="7.2",
            section="7. Consent",
            elementName="Consent Date",
            elementCode=Coding(system=HL7FHIR, code="consent.datetime"),
            elementCodeSystem=HL7FHIR,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Consent.dateTime",
            recommendedDataSpec_fhir="DateTime",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Records the date when the consent was given."
        ),
        DataElement(
            ordinal="7.3",
            section="7. Consent",
            elementName="Health Policy Monitoring",
            elementCode=Coding(system=SNOMED, code="386318002"),
            elementCodeSystem=SNOMED,
            dataType=String,
            dataSpecification=["n/a"],
            valueSet="n/a",
            fhirExpression_v4_0_1="Consent.policy",
            recommendedDataSpec_fhir="string",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="References to the policies that are included in this"
                        "consent scope."
        ),
        DataElement(
            ordinal="7.4",
            section="7. Consent",
            elementName="Agreement to be Contacted for Research",
            elementCode=Coding(system=CustomCode,
                                code="consent_contact_research"),
            elementCodeSystem=CustomCode,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Contact for Research Value Set v2.0.0",
            fhirExpression_v4_0_1="Consent.scope.coding",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Indicates whether the patient agrees to be contacted "
                        "for research."
        ),
        DataElement(
            ordinal="7.5",
            section="7. Consent",
            elementName="Consent to the Reuse of Data",
            elementCode=Coding(system=CustomCode,
                                code="conset_data_reuse"),
            elementCodeSystem=CustomCode,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Data Reuse Consent Value Set v2.0.0",
            fhirExpression_v4_0_1="Consent.scope.coding",
            recommendedDataSpec_fhir="CodeableConcept",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Indicates whether the patient consents to the reuse of their data."
        ),
        DataElement(
            ordinal="7.6",
            section="7. Consent",
            elementName="Biological Sample",
            elementCode=Coding(system=SNOMED, code="123038009"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe"],
            valueSet="Biological Sample Consent Value Set v2.0.0",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Indicates whether a patient's biological sample is "
                        "available for research."
        ),
        DataElement(
            ordinal="7.7",
            section="7. Consent",
            elementName="Link to a Biobank",
            elementCode=Coding(system=CustomCode, code="biobank_link"),
            elementCodeSystem=CustomCode,
            dataType=String,
            dataSpecification=["n/a"],
            valueSet="n/a",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="If there is a biological sample, this data element"
                        " indicates the link to the biobank of the individual's"
                        " biological sample."
        ),
        DataElement(
            ordinal="8.1",
            section="8. Disability",
            elementName="Classification of Functioning / Disability",
            elementCode=Coding(system=CustomCode, code="icf_score"),
            elementCodeSystem=CustomCode,
            dataType=Code,
            dataSpecification=["ICF"],
            valueSet="n/a",
            fhirExpression_v4_0_1="n/a",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="Specifies the classification of the individualss "
                        "functioning or disability according to the "
                        "International Classification of Functioning, Disability"
                        " and Health (ICF)."
        )

    ]
