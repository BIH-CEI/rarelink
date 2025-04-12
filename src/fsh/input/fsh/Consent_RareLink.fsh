Alias: SNOMEDCT = http://snomed.info/sct

Profile: RareLinkConsent
Parent: Consent
Id: rarelink-consent
Title: "RareLink Consent"
Description: "A RareLink-specific Consent profile based on the Consent resource."

* meta.profile ^slicing.discriminator.type = #pattern
* meta.profile ^slicing.discriminator.path = "$this"
* meta.profile ^slicing.rules = #open
* meta.profile contains baseProfile 1..1
* meta.profile[baseProfile] = "http://hl7.org/fhir/StructureDefinition/Consent|4.0.1"

* status 1..1
* status from http://hl7.org/fhir/ValueSet/consent-status (required)

* scope 1..1
* scope.coding from http://terminology.hl7.org/CodeSystem/consentscope (required)
* scope.coding.code = #research

* category 1..1
* category.coding from http://terminology.hl7.org/CodeSystem/consentcategorycodes (required)
* category.coding.code = #research

* patient 1..1
* patient only Reference(RareLinkIPSPatient)
* patient.reference 0..1 MS
* patient.identifier 0..1 MS

* dateTime 0..1
* policy 1..1

* extension contains ConsentToReuseData named consent_to_reuse_data 0..1
* extension contains AgreementToBeContacted named agreement_to_be_contacted 0..1

* extension[ConsentToReuseData]
Extension: ConsentToReuseData
Id: consent-to-reuse-data
Title: "Consent to Reuse Data"
Description: "ERDRI-CDS - Consent to the reuse of data."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://snomed.info/sct"
* valueCodeableConcept.coding.code from ConsentToReuseVS (extensible)

* extension[AgreementToBeContacted]
Extension: AgreementToBeContacted
Id: agreement-to-be-contacted
Title: "Agreement to Be Contacted"
Description: "ERDRI-CDS - Agreement to be contacted for research purposes."
* value[x] only CodeableConcept
* valueCodeableConcept.coding 1..1
* valueCodeableConcept.coding.system = "http://snomed.info/sct"
* valueCodeableConcept.coding.code from AgreementToBeContactedVS (extensible)

ValueSet: ConsentToReuseVS
Id: consent-to-reuse-vs
Title: "Consent to Reuse Data Value Set"
Description: "Value set for capturing consent to reuse data."
* SNOMEDCT#373066001 "Yes"
* SNOMEDCT#373067005 "No"
* SNOMEDCT#261665006 "Unknown"

ValueSet: AgreementToBeContactedVS
Id: agreement-to-be-contacted-vs
Title: "Agreement to Be Contacted Value Set"
Description: "Value set for capturing agreement to be contacted for research."
* SNOMEDCT#373066001 "Yes"
* SNOMEDCT#373067005 "No"
* SNOMEDCT#261665006 "Unknown"
