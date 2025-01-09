Profile: RareLinkIPSCondition
Parent: Condition
Id: rarelink-ips-condition
Title: "RareLink IPS Condition"
Description: "A RareLink-specific Condition profile based on the IPS Condition profile."
* meta.profile[0] =  "http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.0-ballot"
* clinicalStatus 1..1
* clinicalStatus.coding 1..1
* clinicalStatus.coding[0].system from http://terminology.hl7.org/CodeSystem/condition-clinical
* verificationStatus 1..1
* verificationStatus.coding 1..1
* verificationStatus.coding[0].system = "http://terminology.hl7.org/CodeSystem/condition-ver-status"
* severity 0..1
* severity.coding 0..1
* severity.coding[0].system = "http://snomed.info/sct"
* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Condition</strong></p>
  <p>This profile is based on the RareLink-CDM Section (5) Disease and the IPS profile.</p>
</div>
"""
