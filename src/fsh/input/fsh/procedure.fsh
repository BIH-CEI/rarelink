Alias: SNOMEDCT = http://snomed.info/sct
Alias: HL7FHIR = http://hl7.org/fhir/R4/

Profile: RareLinkIPSProcedure
Parent: Procedure-uv-ips
Id: rarelink-ips-procedure
Title: "RareLink IPS Procedure"
Description: "A RareLink-specific profile for the IPS Procedure resource."

* meta.profile = "http://hl7.org/fhir/uv/ips/StructureDefinition/Procedure-uv-ips|2.0.0-ballot" (exactly)

* code 1..1
* code.coding 1..1
* code.coding.system from http://hl7.org/fhir/uv/ips/ValueSet/procedures-uv-ips (required)
* code.coding.code MS

* subject 1..1
* subject.reference = "Patient/{id}"

* performed[x] 1..1
* performedDateTime MS

* bodySite 0..*
* bodySite.coding 0..*
* bodySite.coding.system from SNOMEDCT (required)
* bodySite.coding.code MS

* status 1..1
* status from http://hl7.org/fhir/ValueSet/event-status (required)

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Procedure</strong></p>
  <p>This profile is based on the RareLink-CDM Section (6.3) Measurements, integrated with the IPS Procedure profile.</p>
</div>
"""
