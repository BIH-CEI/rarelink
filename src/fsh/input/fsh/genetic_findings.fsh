Alias: SNOMEDCT = http://snomed.info/sct
Alias: LOINC = https://loinc.org/
Alias: HGVS = http://varnomen.hgvs.org/
Alias: GA4GH = https://www.ga4gh.org/product/phenopackets/

Profile: RareLinkGeneticFindings
Parent: Observation
Id: rarelink-observation-genetic-findings
Title: "RareLink Observation Genetic Findings"
Description: "A RareLink-specific profile for capturing genetic findings."

* meta.profile = "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/finding" (exactly)

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code.coding.system = SNOMEDCT
* code.coding.code = #106221001
* code.coding.display = "Genetic Finding"

* subject 1..1
* subject.reference = "Patient/{id}"

* interpretation 0..*
* interpretation.coding 0..1
* interpretation.coding.system from GA4GH (extensible)
* interpretation.coding.code from InterpretationStatusVS (required)

* method 0..1
* method.coding 0..1
* method.coding.system from LOINC (required)

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink Observation Genetic Findings</strong></p>
  <p>This profile is based on the RareLink-CDM Section (6.1) Genetic Findings, capturing structured genetic findings data.</p>
</div>
"""

* component 0..*

// * component contains GeneticMutationString named genetic_mutation_string 0..1
// * component contains GenomicDNAChange named genomic_dna_change 0..1
// * component contains SequenceDNAChange named sequence_dna_change 0..1
// * component contains AminoAcidChange named amino_acid_change 0..1
// * component contains AlleleState named allele_state 0..1
// * component contains GenomicSourceClass named genomic_source_class 0..1
// * component contains VariantType named variant_type 0..1

// * component[GeneticMutationString].code.coding.system = LOINC
// * component[GeneticMutationString].code.coding.code = #LP7824-8
// * component[GeneticMutationString].code.coding.display = "Genetic Mutation String"
// * component[GeneticMutationString].valueString MS

// * component[GenomicDNAChange].code.coding.system = LOINC
// * component[GenomicDNAChange].code.coding.code = #81290-9
// * component[GenomicDNAChange].code.coding.display = "Genomic DNA Change"
// * component[GenomicDNAChange].valueCodeableConcept.coding.system = HGVS
// * component[GenomicDNAChange].valueCodeableConcept.coding.code MS

// * component[SequenceDNAChange].code.coding.system = LOINC
// * component[SequenceDNAChange].code.coding.code = #48004-6
// * component[SequenceDNAChange].code.coding.display = "Sequence DNA Change"
// * component[SequenceDNAChange].valueCodeableConcept.coding.system = HGVS
// * component[SequenceDNAChange].valueCodeableConcept.coding.code MS

// * component[AminoAcidChange].code.coding.system = LOINC
// * component[AminoAcidChange].code.coding.code = #48005-3
// * component[AminoAcidChange].code.coding.display = "Amino Acid Change"
// * component[AminoAcidChange].valueCodeableConcept.coding.system = HGVS
// * component[AminoAcidChange].valueCodeableConcept.coding.code MS

// * component[AlleleState].code.coding.system = LOINC
// * component[AlleleState].code.coding.code = #53034-5
// * component[AlleleState].code.coding.display = "geneticsAllele.State"
// * component[AlleleState].valueCodeableConcept.coding.system from LOINC (required)
// * component[AlleleState].valueCodeableConcept.coding.code from ZygosityVS (required)

// * component[GenomicSourceClass].code.coding.system = LOINC
// * component[GenomicSourceClass].code.coding.code = #48002-0
// * component[GenomicSourceClass].code.coding.display = "GenomicSourceClass"
// * component[GenomicSourceClass].valueCodeableConcept.coding.system from LOINC (required)
// * component[GenomicSourceClass].valueCodeableConcept.coding.code from GenomicSourceClassVS (required)

// * component[VariantType].code.coding.system = LOINC
// * component[VariantType].code.coding.code = #48019-4
// * component[VariantType].code.coding.display = "Variant.Type (DNA Change Type)"
// * component[VariantType].valueCodeableConcept.coding.system from LOINC (required)
// * component[VariantType].valueCodeableConcept.coding.code from DNAChangeTypeVS (required)

// * component[ReferenceGenome].code.coding.system = LOINC
// * component[ReferenceGenome].code.coding.code = #62374-4
// * component[ReferenceGenome].code.coding.display = "Reference Genome"
// * component[ReferenceGenome].valueCodeableConcept.coding.system from LOINC (required)
// * component[ReferenceGenome].valueCodeableConcept.coding.code from ReferenceGenomeVS (required)


ValueSet: InterpretationStatusVS
Id: interpretation-status-vs
Title: "Interpretation Status Value Set"
Description: "Value set for interpretation statuses."
* GA4GH#UNKNOWN_STATUS "No information is available about the status"
* GA4GH#REJECTED "The variant or gene is not related to the diagnosis"
* GA4GH#CANDIDATE "The variant or gene is possibly related to the diagnosis"
* GA4GH#CONTRIBUTORY "The variant or gene is related to the diagnosis"
* GA4GH#CAUSATIVE "The variant or gene is causative of the diagnosis"

ValueSet: ProgressStatusInterpretationVS
Id: progress-status-interpretation-vs
Title: "Progress Status of Interpretation Value Set"
Description: "Value set for capturing the progress status of interpretation."
* GA4GH#UNKNOWN_PROGRESS "No information is available about the diagnosis"
* GA4GH#IN_PROGRESS "No diagnosis has been found to date but additional differential diagnostic work is in progress."
* GA4GH#COMPLETED "The work on the interpretation is complete."
* GA4GH#SOLVED "The interpretation is complete and also considered to be a definitive diagnosis"
* GA4GH#UNSOLVED "The interpretation is complete but no definitive diagnosis was found."

ValueSet: StructuralVariantAnalysisMethodVS
Id: structural-variant-analysis-method-vs
Title: "Structural Variant Analysis Method Value Set"
Description: "Value set for capturing structural variant analysis methods."
* LOINC#LA26406-1 "Karyotyping"
* LOINC#LA26404-6 "FISH"
* LOINC#LA26418-6 "PCR"
* LOINC#LA26419-4 "qPCR (real-time PCR)"
* LOINC#LA26400-4 "SNP array"
* LOINC#LA26813-8 "Restriction fragment length polymorphism (RFLP)"
* LOINC#LA26810-4 "DNA hybridization"
* LOINC#LA26398-0 "Sequencing"
* LOINC#LA26415-2 "MLPA"
* LOINC#LA46-8 "Other"

ValueSet: ZygosityVS
Id: zygosity-vs
Title: "Zygosity Value Set"
Description: "Value set for capturing zygosity."
* LOINC#LA6705-3 "Homozygous"
* LOINC#LA6706-1 "Heterozygous"
* LOINC#LA26217-2 "Compound heterozygous"
* LOINC#LA26220-6 "Double heterozygous"
* LOINC#LA6707-9 "Hemizygous"
* LOINC#LA6703-8 "Heteroplasmic"
* LOINC#LA6704-6 "Homoplasmic"
* LOINC#53034_5_other "Other"

ValueSet: ReferenceGenomeVS
Id: reference-genome-vs
Title: "Reference Genome Value Set"
Description: "Value set for reference sequence assemblies."
* LOINC#LA14032-9 "NCBI Build 34 (hg16)"
* LOINC#LA14029-5 "GRCh37 (hg19)"
* LOINC#LA14030-3 "NCBI Build 36.1 (hg18)"
* LOINC#LA14031-1 "NCBI Build 35 (hg17)"
* LOINC#LA26806-2 "GRCh38 (hg38)"

ValueSet: GenomicSourceClassVS
Id: genomic-source-class-vs
Title: "Genomic Source Class Value Set"
Description: "Value set for capturing genomic source classes."
* LOINC#LA6683-2 "Germline"
* LOINC#LA6684-0 "Somatic"
* LOINC#LA10429-1 "Fetal"
* LOINC#LA18194-3 "Likely germline"
* LOINC#LA18195-0 "Likely somatic"
* LOINC#LA18196-8 "Likely fetal"
* LOINC#LA18197-6 "Unknown genomic origin"
* LOINC#LA26807-0 "De novo"

ValueSet: DNAChangeTypeVS
Id: dna-change-type-vs
Title: "DNA Change Type Value Set"
Description: "Value set for capturing DNA change types."
* LOINC#LA9658-1 "Wild type"
* LOINC#LA6692-3 "Deletion"
* LOINC#LA6686-5 "Duplication"
* LOINC#LA6687-3 "Insertion"
* LOINC#LA6688-1 "Insertion/Deletion"
* LOINC#LA6689-9 "Inversion"
* LOINC#LA6690-7 "Substitution"
* LOINC#48019_4_other "Other"

ValueSet: ClinicalSignificanceACMGVS
Id: clinical-significance-acmg-vs
Title: "Clinical Significance ACMG Value Set"
Description: "Value set for ACMG clinical significance levels."
* LOINC#LA6668-3 "Pathogenic"
* LOINC#LA26332-9 "Likely pathogenic"
* LOINC#LA26333-7 "Uncertain significance"
* LOINC#LA26334-5 "Likely benign"
* LOINC#LA6675-8 "Benign"
* LOINC#LA4489-6 "Unknown"

ValueSet: ClinicalAnnotationEvidenceVS
Id: clinical-annotation-evidence-vs
Title: "Clinical Annotation Level of Evidence Value Set"
Description: "Value set for clinical annotation levels of evidence."
* LOINC#LA30200-2 "Very strong evidence pathogenic"
* LOINC#LA30201-0 "Strong evidence pathogenic"
* LOINC#LA30202-8 "Moderate evidence pathogenic"
* LOINC#LA30203-6 "Supporting evidence pathogenic"
* LOINC#LA30204-4 "Supporting evidence benign"
* LOINC#LA30205-1 "Strong evidence benign"
* LOINC#LA30206-9 "Stand-alone evidence pathogenic"
