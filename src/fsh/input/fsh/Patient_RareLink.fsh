Alias: SNOMEDCT = http://snomed.info/sct
Alias: ICD10 = https://icd.who.int/browse10/2019/en

Profile: RareLinkIPSPatient
Parent: Patient-uv-ips
Id: rarelink-ips-patient
Title: "RareLink IPS Patient"
Description: "A RareLink-specific profile for the IPS Patient resource."

* identifier 0..*
* identifier.use = #official
* identifier.type.coding.system = "http://snomed.info/sct"
* identifier.type.coding.code = #422549004
* identifier.value MS

* name 1..*
* name.text 0..1
* name.extension contains http://hl7.org/fhir/StructureDefinition/data-absent-reason named dataAbsentReason 0..1
* name.extension[dataAbsentReason].valueCode = #unknown

* gender 0..1

* birthDate 1..1

* deceased[x] 0..1 MS
* deceasedBoolean 0..1 MS
* deceasedDateTime 0..1 MS

* extension contains BirthPlace named birth_place 0..1
* extension contains DateOfAdmission named date_of_admission 0..1
* extension contains RecordedSexAtBirth named recorded_sex_at_birth 0..1
* extension contains CauseOfDeath named cause_of_death 0..1
* extension contains VitalStatus named vital_status 0..1 MS

* extension[BirthPlace]
Extension: BirthPlace
Id: birth-place
Title: "Birth Place"
Description: "The patient's place of birth."
* value[x] only CodeableConcept
* valueCodeableConcept.coding.system = "http://terminology.hl7.org/NamingSystem/v3-iso3166-1"
* valueCodeableConcept.coding.code MS

* extension[DateOfAdmission]
Extension: DateOfAdmission
Id: date-of-admission
Title: "Date of Admission"
Description: "The date of the patient's admission."
* value[x] only dateTime

* extension[RecordedSexAtBirth]
Extension: RecordedSexAtBirth
Id: recorded-sex-at-birth
Title: "Recorded Sex at Birth"
Description: "The sex assigned to the patient at birth."
* value[x] only CodeableConcept
* valueCodeableConcept.coding.system = "http://snomed.info/sct"
* valueCodeableConcept.coding.code from SexAtBirthVS (extensible)

* extension[CauseOfDeath]
Extension: CauseOfDeath
Id: cause-of-death
Title: "Cause of Death"
Description: "The cause of death for the patient."
* extension contains
    CauseOfDeathCode named causeOfDeath 1..1 and
    CauseOfDeathDefinition named codeDefinition 1..1

Extension: CauseOfDeathCode
Id: cause-of-death-code
Title: "Cause of Death Code"
Description: "The ICD-10 code representing the cause of death."
* value[x] only CodeableConcept
* valueCodeableConcept.coding.system = ICD10
* valueCodeableConcept.coding.code MS
* valueCodeableConcept.text MS

Extension: CauseOfDeathDefinition
Id: cause-of-death-definition
Title: "Cause of Death Definition"
Description: "The SNOMED CT definition of the cause of death concept."
* value[x] only CodeableConcept
* valueCodeableConcept.coding.system = SNOMEDCT
* valueCodeableConcept.coding.code = #184305005

Extension: VitalStatus
Id: vital-status
Title: "Vital Status"
Description: "Coded representation of a patient's vital status"
* value[x] only CodeableConcept
* valueCodeableConcept from VitalStatusVS (extensible)

ValueSet: SexAtBirthVS
Id: sex-at-birth-vs
Title: "Sex at Birth Value Set"
Description: "Value set for capturing the sex assigned at birth."
* SNOMEDCT#248152002 "Female"
* SNOMEDCT#248153007 "Male"
* SNOMEDCT#184115007 "Patient sex unknown"
* SNOMEDCT#32570691000036108 "Intersex"
* SNOMEDCT#1220561009 "Not recorded"

ValueSet: VitalStatusVS
Id: vital-status-vs
Title: "Vital Status Value Set"
Description: "Value set for capturing the vital status of the patient."
* SNOMEDCT#438949009 "Alive" // maps to false
* SNOMEDCT#419099009 "Dead" // maps to true
* SNOMEDCT#399307001 "Unknown - Lost in follow-up" // maps to null
* SNOMEDCT#185924006 "Unknown - Opted-out" // maps to null
* SNOMEDCT#261665006 "Unknown - Other Reason" // maps to null