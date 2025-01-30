Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkKaryotypicSex
Parent: Observation
Id: rarelink-karyotypic-sex
Title: "RareLink Observation Karyotypic Sex"
Description: "A RareLink-specific profile for capturing karyotypic sex information."

* meta.profile = "http://hl7.org/fhir/StructureDefinition/Observation|4.0.1" (exactly)

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code.coding.system = SNOMEDCT
* code.coding.code = #1296886006
* code.coding.display = "Karyotypic Sex"

* subject 1..1
* subject.reference = "Patient/{id}"

* value[x] only CodeableConcept
* valueCodeableConcept 1..1
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = SNOMEDCT
* valueCodeableConcept.coding.code from KaryotypicSexVS (required)

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink Karyotypic Sex</strong></p>
  <p>This profile is based on the RareLink-CDM Section (2.3) Personal Information and the Observation resource.</p>
</div>
"""

ValueSet: KaryotypicSexVS
Id: karyotypic-sex-vs
Title: "Karyotypic Sex Value Set"
Description: "Value set for capturing karyotypic sex."
* SNOMEDCT#261665006 "Unknown"
* SNOMEDCT#734875008 "XX"
* SNOMEDCT#734876009 "XY"
* SNOMEDCT#80427008 "X0"
* SNOMEDCT#65162001 "XXY"
* SNOMEDCT#35111009 "XXX"
* SNOMEDCT#403760006 "XXYY"
* SNOMEDCT#78317008 "XXXY"
* SNOMEDCT#10567003 "XXXX"
* SNOMEDCT#48930007 "XYY"
* SNOMEDCT#74964007 "Other"
