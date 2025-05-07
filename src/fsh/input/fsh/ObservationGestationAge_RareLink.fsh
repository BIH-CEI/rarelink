Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkGestationAtBirth
Parent: Observation
Id: rarelink-observation-gestation-at-birth
Title: "RareLink Observation Gestation at Birth"
Description: "A RareLink-specific profile for capturing gestation length at birth."

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code = SNOMEDCT#412726003

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* effective[x] 0..1
* effectiveDateTime MS

// Define slicing for Observation.component
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open
* component contains
    length_of_gestation_in_weeks 0..1 and
    length_of_gestation_in_days 0..1

// Slice: Length of Gestation in Weeks
* component[length_of_gestation_in_weeks].code.coding 1..1
* component[length_of_gestation_in_weeks].code.coding.system = "http://snomed.info/sct"
* component[length_of_gestation_in_weeks].code.coding.code = #412726003
* component[length_of_gestation_in_weeks].code.coding.display = "Length of gestation at birth"
* component[length_of_gestation_in_weeks].value[x] only Quantity
* component[length_of_gestation_in_weeks].valueQuantity.system = "http://www.ontobee.org/ontology/UO"
* component[length_of_gestation_in_weeks].valueQuantity.code = #0000034
* component[length_of_gestation_in_weeks].valueQuantity.unit = "week"

// Slice: Length of Gestation in Days
* component[length_of_gestation_in_days].code.coding 1..1
* component[length_of_gestation_in_days].code.coding.system = "http://snomed.info/sct"
* component[length_of_gestation_in_days].code.coding.code = #412726003
* component[length_of_gestation_in_days].code.coding.display = "Length of gestation at birth"
* component[length_of_gestation_in_days].value[x] only Quantity
* component[length_of_gestation_in_days].valueQuantity.system = "http://www.ontobee.org/ontology/UO"
* component[length_of_gestation_in_days].valueQuantity.code = #0000033
* component[length_of_gestation_in_days].valueQuantity.unit = "day"