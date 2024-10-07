from src.data_model.value_set import ValueSet, ValueSetChoice
from src.data_model.base_types import CodeSystem, Coding
from src.data_model.codesystems import CodeSystems

SNOMED = CodeSystems.SNOMED
HL7FHIR = CodeSystems.HL7FHIR
LOINC = CodeSystems.LOINC
GA4GH = CodeSystems.GA4GH
CustomCode = CodeSystems.CustomCode
HP = CodeSystems.HP

class VALUE_SETS_VERSIONS_V2_0_0_dev0:
    """Value set definitions for version 2_0_0_dev0."""
    
    value_sets = [
        ValueSet(
            valueSetName="Sex at Birth Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Sex at Birth",
            valueSetCode=Coding(system=SNOMED, code="281053000"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Female",
                    choiceCode=Coding(system=SNOMED, code="248152002"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Male",
                    choiceCode=Coding(system=SNOMED, code="248153007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Patient sex unknown",
                    choiceCode=Coding(system=SNOMED, code="184115007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Intersex",
                    choiceCode=Coding(system=SNOMED, code="32570691000036108"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Karyotypic Sex Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Karyotypic Sex",
            valueSetCode=Coding(system=SNOMED, code="1296886006"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="XX",
                    choiceCode=Coding(system=SNOMED, code="734875008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XY",
                    choiceCode=Coding(system=SNOMED, code="734876009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="X0",
                    choiceCode=Coding(system=SNOMED, code="80427008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXY",
                    choiceCode=Coding(system=SNOMED, code="65162001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXX",
                    choiceCode=Coding(system=SNOMED, code="35111009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXYY",
                    choiceCode=Coding(system=SNOMED, code="403760006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXXY",
                    choiceCode=Coding(system=SNOMED, code="78317008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXXX",
                    choiceCode=Coding(system=SNOMED, code="10567003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XYY",
                    choiceCode=Coding(system=SNOMED, code="48930007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Other",
                    choiceCode=Coding(system=SNOMED, code="74964007"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Gender Identity Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Gender Identity",
            valueSetCode=Coding(system=SNOMED, code="263495000"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Female gender identity",
                    choiceCode=Coding(system=SNOMED, code="446141000124107"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Male gender identity",
                    choiceCode=Coding(system=SNOMED, code="446151000124109"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Gender unknown",
                    choiceCode=Coding(system=SNOMED, code="394743007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Identifies as nonbinary gender",
                    choiceCode=Coding(system=SNOMED, code="33791000087105"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Vital Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Vital Status",
            valueSetCode=Coding(system=SNOMED, code="278844005"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Alive",
                    choiceCode=Coding(system=SNOMED, code="438949009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Lost in follow-up",
                    choiceCode=Coding(system=SNOMED, code="399307001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Opted-out",
                    choiceCode=Coding(system=SNOMED, code="185924006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Other Reason",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Age Category Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Age Category",
            valueSetCode=Coding(system=SNOMED, code="105727008"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Infancy",
                    choiceCode=Coding(system=SNOMED, code="3658006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Toddler",
                    choiceCode=Coding(system=SNOMED, code="713153009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Childhood",
                    choiceCode=Coding(system=SNOMED, code="255398004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adolescence",
                    choiceCode=Coding(system=SNOMED, code="263659003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adulthood",
                    choiceCode=Coding(system=SNOMED, code="41847000"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Fetal period",
                    choiceCode=Coding(system=SNOMED, code="303112003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Vital Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Vital Status",
            valueSetCode=Coding(system=SNOMED, code="278844005"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Alive",
                    choiceCode=Coding(system=SNOMED, code="438949009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Lost in follow-up",
                    choiceCode=Coding(system=SNOMED, code="399307001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Opted-out",
                    choiceCode=Coding(system=SNOMED, code="185924006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Other Reason",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Age Category Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Age Category",
            valueSetCode=Coding(system=SNOMED, code="105727008"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Infancy",
                    choiceCode=Coding(system=SNOMED, code="3658006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Toddler",
                    choiceCode=Coding(system=SNOMED, code="713153009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Childhood",
                    choiceCode=Coding(system=SNOMED, code="255398004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adolescence",
                    choiceCode=Coding(system=SNOMED, code="263659003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adulthood",
                    choiceCode=Coding(system=SNOMED, code="41847000"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Fetal period",
                    choiceCode=Coding(system=SNOMED, code="303112003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Undiagnosed RD Case Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Undiagnosed RD Case",
            valueSetCode=Coding(system=SNOMED, code="723663001"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        # 4. Care Pathway
        ValueSet(
            valueSetName="Encounter Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Encounter Status",
            valueSetCode=Coding(system=SNOMED, code="305058001"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Planned", 
                    choiceCode=Coding(system=HL7FHIR, code="planned"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Arrived", 
                    choiceCode=Coding(system=HL7FHIR, code="arrived"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Triaged", 
                    choiceCode=Coding(system=HL7FHIR, code="triaged"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="In Progress", 
                    choiceCode=Coding(system=HL7FHIR, code="in-progress"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="On Leave", 
                    choiceCode=Coding(system=HL7FHIR, code="onleave"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Finished", 
                    choiceCode=Coding(system=HL7FHIR, code="finished"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Cancelled", 
                    choiceCode=Coding(system=HL7FHIR, code="cancelled"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Entered in Error", 
                    choiceCode=Coding(system=HL7FHIR, code="entered-in-error"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown", 
                    choiceCode=Coding(system=HL7FHIR, code="unknown"), 
                    choiceCodeSystem=HL7FHIR
                )
            ]
        ),
        ValueSet(
            valueSetName="Encounter Class Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Encounter Class",
            valueSetCode=Coding(system=HL7FHIR, code="encounter.class"),
            valueSetCodeSystem=[HL7FHIR, SNOMED],
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Ambulatory", 
                    choiceCode=Coding(system=HL7FHIR, code="AMB"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Inpatient", 
                    choiceCode=Coding(system=HL7FHIR, code="IMP"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Observation", 
                    choiceCode=Coding(system=HL7FHIR, code="OBSENC"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Emergency", 
                    choiceCode=Coding(system=HL7FHIR, code="EMER"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Virtual", 
                    choiceCode=Coding(system=HL7FHIR, code="VR"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Home Health", 
                    choiceCode=Coding(system=HL7FHIR, code="HH"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="RD Specialist Center", 
                    choiceCode=Coding(system=HL7FHIR, code="RDC"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown", 
                    choiceCode=Coding(system=SNOMED, code="261665006"), 
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Verification Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Verification Status",
            valueSetCode=Coding(system=LOINC, code="99498-8"),
            valueSetCodeSystem=HL7FHIR,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Unconfirmed",
                    choiceCode=Coding(system=HL7FHIR, code="unconfirmed"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Provisional",
                    choiceCode=Coding(system=HL7FHIR, code="provisional"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Differential",
                    choiceCode=Coding(system=HL7FHIR, code="differential"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Confirmed",
                    choiceCode=Coding(system=HL7FHIR, code="confirmed"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Refuted",
                    choiceCode=Coding(system=HL7FHIR, code="refuted"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Entered in Error",
                    choiceCode=Coding(system=HL7FHIR, code="entered-in-error"),
                    choiceCodeSystem=HL7FHIR
                )
            ]
        ),
        ValueSet(
            valueSetName="Age at Onset Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Age at Onset",
            valueSetCode=Coding(system=SNOMED, code="424850005"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Prenatal",
                    choiceCode=Coding(system=SNOMED, code="118189007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Birth",
                    choiceCode=Coding(system=SNOMED, code="3950001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Date",
                    choiceCode=Coding(system=SNOMED, code="410672004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Age at Diagnosis Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Age at Diagnosis",
            valueSetCode=Coding(system=SNOMED, code="423493009"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Prenatal",
                    choiceCode=Coding(system=SNOMED, code="118189007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Birth",
                    choiceCode=Coding(system=SNOMED, code="3950001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Date",
                    choiceCode=Coding(system=SNOMED, code="410672004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Body Site Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Body Site",
            valueSetCode=Coding(system=SNOMED, code="363698007"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="<< 442083009 |Anatomical or acquired body structure|",
                    choiceCode=Coding(system=SNOMED, code="<< 442083009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Clinical Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Clinical Status",
            valueSetCode=Coding(system=SNOMED, code="263493007"),
            valueSetCodeSystem=HL7FHIR,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Active",
                    choiceCode=Coding(system=HL7FHIR, code="active"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Recurrence",
                    choiceCode=Coding(system=HL7FHIR, code="recurrence"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Relapse",
                    choiceCode=Coding(system=HL7FHIR, code="relapse"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Inactive",
                    choiceCode=Coding(system=HL7FHIR, code="inactive"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Remission",
                    choiceCode=Coding(system=HL7FHIR, code="remission"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Resolved",
                    choiceCode=Coding(system=HL7FHIR, code="resolved"),
                    choiceCodeSystem=HL7FHIR
                )
            ]
        ),
        ValueSet(
            valueSetName="Severity Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Severity",
            valueSetCode=Coding(system=SNOMED, code="246112005"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Severe",
                    choiceCode=Coding(system=SNOMED, code="24484000"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Moderate",
                    choiceCode=Coding(system=SNOMED, code="6736007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Mild",
                    choiceCode=Coding(system=SNOMED, code="255604002"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        # 6.1 Genetic Findings
        ValueSet(
            valueSetName="Progress Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Progress Status",
            valueSetCode=Coding(system=GA4GH, code="progress_status"),
            valueSetCodeSystem=GA4GH,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="No information is available about"
                                    "the diagnosis",
                    choiceCode=Coding(system=GA4GH, code="UNKNOWN_PROGRESS"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="No diagnosis has been found to date but"
                                " additional differential diagnostic"
                                " work is in progress.",
                    choiceCode=Coding(system=GA4GH, code="IN_PROGRESS"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The work on the interpretation is complete.",
                    choiceCode=Coding(system=GA4GH, code="COMPLETED"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The interpretation is complete and also"
                                " considered to be a definitive diagnosis.",
                    choiceCode=Coding(system=GA4GH, code="SOLVED"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The interpretation is complete but no "
                                "definitive diagnosiswas found.",
                    choiceCode=Coding(system=GA4GH, code="UNSOLVED"),
                    choiceCodeSystem=GA4GH
                )
            ]
        ),
        ValueSet(
            valueSetName="Interpretation Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Interpretation Status",
            valueSetCode=Coding(system=GA4GH, code="interpretation_status"),
            valueSetCodeSystem=GA4GH,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="No information is available about the status",
                    choiceCode=Coding(system=GA4GH, code="UNKNOWN_STATUS"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The variant or gene reported here is  "
                                "interpreted not to be related to the diagnosis.",
                    choiceCode=Coding(system=GA4GH, code="REJECTED"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The variant or gene reported here is "
                                "interpreted to possibly be related to the "
                                "diagnosis.",
                    choiceCode=Coding(system=GA4GH, code="CANDIDATE"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The variant or gene reported here is  "
                                "interpreted to be related to the diagnosis.",
                    choiceCode=Coding(system=GA4GH, code="CONTRIBUTORY"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="The variant or gene reported here is  "
                                "interpreted to be causative of the diagnosis.",
                    choiceCode=Coding(system=GA4GH, code="CAUSATIVE"),
                    choiceCodeSystem=GA4GH
                )
            ]
        ),
        ValueSet(
            valueSetName="Structural Variant Analysis Method Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Structural Variant Analysis Method",
            valueSetCode=Coding(system=LOINC, code="81304-8"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Karyotyping",
                    choiceCode=Coding(system=LOINC, code="LA26406-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="FISH",
                    choiceCode=Coding(system=LOINC, code="LA26404-6"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="PCR",
                    choiceCode=Coding(system=LOINC, code="LA26418-6"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="qPCR (real-time PCR)",
                    choiceCode=Coding(system=LOINC, code="LA26419-4"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="SNP array",
                    choiceCode=Coding(system=LOINC, code="LA26400-4"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Restriction fragment length polymorphism (RFLP)",
                    choiceCode=Coding(system=LOINC, code="LA26813-8"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="DNA hybridization",
                    choiceCode=Coding(system=LOINC, code="LA26810-4"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Sequencing",
                    choiceCode=Coding(system=LOINC, code="LA26398-0"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="MLPA",
                    choiceCode=Coding(system=LOINC, code="LA26415-2"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Other",
                    choiceCode=Coding(system=LOINC, code="LA46-8"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),
        ValueSet(
            valueSetName="Reference Genome Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Reference Genome",
            valueSetCode=Coding(system=LOINC, code="62374-4"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="NCBI Build 34 (hg16)",
                    choiceCode=Coding(system=LOINC, code="LA14032-9"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="GRCh37 (hg19)",
                    choiceCode=Coding(system=LOINC, code="LA14029-5"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="NCBI Build 36.1 (hg18)",
                    choiceCode=Coding(system=LOINC, code="LA14030-3"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="NCBI Build 35 (hg17)",
                    choiceCode=Coding(system=LOINC, code="LA14031-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="GRCh38 (hg38)",
                    choiceCode=Coding(system=LOINC, code="LA26806-2"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),
        ValueSet(
            valueSetName="Zygosity Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Zygosity",
            valueSetCode=Coding(system=LOINC, code="53034-5"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Homozygous",
                    choiceCode=Coding(system=LOINC, code="LA6705-3"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="(Simple) Heterozygous",
                    choiceCode=Coding(system=LOINC, code="LA6706-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Compound Heterozygous",
                    choiceCode=Coding(system=LOINC, code="LA26217-2"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Double Heterozygous",
                    choiceCode=Coding(system=LOINC, code="LA26220-6"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Hemizygous",
                    choiceCode=Coding(system=LOINC, code="LA6707-9"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Heteroplasmic",
                    choiceCode=Coding(system=LOINC, code="LA6703-8"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Homoplasmic",
                    choiceCode=Coding(system=LOINC, code="LA6704-6"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Other",
                    choiceCode=Coding(system=LOINC, code="LA46-8"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),
        ValueSet(
            valueSetName="Genomic Source Class Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Genomic Source Class",
            valueSetCode=Coding(system=LOINC, code="48002-0"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Germline",
                    choiceCode=Coding(system=LOINC, code="LA6683-2"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Somatic",
                    choiceCode=Coding(system=LOINC, code="LA6684-0"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Fetal",
                    choiceCode=Coding(system=LOINC, code="LA10429-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Likely Germline",
                    choiceCode=Coding(system=LOINC, code="LA18194-3"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Likely Somatic",
                    choiceCode=Coding(system=LOINC, code="LA18195-0"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Likely Fetal",
                    choiceCode=Coding(system=LOINC, code="LA18196-8"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown Genomic Origin",
                    choiceCode=Coding(system=LOINC, code="LA18197-6"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="De Novo",
                    choiceCode=Coding(system=LOINC, code="LA26807-0"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),
        ValueSet(
            valueSetName="DNA Change Type Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="DNA Change Type",
            valueSetCode=Coding(system=LOINC, code="48019-4"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Wild Type",
                    choiceCode=Coding(system=LOINC, code="LA9658-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Deletion",
                    choiceCode=Coding(system=LOINC, code="LA6692-3"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Duplication",
                    choiceCode=Coding(system=LOINC, code="LA6686-5"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Insertion",
                    choiceCode=Coding(system=LOINC, code="LA6687-3"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Insertion/Deletion",
                    choiceCode=Coding(system=LOINC, code="LA6688-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Inversion",
                    choiceCode=Coding(system=LOINC, code="LA6689-9"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Substitution",
                    choiceCode=Coding(system=LOINC, code="LA6690-7"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),
        ValueSet(
            valueSetName="Clinical Significance ACMG Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Clinical Significance [ACMG]",
            valueSetCode=Coding(system=LOINC, code="53037-8"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA6668-3"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Likely Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA26332-9"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Uncertain Significance",
                    choiceCode=Coding(system=LOINC, code="LA26333-7"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Likely Benign",
                    choiceCode=Coding(system=LOINC, code="LA26334-5"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Benign",
                    choiceCode=Coding(system=LOINC, code="LA6675-8"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=LOINC, code="LA4489-6"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),
        ValueSet(
            valueSetName="Therapeutic Actionability Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Therapeutic Actionability",
            valueSetCode=Coding(system=GA4GH, code="therapeutic_actionability"),
            valueSetCodeSystem=GA4GH,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="There is not enough information at this time"
                                  " to support any therapeutic actionability"
                                  " for this variant.",
                    choiceCode=Coding(system=GA4GH, code="UNKNOWN_ACTIONABILITY"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="This variant has no therapeutic actionability.",
                    choiceCode=Coding(system=GA4GH, code="NOT_ACTIONABLE"),
                    choiceCodeSystem=GA4GH
                ),
                ValueSetChoice(
                    choiceDisplay="This variant is known to be therapeutically"
                                    "actionalbe.",
                    choiceCode=Coding(system=GA4GH, code="ACTIONABLE"),
                    choiceCodeSystem=GA4GH
                )
            ]
        ),
        ValueSet(
            valueSetName="Clinical Annotation Level Of Evidence Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Clinical Annotation Level Of Evidence",
            valueSetCode=Coding(system=LOINC, code="93044-6"),
            valueSetCodeSystem=LOINC,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Very Strong Evidence Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA30200-2"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Strong Evidence Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA30201-0"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Moderate Evidence Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA30202-8"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Supporting Evidence Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA30203-6"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Supporting Evidence Benign",
                    choiceCode=Coding(system=LOINC, code="LA30204-4"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Strong Evidence Benign",
                    choiceCode=Coding(system=LOINC, code="LA30205-1"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Stand-alone Evidence Pathogenic",
                    choiceCode=Coding(system=LOINC, code="LA30206-9"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Stand-alone Evidence Benign",
                    choiceCode=Coding(system=LOINC, code="LA30207-7"),
                    choiceCodeSystem=LOINC
                ),
                ValueSetChoice(
                    choiceDisplay="Uncertain Significance",
                    choiceCode=Coding(system=LOINC, code="LA26333-7"),
                    choiceCodeSystem=LOINC
                )
            ]
        ),

        # 6.2 Phenotypic Findings
        ValueSet(
            valueSetName="Phenotype Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Phenotypic Findings Status",
            valueSetCode=Coding(system=GA4GH, code="phenotypicfeature.excluded"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Confirmed Present",
                    choiceCode=Coding(system=SNOMED, code="410605003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Refuted",
                    choiceCode=Coding(system=SNOMED, code="723511001"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Onset Category Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Onset Category",
            valueSetCode=Coding(system=HP, code="0003674"),
            valueSetCodeSystem=HP,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Embryonal onset (0w-8w embryonal)",
                    choiceCode=Coding(system=HP, code="0011460"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Fetal onset (8w embryonal - birth)",
                    choiceCode=Coding(system=HP, code="0011461"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Congenital onset (at birth)",
                    choiceCode=Coding(system=HP, code="0003577"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Neonatal onset (0d-28d)",
                    choiceCode=Coding(system=HP, code="0003623"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Infantile onset (28d-1y)",
                    choiceCode=Coding(system=HP, code="0003593"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Childhood onset (1y-5y)",
                    choiceCode=Coding(system=HP, code="0011463"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Juvenile onset (5y-15y)",
                    choiceCode=Coding(system=HP, code="0003621"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Young adult onset (16y-40y)",
                    choiceCode=Coding(system=HP, code="0011462"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Middle age adult onset (40y-60y)",
                    choiceCode=Coding(system=HP, code="0003596"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Late adult onset (60y+)",
                    choiceCode=Coding(system=HP, code="0003584"),
                    choiceCodeSystem=HP
                )
            ]
        ),
        ValueSet(
            valueSetName="Temporal Pattern Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Temporal Pattern",
            valueSetCode=Coding(system=HP, code="0011008"),
            valueSetCodeSystem=HP,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Acute",
                    choiceCode=Coding(system=HP, code="0011009"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Chronic",
                    choiceCode=Coding(system=HP, code="0011010"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Fluctuating",
                    choiceCode=Coding(system=HP, code="0031914"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Prolonged",
                    choiceCode=Coding(system=HP, code="0025297"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Recurrent",
                    choiceCode=Coding(system=HP, code="0031796"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Stable",
                    choiceCode=Coding(system=HP, code="0031915"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Subacute",
                    choiceCode=Coding(system=HP, code="0011011"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Transient",
                    choiceCode=Coding(system=HP, code="0025153"),
                    choiceCodeSystem=HP
                )
            ]
        ),
        ValueSet(
            valueSetName="Severity Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/"
                         "rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Severity",
            valueSetCode=Coding(system=HP, code="0012824"),
            valueSetCodeSystem=HP,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Borderline",
                    choiceCode=Coding(system=HP, code="0012827"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Mild",
                    choiceCode=Coding(system=HP, code="0012825"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Moderate",
                    choiceCode=Coding(system=HP, code="0012826"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Profound",
                    choiceCode=Coding(system=HP, code="0012829"),
                    choiceCodeSystem=HP
                ),
                ValueSetChoice(
                    choiceDisplay="Severe",
                    choiceCode=Coding(system=HP, code="0012828"),
                    choiceCodeSystem=HP
                )
            ]
        ),

        # 6.3 Measurements

        # 6.4 Family History
        ValueSet(
            valueSetName="Propositus Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Propositus/-a",
            valueSetCode=Coding(system=SNOMED, code="64245008"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Family Relationship To Index Case Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Relationship to Propositus",
            valueSetCode=Coding(system=SNOMED, code="408732007"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Natural mother",
                    choiceCode=Coding(system=SNOMED, code="65656005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural father",
                    choiceCode=Coding(system=SNOMED, code="9947008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural daughter",
                    choiceCode=Coding(system=SNOMED, code="83420006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural son",
                    choiceCode=Coding(system=SNOMED, code="113160008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural brother",
                    choiceCode=Coding(system=SNOMED, code="60614009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural sister",
                    choiceCode=Coding(system=SNOMED, code="73678001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Twin sibling",
                    choiceCode=Coding(system=SNOMED, code="11286003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Half-brother",
                    choiceCode=Coding(system=SNOMED, code="45929001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Half-sister",
                    choiceCode=Coding(system=SNOMED, code="2272004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural grandfather",
                    choiceCode=Coding(system=SNOMED, code="62296006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural grandmother",
                    choiceCode=Coding(system=SNOMED, code="17945006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Consanguinity Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Consanguinity",
            valueSetCode=Coding(system=SNOMED, code="842009"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="FamilyMember Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Family Member Relationship",
            valueSetCode=Coding(system=SNOMED, code="444018008"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Natural mother",
                    choiceCode=Coding(system=SNOMED, code="65656005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural father",
                    choiceCode=Coding(system=SNOMED, code="9947008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural daughter",
                    choiceCode=Coding(system=SNOMED, code="83420006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural son",
                    choiceCode=Coding(system=SNOMED, code="113160008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural brother",
                    choiceCode=Coding(system=SNOMED, code="60614009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural sister",
                    choiceCode=Coding(system=SNOMED, code="73678001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Twin sibling",
                    choiceCode=Coding(system=SNOMED, code="11286003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Half-brother",
                    choiceCode=Coding(system=SNOMED, code="45929001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Half-sister",
                    choiceCode=Coding(system=SNOMED, code="2272004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural grandfather",
                    choiceCode=Coding(system=SNOMED, code="62296006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Natural grandmother",
                    choiceCode=Coding(system=SNOMED, code="17945006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="FamilyHistoryStatus Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Family Member Record Status",
            valueSetCode=Coding(system=HL7FHIR, code="familymemberhistory.status"),
            valueSetCodeSystem=HL7FHIR,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Partial",
                    choiceCode=Coding(system=HL7FHIR, code="partial"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Completed",
                    choiceCode=Coding(system=HL7FHIR, code="completed"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Entered in Error",
                    choiceCode=Coding(system=HL7FHIR, code="entered-in-error"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Health Unknown",
                    choiceCode=Coding(system=HL7FHIR, code="health-unknown"),
                    choiceCodeSystem=HL7FHIR
                )
            ]
        ),
        ValueSet(
            valueSetName="AdministrativeGender Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Family Member Sex",
            valueSetCode=Coding(system=LOINC, code="54123-5"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Female",
                    choiceCode=Coding(system=SNOMED, code="248152002"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Male",
                    choiceCode=Coding(system=SNOMED, code="248153007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Patient sex unknown",
                    choiceCode=Coding(system=SNOMED, code="184115007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Intersex",
                    choiceCode=Coding(system=SNOMED, code="32570691000036108"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Deceased Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Family Member Deceased",
            valueSetCode=Coding(system=SNOMED, code="740604001"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Consent Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Consent Status",
            valueSetCode=Coding(system=SNOMED, code="309370004"),
            valueSetCodeSystem=HL7FHIR,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Pending",
                    choiceCode=Coding(system=HL7FHIR, code="draft"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Proposed",
                    choiceCode=Coding(system=HL7FHIR, code="proposed"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Active",
                    choiceCode=Coding(system=HL7FHIR, code="active"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Rejected",
                    choiceCode=Coding(system=HL7FHIR, code="rejected"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Inactive",
                    choiceCode=Coding(system=HL7FHIR, code="inactive"),
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Entered in Error",
                    choiceCode=Coding(system=HL7FHIR, code="entered-in-error"),
                    choiceCodeSystem=HL7FHIR
                )
            ]
        ),
        ValueSet(
            valueSetName="Contact for Research Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/"
                         "rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Agreement to be Contacted for Research",
            valueSetCode=Coding(system=CustomCode, code="consent_contact_research"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Data Reuse Consent Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/"
                         "rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Consent to the Reuse of Data",
            valueSetCode=Coding(system=CustomCode, code="conset_data_reuse"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Biological Sample Consent Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/BIH-CEI/rd-cdm/blob/develop/res/v2_0_0_dev0/"
                         "rd_cdm_value_sets_v2_0_0_dev0.json",
            display="Biological Sample",
            valueSetCode=Coding(system=SNOMED, code="123038009"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),


        





    ]
    