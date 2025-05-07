Alias: SNOMEDCT = http://snomed.info/sct
Alias: UO = http://www.ontobee.org/ontology/UO

Profile: RareLinkIPSMeasurementLaboratory
Parent: Observation-results-radiology-uv-ips
Id: rarelink-ips-measurement-laboratory
Title: "RareLink IPS Measurement Laboratory"
Description: "A RareLink-specific profile for laboratory measurements based on the IPS Observation profile."

* status 1..1

* category 1..1
* category.coding 1..1
* category.coding.code = #laboratory

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 1..1 MS
* subject.identifier 0..1 MS

* effective[x] 1..1

* value[x] 0..1

* performer 1..*
* performer MS
* performer ^extension[0].url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* performer ^extension[0].valueCode = #unknown

* interpretation 0..*
* interpretation.coding 0..*
* interpretation.coding.system = "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"

* method 0..1
* method.coding 0..*
* method.coding.system = "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"