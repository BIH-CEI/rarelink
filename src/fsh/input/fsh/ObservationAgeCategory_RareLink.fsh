Alias: SNOMEDCT = http://snomed.info/sct
Alias: HL7FHIR = http://hl7.org/fhir/R4/

Profile: RareLinkAgeCategory
Parent: Observation
Id: rarelink-observation-age-category
Title: "RareLink Observation Age Category"
Description: "A RareLink-specific profile for capturing the age category of
 a patient as an observation, based on the ERDRI-CDS value set."

* meta.profile = "http://hl7.org/fhir/StructureDefinition/Observation|4.0.1" (exactly)

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code.coding.system = "https://www.snomed.org/snomed-ct"
* code.coding.code = #105727008
* code.coding.display = "Age Category"

* subject 1..1
* subject.type = Patient
* subject.identifier = Patient.id

* effective[x] 1..1
* effectiveDateTime MS

* value[x] 1..1
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "https://www.snomed.org/snomed-ct"
* valueCodeableConcept.coding.code from AgeCategoryVS (required)

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink Observation Age Category</strong></p>
  <p>This profile is based on the RareLink-CDM Section (3) Patient Status, 
  capturing the age category as an observation, based on the ERDRI-CDS value set</p>
</div>

"""

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
