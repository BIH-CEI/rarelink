Alias: SNOMEDCT = http://snomed.info/sct
Alias: ORPHANET = http://www.orpha.net/
Alias: HL7FHIR = http://hl7.org/fhir/R4/
Alias: LOINC = https://loinc.org/
Alias: UO = http://www.ontobee.org/ontology/UO
Alias: NCIT = https://ncit.nci.nih.gov/

Profile: RareLinkIPSMeasurementRadiology
Parent: Observation-results-radiology-uv-ips
Id: rarelink-ips-measurement-radiology
Title: "RareLink IPS Measurement Radiology"
Description: "A RareLink-specific profile for radiology measurements based on the IPS Observation profile."

* meta.profile = "http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-radiology-uv-ips|2.0.0-ballot" (exactly)
* status 1..1
* status from http://hl7.org/fhir/ValueSet/observation-status (required)

* category 1..1
* category.coding 1..1
* category.coding.system from http://terminology.hl7.org/CodeSystem/observation-category (required)
* category.coding.code = #imaging

* code 1..1
* code.coding 1..1
* code.coding.system from LOINC (required)
* code.coding.code MS

* subject 1..1
* subject.reference = "Patient/{id}"

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

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Measurement Radiology</strong></p>
  <p>This profile is based on the RareLink-CDM Section (6.3) Measurements and the IPS Observation profile, specifically for radiology measurements.</p>
</div>
"""
