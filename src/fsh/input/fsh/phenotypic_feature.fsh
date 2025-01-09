Alias: SNOMEDCT = http://snomed.info/sct
Alias: HP = http://www.human-phenotype-ontology.org

Profile: RareLinkPhenotypicFeature
Parent: Observation
Id: rarelink-phenotypic-feature
Title: "RareLink Observation Phenotypic Feature"
Description: "A RareLink-specific profile for capturing phenotypic features."

* meta.profile = "http://hl7.org/fhir/StructureDefinition/Observation|4.0.1" (exactly)

* status 1..1
* status = #registered

* code 1..1
* code.coding 1..1
* code.coding.system = HP
* code.coding.version = "2024-08-13"
* code.coding.code MS

* category 0..*
* category.coding 0..*
* category.coding.system from HP (required)
* category.coding.version = "2024-08-13"
* category.coding.code from AgeOfOnsetVS (required)

* subject 1..1
* subject.reference = "Patient/{id}"

* effective[x] 0..1
* effectiveDateTime MS

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink Phenotypic Feature</strong></p>
  <p>This profile is based on the RareLink-CDM Section (6.2) Phenotypic Features and the Observation resource.</p>
</div>
"""

// * component ^slicing.discriminator.type = #value
// * component ^slicing.discriminator.path = "code"
// * component ^slicing.rules = #open

// * component[phenotype_severity] 0..1
// * component[phenotype_severity].code.coding.system = HP
// * component[phenotype_severity].code.coding.code = #0012823
// * component[phenotype_severity].valueCodeableConcept.coding.system = HP
// * component[phenotype_severity].valueCodeableConcept.coding.code from SeverityVS (required)

// * component[causing_organism] 0..1
// * component[causing_organism].code.coding.system = "https://www.ncbi.nlm.nih.gov/taxonomy"
// * component[causing_organism].code.coding.version = "2024-07-03"

* extension contains PhenotypeStatus named phenotype_status 0..1
* extension contains ResolutionDate named resolution_date 0..1
* extension contains PhenotypeModifier named phenotype_modifier 0..1

* extension[PhenotypeStatus]
Extension: PhenotypeStatus
Id: phenotype-status
Title: "Phenotype Status"
Description: "Captures the status of a phenotypic feature, such as confirmed present or refuted."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system from SNOMEDCT (required)
* valueCodeableConcept.coding.code from PhenotypeStatusVS (required)

* extension[ResolutionDate]
Extension: ResolutionDate
Id: resolution-date
Title: "Resolution Date"
Description: "The date when the phenotypic feature resolved."
* value[x] only dateTime

* extension[PhenotypeModifier]
Extension: PhenotypeModifier
Id: phenotype-modifier
Title: "Phenotype Modifier"
Description: "Captures modifiers for the phenotypic feature, such as severity or specific classifications."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system from HP (required)
* valueCodeableConcept.coding.code MS


ValueSet: PhenotypeStatusVS
Id: phenotype-status-vs
Title: "Phenotype Status Value Set"
Description: "Value set for capturing phenotype status."
* SNOMEDCT#410605003 "Confirmed present"
* SNOMEDCT#723511001 "Refuted"

ValueSet: AgeOfOnsetVS
Id: age-of-onset-vs
Title: "Age of Onset Value Set"
Description: "Value set for capturing the age of onset for phenotypes."
* HP#0011460 "Embryonal onset (0w-8w embryonal)"
* HP#0011461 "Fetal onset (8w embryonal - birth)"
* HP#0003577 "Congenital onset (at birth)"
* HP#0003623 "Neonatal onset (0d-28d)"
* HP#0003593 "Infantile onset (28d-1y)"
* HP#0011463 "Childhood onset (1y-5y)"
* HP#0003621 "Juvenile onset (5y-15y)"
* HP#0011462 "Young adult onset (16y-40y)"
* HP#0003596 "Middle age adult onset (40y-60y)"
* HP#0003584 "Late adult onset (60y+)"

ValueSet: TemporalPatternVS
Id: temporal-pattern-vs
Title: "Temporal Pattern Value Set"
Description: "Value set for capturing the temporal pattern of phenotypic features."
* HP#0011009 "Acute"
* HP#0011010 "Chronic"
* HP#0031914 "Fluctuating"
* HP#0025297 "Prolonged"
* HP#0031796 "Recurrent"
* HP#0031915 "Stable"
* HP#0011011 "Subacute"
* HP#0025153 "Transient"

ValueSet: PhenotypeSeverityVS
Id: phenotypie-severity-vs
Title: "Phenotype Severity Value Set"
Description: "Value set for capturing phenotype severity."
* HP#0012827 "Borderline"
* HP#0012825 "Mild"
* HP#0012826 "Moderate"
* HP#0012829 "Profound"
* HP#0012828 "Severe"
