Profile: IPSCondition
Parent: https://build.fhir.org/ig/HL7/fhir-ips/StructureDefinition-Condition-uv-ips.html
Id: ips.condition
Title: "IPS Condition"
Description: "RareLink IPS Condition profile based on the IPS 2.0.0-ballot specification."

* meta.profile[0] = "http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.0-ballot"
* clinicalStatus 1..1
* clinicalStatus.coding 1..1
* clinicalStatus.coding[0].system = "http://terminology.hl7.org/CodeSystem/condition-clinical" (required)
* verificationStatus 1..1
* verificationStatus.coding 1..1
* verificationStatus.coding[0].system = "http://terminology.hl7.org/CodeSystem/condition-ver-status" (required)
* subject 1..1
* severity 0..1
* severity.coding 0..1
* severity.coding[0].system = "http://snomed.info/sct" (preferred)
* severity.coding[0].code from #5_9_severity.csv (preferred)
* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Condition</strong></p>
  <p>This profile is based on the RareLink CDM Section 5 - Disease and the IPS v2.0.0.ballot profile. It defines conditions with standardized clinical, verification, and severity information.</p>
</div>
"""
