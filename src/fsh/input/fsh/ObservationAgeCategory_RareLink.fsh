Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkAgeCategory
Parent: Observation
Id: rarelink-observation-age-category
Title: "RareLink Observation Age Category"
Description: "A RareLink-specific profile for capturing the age category of
 a patient as an observation, based on the ERDRI-CDS value set."

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code = SNOMEDCT#105727008

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* effective[x] 1..1
* effectiveDateTime MS

* value[x] 1..1
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://snomed.info/sct"
* valueCodeableConcept.coding.code from AgeCategoryVS (required)

ValueSet: AgeCategoryVS
Id: age-category-vs
Title: "Age Category Value Set"
Description: "Value set for capturing the age category of a patient."
* SNOMEDCT#3658006 "Infancy"
* SNOMEDCT#713153009 "Toddler"
* SNOMEDCT#255398004 "Childhood"
* SNOMEDCT#263659003 "Adolescence"
* SNOMEDCT#41847000 "Adulthood"
* SNOMEDCT#303112003 "Fetal period"
* SNOMEDCT#419099009 "Dead"
* SNOMEDCT#261665006 "Unknown"
