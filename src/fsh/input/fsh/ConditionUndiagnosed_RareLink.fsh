Alias: SNOMEDCT = http://snomed.info/sct
Alias: ORPHANET = http://www.orpha.net/ORDO

Profile: RareLinkConditionUndiagnosedRDCase
Parent: Condition-uv-ips
Id: rarelink-condition-undiagnosed-rd-case
Title: "RareLink Condition for Undiagnosed RD Case"
Description: "A RareLink-specific Condition profile for documenting undiagnosed rare disease cases based on the IPS Condition profile."

* code 1..1
* code.coding 1..1
* code.coding.code from UndiagnosedRDCaseVS (required)

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 1..1 MS
* subject.identifier 0..1 MS

* recordedDate 0..1

ValueSet: UndiagnosedRDCaseVS
Id: undiagnosed-rd-case-vs
Title: "Undiagnosed Rare Disease Case Value Set"
Description: "Value set for capturing undiagnosed rare disease cases."
* ORPHANET#616874 "Rare disorder without a determined diagnosis after full investigation"
* SNOMEDCT#373067005 "A Rare Disease was diagnosed"
