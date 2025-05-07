Profile: RareLinkIPSMeasurementsVitalSigns
Parent: Observation
Id: rarelink-observation-vital-signs
Title: "RareLink Vital Signs Measurements"
Description: "A RareLink-specific profile for vital signs measurements."

* status 1..1

* category 1..1
* category.coding 1..1
* category.coding.system 1..1
* category.coding.code 1..1
* category.coding.system = "http://terminology.hl7.org/CodeSystem/observation-category"
* category.coding.code = #vital-signs

* code 1..1
* code.coding from http://hl7.org/fhir/ValueSet/observation-vitalsignresult

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* effective[x] 1..1

* value[x] 0..1
* valueQuantity 0..1
* valueQuantity.value MS
* valueQuantity.unit MS

* interpretation 0..*
* interpretation.coding 0..1
* interpretation.coding.system = "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"
* interpretation.coding.code MS

* method 0..1
* method.coding 0..*
* method.coding.system = "http://loinc.org"
* method.coding.code MS
