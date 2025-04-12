Alias: SNOMEDCT = http://snomed.info/sct
Alias: ORPHANET = http://www.orpha.net/
Alias: HL7FHIR = http://hl7.org/fhir/R4/
Alias: LOINC = https://loinc.org/
Alias: UO = http://www.ontobee.org/ontology/UO
Alias: NCIT = https://ncit.nci.nih.gov/

Profile: RareLinkIPSMeasurementLaboratory
Parent: Observation-results-laboratory-pathology-uv-ips
Id: rarelink-ips-measurement-laboratory
Title: "RareLink IPS Measurement Laboratory"
Description: "A RareLink-specific profile for laboratory measurements based on the IPS Observation profile."

* meta.profile ^slicing.discriminator.type = #pattern
* meta.profile ^slicing.discriminator.path = "$this"
* meta.profile ^slicing.rules = #open
* meta.profile contains ipsProfile 1..1
* meta.profile[ipsProfile] = "http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-laboratory-pathology-uv-ips|2.0.0-ballot"

* status 1..1
* status = "http://hl7.org/fhir/ValueSet/observation-status"

* category 1..1
* category.coding 1..1
* category.coding.system = "http://terminology.hl7.org/CodeSystem/observation-category"
* category.coding.code = #laboratory

* code 1..1
* code.coding 1..1
* code.coding.system from LOINC (required)
* code.coding.code MS

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS


* effective[x] 1..1
* value[x] 0..1

* performer 1..*
* performer.display = "unknown"

* interpretation 0..*
* interpretation.coding 0..*
* interpretation.coding.system from NCIT (extensible)

* method 0..1
* method.coding 0..*
* method.coding.system from NCIT (extensible)
