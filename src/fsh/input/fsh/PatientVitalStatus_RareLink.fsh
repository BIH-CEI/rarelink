Alias: SNOMEDCT = http://snomed.info/sct
Alias: HL7FHIR = http://hl7.org/fhir/R4/

Profile: RareLinkIPSPatientVitalStatus
Parent: Patient-uv-ips
Id: rarelink-ips-patient-vital-status
Title: "RareLink IPS Patient Vital Status"
Description: "A RareLink-specific profile for the IPS Patient resource with vital status extensions."

* meta.profile = "http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips|2.0.0-ballot" (exactly)

* identifier 0..*
* identifier.value MS

* name 1..*
* name.text = "anonymous"

* birthDate 1..1

* deceased[x] 0..1

* text.div = """
<div xmlns="http://www.w3.org/1999/xhtml">
  <p><strong>RareLink IPS Patient Vital Status</strong></p>
  <p>This profile is based on the RareLink-CDM Section (3) Patient Status, integrated with the IPS Patient profile.</p>
</div>
"""

* extension contains CauseOfDeath named cause_of_death 0..1
* extension contains PatientStatusDate named patient_status_date 0..1

* extension[CauseOfDeath]
Extension: CauseOfDeath
Id: cause-of-death
Title: "Cause of Death"
Description: "The cause of death for the patient."
* value[x] only CodeableConcept
* valueCodeableConcept.coding.system from SNOMEDCT
* valueCodeableConcept.coding.code MS

* extension[PatientStatusDate]
Extension: PatientStatusDate
Id: patient-status-date
Title: "Patient Status Date"
Description: "The date of completion for the RareLink-CDM Patient Status sheet."
* value[x] only dateTime

ValueSet: VitalStatusVS
Id: vital-status-vs
Title: "Vital Status Value Set"
Description: "Value set for capturing the vital status of the patient."
* SNOMEDCT#438949009 "Not Deceased" // false
* SNOMEDCT#419099009 "Deceased" // true 
* SNOMEDCT#399307001 "Unknown - Lost in follow-up" // null
* SNOMEDCT#185924006 "Unknown - Opted-out" // null 
* SNOMEDCT#261665006 "Unknown - Other Reason" // null
