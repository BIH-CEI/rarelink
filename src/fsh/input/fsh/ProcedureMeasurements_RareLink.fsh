Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkIPSProcedure
Parent: Procedure-uv-ips
Id: rarelink-ips-procedure
Title: "RareLink IPS Procedure"
Description: "A RareLink-specific profile for the IPS Procedure resource."

* code 1..1
* code.coding 1..1
* code.coding.system from http://hl7.org/fhir/uv/ips/ValueSet/procedures-uv-ips (required)
* code.coding.code MS

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 1..1 MS
* subject.identifier 0..1 MS

* bodySite 0..*
* bodySite.coding 0..*
* bodySite.coding.system = "http://snomed.info/sct"
* bodySite.coding.code MS

* status 1..1
* status from http://hl7.org/fhir/ValueSet/event-status (required)
