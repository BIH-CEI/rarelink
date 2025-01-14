Alias: SNOMEDCT = http://snomed.info/sct
Alias: HL7FHIR = http://hl7.org/fhir/R4/

Profile: RareLinkIPSPatient
Parent: Patient-uv-ips
Id: rarelink-ips-patient
Title: "RareLink IPS Patient"
Description: "A RareLink-specific profile for the IPS Patient resource."

* meta.profile = "http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips|2.0.0-ballot" (exactly)

* identifier 0..*
* identifier.use = #official
* identifier.type.coding.system from SNOMEDCT
* identifier.type.coding.code = #422549004
* identifier.type.coding.display = "Patient-related Identification code (observable entity)"
* identifier.value MS

* name 1..*
* name.text = "anonymous"

* gender 0..1
* gender from GenderIdentityVS (required)

* birthDate 1..1

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Patient</strong></p>
  <p>This profile is based on the RareLink-CDM Section (1) Formal Criteria and 
  (2) Personal Information, integrated with the IPS Patient profile.</p>
</div>
"""

* extension contains BirthPlace named birthplace 0..1
* extension contains DateOfAdmission named date_of_admission 0..1
* extension contains RecordedSexAtBirth named recorded_sex_at_birth 0..1

* extension[BirthPlace]
Extension: BirthPlace
Id: birthplace
Title: "Birth Place"
Description: "The patient's place of birth."
* value[x] only CodeableConcept
* valueCodeableConcept.coding.system from HL7FHIR (extensible)
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
* valueCodeableConcept.coding.system from SNOMEDCT
* valueCodeableConcept.coding.code from SexAtBirthVS (extensible)

ValueSet: GenderIdentityVS
Id: gender-identity-vs
Title: "Gender Identity Value Set"
Description: "Value set for gender identity."
* SNOMEDCT#446141000124107 "Female gender identity"
* SNOMEDCT#446151000124109 "Male gender identity"
* SNOMEDCT#394743007 "Gender unknown"
* SNOMEDCT#33791000087105 "Identifies as nonbinary gender"
* SNOMEDCT#1220561009 "Not recorded"

ValueSet: SexAtBirthVS
Id: sex-at-birth-vs
Title: "Sex at Birth Value Set"
Description: "Value set for capturing the sex assigned at birth."
* SNOMEDCT#248152002 "Female"
* SNOMEDCT#248153007 "Male"
* SNOMEDCT#184115007 "Patient sex unknown"
* SNOMEDCT#32570691000036108 "Intersex"
* SNOMEDCT#1220561009 "Not recorded"
