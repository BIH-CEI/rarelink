# Artifacts Summary - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [RareLink Condition for Undiagnosed RD Case](StructureDefinition-rarelink-condition-undiagnosed-rd-case.md) | A RareLink-specific Condition profile for documenting undiagnosed rare disease cases based on the IPS Condition profile. |
| [RareLink Consent](StructureDefinition-rarelink-consent.md) | A RareLink-specific Consent profile based on the Consent resource. |
| [RareLink Diagnostic Implication Observation](StructureDefinition-rarelink-diagnostic-implication.md) | A RareLink-specific profile extending the HL7 Genomics Reporting 'diagnostic-implication' profile for documenting diagnostic significance, evidence levels, and associated phenotypes (genetic_findings.diagnostic_implication). |
| [RareLink Encounter](StructureDefinition-rarelink-encounter.md) | A RareLink-specific Encounter profile based on the Encounter resource. |
| [RareLink Family History](StructureDefinition-rarelink-familyhistory.md) | A RareLink-specific FamilyMemberHistory profile based on the FamilyMemberHistory resource. |
| [RareLink Genetic Variant Observation](StructureDefinition-rarelink-genetic-variant.md) | A RareLink-specific profile for documenting genetic findings (genetic_findings.variant), based on the HL7 Genomics Reporting variant profile. |
| [RareLink IPS Condition](StructureDefinition-rarelink-ips-condition.md) | A RareLink-specific Condition profile based on the IPS Condition profile. |
| [RareLink IPS Measurement Laboratory](StructureDefinition-rarelink-ips-measurement-laboratory.md) | A RareLink-specific profile for laboratory measurements based on the IPS Observation profile. |
| [RareLink IPS Measurement Radiology](StructureDefinition-rarelink-ips-measurement-radiology.md) | A RareLink-specific profile for radiology measurements based on the IPS Observation profile. |
| [RareLink IPS Patient](StructureDefinition-rarelink-ips-patient.md) | A RareLink-specific profile for the IPS Patient resource. |
| [RareLink IPS Procedure](StructureDefinition-rarelink-ips-procedure.md) | A RareLink-specific profile for the IPS Procedure resource. |
| [RareLink Observation Age Category](StructureDefinition-rarelink-observation-age-category.md) | A RareLink-specific profile for capturing the age category of a patient as an observation, based on the ERDRI-CDS value set. |
| [RareLink Observation Gestation at Birth](StructureDefinition-rarelink-observation-gestation-at-birth.md) | A RareLink-specific profile for capturing gestation length at birth. |
| [RareLink Observation Karyotypic Sex](StructureDefinition-rarelink-karyotypic-sex.md) | A RareLink-specific profile for capturing karyotypic sex information. |
| [RareLink Observation Measurements (Others)](StructureDefinition-rarelink-observation-measurements-others.md) | A RareLink-specific profile for measurements that do not fall under IPS laboratory, radiology, procedures, or vital signs. |
| [RareLink Observation Phenotypic Feature](StructureDefinition-rarelink-phenotypic-feature.md) | A RareLink-specific profile for capturing phenotypic features. |
| [RareLink Vital Signs Measurements](StructureDefinition-rarelink-observation-vital-signs.md) | A RareLink-specific profile for vital signs measurements. |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Age at Diagnosis](StructureDefinition-age-at-diagnosis.md) | ERDRI-CDS - The age at which the condition was diagnosed. |
| [Age at Onset](StructureDefinition-age-at-onset.md) | ERDRI-CDS - The age at which the condition first appeared. |
| [Agreement to Be Contacted](StructureDefinition-erdri-agreement-to-be-contacted.md) | ERDRI-CDS - Agreement to be contacted for research purposes. |
| [Birth Place](StructureDefinition-birth-place.md) | The patient's place of birth. |
| [Cause of Death](StructureDefinition-cause-of-death.md) | The cause of death for the patient. |
| [Cause of Death Code](StructureDefinition-cause-of-death-code.md) | The ICD-10 code representing the cause of death. |
| [Cause of Death Definition](StructureDefinition-cause-of-death-definition.md) | The SNOMED CT definition of the cause of death concept. |
| [Clinical Modifier](StructureDefinition-clinical-modifier-1.md) | Modifier describing a specific phenotypic feature further (derived from clinical modifiers - HP:0012823) |
| [Clinical Modifier](StructureDefinition-clinical-modifier-2.md) | Modifier describing a specific phenotypic feature further (derived from clinical modifiers - HP:0012823) |
| [Clinical Modifier](StructureDefinition-clinical-modifier-3.md) | Modifier describing a specific phenotypic feature further (derived from clinical modifiers - HP:0012823) |
| [Consanguinity](StructureDefinition-consanguinity.md) | Indicates whether there is consanguinity in the family relationship. |
| [Consent to Reuse Data](StructureDefinition-erdri-consent-to-reuse-data.md) | ERDRI-CDS - Consent to the reuse of data. |
| [Date of Admission](StructureDefinition-date-of-admission.md) | The date of the patient's admission. |
| [Phenotype Causing Organism](StructureDefinition-causing-agent.md) | The organism that is causing the phenotypic feature (e.g., a virus, bacteria, etc.). |
| [Phenotype Severity](StructureDefinition-phenotype-severity.md) | The severity of the phenotypic feature. |
| [Phenotype Status](StructureDefinition-phenotype-status.md) | Captures the status of a phenotypic feature, such as confirmed present or refuted. |
| [Phenotype Temporal Pattern](StructureDefinition-temporal-pattern.md) | The speed at which a disease manifestations appear and develop. |
| [Propositus](StructureDefinition-propositus.md) | Indicates whether the family member is the propositus. |
| [Recorded Sex at Birth](StructureDefinition-recorded-sex-at-birth.md) | The sex assigned to the patient at birth. |
| [Resolution Date](StructureDefinition-resolution-date.md) | The date when the phenotypic feature resolved. |
| [Vital Status](StructureDefinition-vital-status.md) | Coded representation of a patient's vital status |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Age Category Value Set](ValueSet-age-category-vs.md) | Value set for capturing the age category of a patient. |
| [Age at Diagnosis Value Set](ValueSet-age-at-diagnosis-vs.md) | Value set for capturing age at diagnosis. |
| [Age at Onset Value Set](ValueSet-age-at-onset-vs.md) | Value set for capturing age at onset. |
| [Age of Onset Value Set](ValueSet-age-of-onset-vs.md) | Value set for capturing the age of onset for phenotypes. |
| [Agreement to Be Contacted Value Set (ERDRI-CDS)](ValueSet-agreement-to-be-contacted-vs.md) | Value set for capturing agreement to be contacted for research. |
| [Clinical Significance Value Set](ValueSet-clinical-significance-vs.md) | LOINC LA codes for the clinical significance of a variant. |
| [Consanguinity Value Set](ValueSet-consanguinity-vs.md) | Value set for indicating whether there is consanguinity in the family relationship. |
| [Consent to Reuse Data Value Set (ERDRI-CDS)](ValueSet-consent-to-reuse-vs.md) | Value set for capturing consent to reuse data. |
| [DNA Change Type Value Set](ValueSet-dna-change-type-vs.md) | LOINC LA codes enumerating various DNA change types. |
| [Encounter Class Value Set](ValueSet-encounter-class-vs.md) | Value set for encounter classes, including custom RareLink-specific codes. |
| [Family Member Sex Value Set](ValueSet-family-sex-vs.md) | Value set for capturing the sex of a family member. |
| [Family Relationship Value Set](ValueSet-family-relationship-vs.md) | Value set for capturing family member relationships. |
| [Genomic Source Class Value Set](ValueSet-genomic-source-class-vs.md) | LOINC LA codes enumerating germline, somatic, fetal, etc. |
| [Karyotypic Sex Value Set](ValueSet-karyotypic-sex-vs.md) | Value set for capturing karyotypic sex. |
| [Level of Evidence Value Set](ValueSet-level-of-evidence-vs.md) | LOINC LA codes describing evidence strength for a variant. |
| [Phenotype Severity Value Set](ValueSet-phenotype-severity-vs.md) | Value set for capturing phenotype severity. |
| [Phenotype Status Value Set](ValueSet-phenotype-status-vs.md) | Value set for capturing phenotype status. |
| [Propositus Value Set](ValueSet-propositus-vs.md) | Value set for indicating whether the family member is the propositus. |
| [Reference Genome Value Set](ValueSet-reference-genome-vs.md) | LOINC LA codes specifying the reference genome build. |
| [Severity Value Set](ValueSet-severity-vs.md) | Value set for severity levels of conditions. |
| [Sex at Birth Value Set](ValueSet-sex-at-birth-vs.md) | Value set for capturing the sex assigned at birth. |
| [Structural Variant Method Value Set](ValueSet-structural-variant-method-vs.md) | LOINC LA codes enumerating methods for detecting structural variants. |
| [Temporal Pattern Value Set](ValueSet-temporal-pattern-vs.md) | Value set for capturing the temporal pattern of phenotypic features. |
| [Undiagnosed Rare Disease Case Value Set](ValueSet-undiagnosed-rd-case-vs.md) | Value set for capturing undiagnosed rare disease cases. |
| [Vital Status Value Set](ValueSet-vital-status-vs.md) | Value set for capturing the vital status of the patient. |
| [Zygosity Value Set](ValueSet-zygosity-vs.md) | LOINC LA codes enumerating various zygosity states. |

