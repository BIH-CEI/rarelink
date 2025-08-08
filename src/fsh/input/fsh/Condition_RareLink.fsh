Alias: SNOMEDCT = http://snomed.info/sct
Profile: RareLinkIPSCondition
Parent: Condition-uv-ips
Id: rarelink-ips-condition
Title: "RareLink IPS Condition"
Description: "A RareLink-specific Condition profile based on the IPS Condition profile."

* code 1..1

* clinicalStatus 1..1
* clinicalStatus from http://terminology.hl7.org/ValueSet/condition-clinical

* verificationStatus 1..1
* verificationStatus from http://terminology.hl7.org/ValueSet/condition-ver-status

* severity 0..1
* severity.coding 0..1
* severity.coding.system = "http://snomed.info/sct"
* severity.coding.code from SeverityVS (extensible)

* bodySite 0..* MS
* bodySite.coding 0..1
* bodySite.coding.system = "http://snomed.info/sct"
* bodySite.coding.code MS

* subject 1..1
* subject only Reference(RareLinkIPSPatient)
* subject.reference 1..1 MS
* subject.identifier 0..1 MS

* onsetDateTime 0..1

* recordedDate 0..1

* extension contains AgeAtDiagnosis named age_at_diagnosis 0..1
* extension contains AgeAtOnset named age_at_onset 0..1

Extension: AgeAtDiagnosis
Id: age-at-diagnosis
Title: "Age at Diagnosis"
Description: "ERDRI-CDS - The age at which the condition was diagnosed."
* value[x] only CodeableConcept
* valueCodeableConcept from AgeAtDiagnosisVS (extensible)

Extension: AgeAtOnset
Id: age-at-onset
Title: "Age at Onset"
Description: "ERDRI-CDS - The age at which the condition first appeared."
* value[x] only CodeableConcept
* valueCodeableConcept from AgeAtOnsetVS (extensible)


ValueSet: SeverityVS
Id: severity-vs
Title: "Severity Value Set"
Description: "Value set for severity levels of conditions."
* SNOMEDCT#24484000 "Severe"
* SNOMEDCT#6736007 "Moderate"
* SNOMEDCT#255604002 "Mild"

ValueSet: AgeAtDiagnosisVS
Id: age-at-diagnosis-vs
Title: "Age at Diagnosis Value Set"
Description: "Value set for capturing age at diagnosis."
* SNOMEDCT#118189007 "Prenatal"
* SNOMEDCT#3950001 "Birth"
* SNOMEDCT#410672004 "Date"
* SNOMEDCT#261665006 "Unknown"

ValueSet: AgeAtOnsetVS
Id: age-at-onset-vs
Title: "Age at Onset Value Set"
Description: "Value set for capturing age at onset."
* SNOMEDCT#118189007 "Prenatal"
* SNOMEDCT#3950001 "Birth"
* SNOMEDCT#410672004 "Date"
* SNOMEDCT#261665006 "Unknown"
