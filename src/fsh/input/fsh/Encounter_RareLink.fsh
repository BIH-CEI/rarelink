Alias: SNOMEDCT = http://snomed.info/sct
Alias: HL7FHIR = http://hl7.org/fhir/R4

Profile: RareLinkEncounter
Parent: Encounter
Id: rarelink-encounter
Title: "RareLink Encounter"
Description: "A RareLink-specific Encounter profile based on the Encounter resource."

* status 1..1
* status from http://hl7.org/fhir/ValueSet/encounter-status (required)

* class 1..1
* class from EncounterClassVS (required)

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 0..1 MS
* subject.identifier 0..1 MS

* period 0..1
* period.start 0..1
* period.end 0..1


ValueSet: EncounterClassVS
Id: encounter-class-vs
Title: "Encounter Class Value Set"
Description: "Value set for encounter classes, including custom RareLink-specific codes."
* HL7FHIR#AMB "Ambulatory"
* HL7FHIR#IMP "Inpatient"
* HL7FHIR#OBSENC "Observation"
* HL7FHIR#EMER "Emergency"
* HL7FHIR#VR "Virtual"
* HL7FHIR#HH "Home Health"
* http://github.com/BIH-CEI/RareLink#RDC "RD Specialist Center"
* SNOMEDCT#261665006 "Unknown"
