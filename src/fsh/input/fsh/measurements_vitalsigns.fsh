Alias: LOINC = https://loinc.org/
Alias: HL7FHIR = http://hl7.org/fhir/R4/
Alias: NCIT = https://ncit.nci.nih.gov/

Profile: RareLinkIPSMeasurementsVitalSigns
Parent: Observation
Id: rarelink-observation-vital-signs
Title: "RareLink Vital Signs Measurements"
Description: "A RareLink-specific profile for vital signs measurements."

* meta.profile = "http://hl7.org/fhir/StructureDefinition/vitalsigns|4.0.1" (exactly)

* status 1..1
* status from http://hl7.org/fhir/ValueSet/observation-status (required)

* category 1..1
* category.coding 1..1
* category.coding.system = "http://terminology.hl7.org/CodeSystem/observation-category"
* category.coding.code = #vital-signs

* code 1..1
* code.coding from http://hl7.org/fhir/ValueSet/observation-vitalsignresult

* subject 1..1
* subject.reference = "Patient/{id}"

* effective[x] 1..1

* value[x] 0..1
* valueQuantity 0..1
* valueQuantity.value MS
* valueQuantity.unit MS

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink Vital Signs Measurements</strong></p>
  <p>This profile is based on the RareLink-CDM Section (6.3) Measurements for Vital Signs and the FHIR VitalSigns Observation profile.</p>
</div>
"""

* interpretation 0..*
* interpretation.coding 0..1
* interpretation.coding.system from NCIT (required)
* interpretation.coding.code MS

* method 0..1
* method.coding 0..*
* method.coding.system from LOINC (extensible)
* method.coding.code MS
