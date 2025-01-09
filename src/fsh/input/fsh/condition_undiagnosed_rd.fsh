Alias: SNOMEDCT = http://snomed.info/sct
Alias: ORPHANET = http://www.orpha.net/

Profile: RareLinkConditionUndiagnosedRDCase
Parent: Condition-uv-ips
Id: rarelink-condition-undiagnosed-rd-case
Title: "RareLink Condition for Undiagnosed RD Case"
Description: "A RareLink-specific Condition profile for documenting undiagnosed rare disease cases based on the IPS Condition profile."

* meta.profile = "http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.0-ballot" (exactly)
* code 1..1
* code.coding 1..1
* code.coding.system from ORPHANET (required)
* code.coding.code from UndiagnosedRDCaseVS (required)

* subject 1..1
* subject.reference = "Patient/{id}"

* recordedDate 0..1

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink Condition</strong></p>
  <p>This profile is based on the RareLink-CDM Section (3) Patient Status and the IPS Condition profile, specifically for undiagnosed rare disease cases.</p>
</div>
"""

ValueSet: UndiagnosedRDCaseVS
Id: undiagnosed-rd-case-vs
Title: "Undiagnosed Rare Disease Case Value Set"
Description: "Value set for capturing undiagnosed rare disease cases."
* SNOMEDCT#373066001 "Rare disorder without a determined diagnosis after full investigation"
* SNOMEDCT#373067005 "A Rare Disease was diagnosed"
