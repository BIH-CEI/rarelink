Alias: LOINC = https://loinc.org/
Alias: HL7FHIR = http://hl7.org/fhir/R4/
Alias: NCIT = https://ncit.nci.nih.gov/

Profile: RareLinkIPSMeasurementsVitalSigns
Parent: Observation
Id: rarelink-observation-vital-signs
Title: "RareLink Vital Signs Measurements"
Description: "A RareLink-specific profile for vital signs measurements."

* meta.profile ^slicing.discriminator.type = #pattern
* meta.profile ^slicing.discriminator.path = "$this"
* meta.profile ^slicing.rules = #open
* meta.profile contains vitalSignsProfile 1..1
* meta.profile[vitalSignsProfile] = "http://hl7.org/fhir/StructureDefinition/vitalsigns|4.0.1"

* status 1..1
* status from http://hl7.org/fhir/ValueSet/observation-status (required)

* category 1..1
* category.coding 1..1
* category.coding.system = "http://terminology.hl7.org/CodeSystem/observation-category"
* category.coding.code = #vital-signs

* code 1..1
* code.coding from http://hl7.org/fhir/ValueSet/observation-vitalsignresult

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* effective[x] 1..1

* value[x] 0..1
* valueQuantity 0..1
* valueQuantity.value MS
* valueQuantity.unit MS

* interpretation 0..*
* interpretation.coding 0..1
* interpretation.coding.system from NCIT (required)
* interpretation.coding.code MS

* method 0..1
* method.coding 0..*
* method.coding.system from LOINC (extensible)
* method.coding.code MS
