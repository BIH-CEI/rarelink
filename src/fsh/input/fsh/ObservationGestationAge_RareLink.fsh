Profile: RareLinkGestationAtBirth
Parent: Observation
Id: rarelink-observation-gestation-at-birth
Title: "RareLink Observation Gestation at Birth"
Description: "A RareLink-specific profile for capturing gestation length at birth."

* meta.profile ^slicing.discriminator.type = #pattern
* meta.profile ^slicing.discriminator.path = "$this"
* meta.profile ^slicing.rules = #open
* meta.profile contains baseProfile 1..1
* meta.profile[baseProfile] = "http://hl7.org/fhir/StructureDefinition/Observation|4.0.1"

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code.coding.system = SNOMEDCT
* code.coding.code = #412726003

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS


* effective[x] 0..1
* effectiveDateTime MS


// guide for slicing: https://fshschool.org/docs/sushi/tips/
// Define slicing for Observation.component
// * component ^slicing.discriminator.type = #value
// * component ^slicing.discriminator.path = "code.coding"
// * component ^slicing.rules = #open

// // Slice: Length of Gestation in Weeks
// * component[length_of_gestation_in_weeks] 1..1
// * component[length_of_gestation_in_weeks].code.coding 1..1
// * component[length_of_gestation_in_weeks].code.coding.system = SNOMEDCT
// * component[length_of_gestation_in_weeks].code.coding.code = #412726003
// * component[length_of_gestation_in_weeks].value[x] only Quantity
// * component[length_of_gestation_in_weeks].valueQuantity.system = "http://www.ontobee.org/ontology/UO"
// * component[length_of_gestation_in_weeks].valueQuantity.code = "UO:0000034"
// * component[length_of_gestation_in_weeks].valueQuantity.unit = "week"

// // Slice: Length of Gestation in Days
// * component[length_of_gestation_in_days] 1..1
// * component[length_of_gestation_in_days].code.coding 1..1
// * component[length_of_gestation_in_days].code.coding.system = SNOMEDCT
// * component[length_of_gestation_in_days].code.coding.code = #412726003
// * component[length_of_gestation_in_days].value[x] only Quantity
// * component[length_of_gestation_in_days].valueQuantity.system = "http://www.ontobee.org/ontology/UO"
// * component[length_of_gestation_in_days].valueQuantity.code = "UO:0000033"
// * component[length_of_gestation_in_days].valueQuantity.unit = "day"


