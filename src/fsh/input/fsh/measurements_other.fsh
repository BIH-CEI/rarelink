Alias: HL7FHIR = http://hl7.org/fhir/R4/
Alias: NCIT = https://ncit.nci.nih.gov/
Alias: UO = http://www.ontobee.org/ontology/UO
Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkIPSMeasurementsOthers
Parent: Observation
Id: rarelink-observation-measurements-others
Title: "RareLink Observation Measurements (Others)"
Description: "A RareLink-specific profile for measurements that do not fall under IPS laboratory, radiology, procedures, or vital signs."

* meta.profile = "http://hl7.org/fhir/StructureDefinition/Observation|4.0.1" (exactly)

* status 1..1
* status MS

* category 1..1
* category.coding 1..1
* category.coding.system from HL7FHIR
* category.coding.code MS
* category.coding.version = "R4"

* code 1..1
* code.coding 1..1
* code.coding.system from NCIT
* code.coding.code = #C60819
* code.coding.version = "24.04e"

* subject 1..1
* subject.reference = "Patient/{id}"

* effective[x] 0..1
* effectiveDateTime MS

* value[x] 0..1
* valueQuantity.system from UO
* valueQuantity.code MS
* valueQuantity.value MS

* interpretation 0..*
* interpretation.coding 0..*
* interpretation.coding.system from NCIT (extensible)

* method 0..1
* method.coding 0..*
* method.coding.system from SNOMEDCT (extensible)

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Measurements (Others)</strong></p>
  <p>This profile captures measurements not categorized as laboratory, radiology, procedures, or vital signs, within the RareLink-CDM framework.</p>
</div>
"""
