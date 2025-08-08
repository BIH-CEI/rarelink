Alias: SNOMEDCT = http://snomed.info/sct
Alias: HP = http://purl.obolibrary.org/obo/hp.owl

Profile: RareLinkPhenotypicFeature
Parent: Observation
Id: rarelink-phenotypic-feature
Title: "RareLink Observation Phenotypic Feature"
Description: "A RareLink-specific profile for capturing phenotypic features."

* status 1..1
* status = #registered

* code 1..1
* code.coding 1..1
* code.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* code.coding.code MS

* category 0..*
* category.coding 0..*
* category.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* category.coding.code from AgeOfOnsetVS (required)

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* effective[x] 0..1
* effectiveDateTime MS

* bodySite 0..1

* extension contains PhenotypeStatus named phenotype_status 0..1
* extension contains ResolutionDate named resolution_date 0..1
* extension contains TemporalPattern named temporal_pattern 0..1
* extension contains PhenotypeSeverity named phenotype_severity 0..1
* extension contains ClinicalModifier1 named clinical_modifier_1 0..1
* extension contains ClinicalModifier2 named clinical_modifier_2 0..1
* extension contains ClinicalModifier3 named clinical_modifier_3 0..1
* extension contains CausingOrganism named causing_organism 0..1

* extension[PhenotypeStatus]
Extension: PhenotypeStatus
Id: phenotype-status
Title: "Phenotype Status"
Description: "Captures the status of a phenotypic feature, such as confirmed present or refuted."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://snomed.info/sct"
* valueCodeableConcept.coding.code from PhenotypeStatusVS (required)

* extension[ResolutionDate]
Extension: ResolutionDate
Id: resolution-date
Title: "Resolution Date"
Description: "The date when the phenotypic feature resolved."
* value[x] only dateTime

* extension[TemporalPattern]
Extension: TemporalPattern
Id: temporal-pattern
Title: "Phenotype Temporal Pattern"
Description: "The speed at which a disease manifestations appear and develop."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* valueCodeableConcept.coding.code from TemporalPatternVS (required)

* extension[PhenotypeSeverity]
Extension: PhenotypeSeverity
Id: phenotype-severity
Title: "Phenotype Severity"
Description: "The severity of the phenotypic feature."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* valueCodeableConcept.coding.code from PhenotypeSeverityVS (required)

* extension[ClinicalModifier1]
Extension: ClinicalModifier1
Id: clinical-modifier-1
Title: "Cliical Modifier"
Description: "Modifier describing a specific phenotypic feature further (deerived from clinical modifiers - HP:0012823)"
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* valueCodeableConcept.coding.code MS

* extension[ClinicalModifier2]
Extension: ClinicalModifier2
Id: clinical-modifier-2
Title: "Cliical Modifier"
Description: "Modifier describing a specific phenotypic feature further (deerived from clinical modifiers - HP:0012823)"
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* valueCodeableConcept.coding.code MS

* extension[ClinicalModifier3]
Extension: ClinicalModifier3
Id: clinical-modifier-3
Title: "Cliical Modifier"
Description: "Modifier describing a specific phenotypic feature further (deerived from clinical modifiers - HP:0012823)"
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://purl.obolibrary.org/obo/hp.owl"
* valueCodeableConcept.coding.code MS

* extension[CausingOrganism]
Extension: CausingOrganism
Id: causing-agent
Title: "Phenotype Causing Organism"
Description: "The organism that is causing the phenotypic feature (e.g., a virus, bacteria, etc.)."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://purl.obolibrary.org/obo/NCBITaxon.owl"
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
* HP#HP:0011460 "Embryonal onset (0w-8w embryonal)"
* HP#HP:0011461 "Fetal onset (8w embryonal - birth)"
* HP#HP:0003577 "Congenital onset (at birth)"
* HP#HP:0003623 "Neonatal onset (0d-28d)"
* HP#HP:0003593 "Infantile onset (28d-1y)"
* HP#HP:0011463 "Childhood onset (1y-5y)"
* HP#HP:0003621 "Juvenile onset (5y-15y)"
* HP#HP:0011462 "Young adult onset (16y-40y)"
* HP#HP:0003596 "Middle age adult onset (40y-60y)"
* HP#HP:0003584 "Late adult onset (60y+)"

ValueSet: TemporalPatternVS
Id: temporal-pattern-vs
Title: "Temporal Pattern Value Set"
Description: "Value set for capturing the temporal pattern of phenotypic features."
* HP#HP:0011009 "Acute"
* HP#HP:0011010 "Chronic"
* HP#HP:0031914 "Fluctuating"
* HP#HP:0025297 "Prolonged"
* HP#HP:0031796 "Recurrent"
* HP#HP:0031915 "Stable"
* HP#HP:0011011 "Subacute"
* HP#HP:0025153 "Transient"

ValueSet: PhenotypeSeverityVS
Id: phenotypie-severity-vs
Title: "Phenotype Severity Value Set"
Description: "Value set for capturing phenotype severity."
* HP#HP:0012827 "Borderline"
* HP#HP:0012825 "Mild"
* HP#HP:0012826 "Moderate"
* HP#HP:0012829 "Profound"
* HP#HP:0012828 "Severe"
