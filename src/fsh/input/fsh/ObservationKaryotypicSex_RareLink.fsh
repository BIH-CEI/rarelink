Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkKaryotypicSex
Parent: Observation
Id: rarelink-karyotypic-sex
Title: "RareLink Observation Karyotypic Sex"
Description: "A RareLink-specific profile for capturing karyotypic sex information."

* status 1..1
* status = #final

* code 1..1
* code.coding 1..1
* code = SNOMEDCT#1296886006

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* value[x] only CodeableConcept
* valueCodeableConcept 1..1
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = SNOMEDCT
* valueCodeableConcept.coding.code from KaryotypicSexVS (required)

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
