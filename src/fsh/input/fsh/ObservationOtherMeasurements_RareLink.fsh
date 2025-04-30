Alias: HL7FHIR = http://hl7.org/fhir/R4/
Alias: NCIT = https://ncit.nci.nih.gov/
Alias: UO = http://www.ontobee.org/ontology/UO
Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkIPSMeasurementsOthers
Parent: Observation
Id: rarelink-observation-measurements-others
Title: "RareLink Observation Measurements (Others)"
Description: "A RareLink-specific profile for measurements that do not fall under IPS laboratory, radiology, procedures, or vital signs."

* meta.profile ^slicing.discriminator.type = #pattern
* meta.profile ^slicing.discriminator.path = "$this"
* meta.profile ^slicing.rules = #open
* meta.profile contains baseProfile 1..1
* meta.profile[baseProfile] = "https://github.com/BIH-CEI/rarelink/blob/develop/src/fsh/input/fsh/ObservationOtherMeasruements_RareLink.fsh"

* status 1..1
* status MS

* category 1..1
* category.coding 1..1
* category.coding.system = "https://hl7.org/fhir/R4/codesystem-observation-category.html"
* category.coding.code MS
* category.coding.version = "4.0.1"

* code 1..1
* code.coding 1..1
* code.coding.system 1..1
* code.coding.code 1..1
* code.coding.system from NCIT
* code.coding.code = #C60819

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS


* effective[x] 0..1
* effectiveDateTime MS

* value[x] 0..1
* valueQuantity.system 1..1
* valueQuantity.code from UO (required)
* valueQuantity.system = "http://purl.obolibrary.org/obo/uo.owl"
* valueQuantity.code MS
* valueQuantity.value MS

* interpretation 0..* // CodeableConcept
* interpretation.coding 0..*
* interpretation.coding.system from NCIT (extensible)
* interpretation.coding.code MS

* method 0..1 // CodeableConcept
* method.coding 0..*
* method.coding.system from SNOMEDCT (extensible)
* method.coding.code MS
