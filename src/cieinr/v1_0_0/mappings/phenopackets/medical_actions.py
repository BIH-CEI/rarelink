# Treatment keys (https://phenopacket-schema.readthedocs.io/en/latest/treatment.html#rsttreatment)
# agent
# route_of_administration
# dose_intervals
# drug_type
# cumulative_dose

# MedicalActions keys (https://phenopacket-schema.readthedocs.io/en/latest/medical-action.html):
# action
# treatment_target
# treatment_intent
# response_to_treatment
# adverse_events
# treatment_termination_reason

BASIC_PROCEDURE_BLOCK = {
    "procedure_field_1": "basic_form.igrt_basic",
    "procedure_field_2": "basic_form.hct_basic_form",
    "performed": None
}

# Inactivated vaccine mapping
INACTIVATE_VACCINE_BLOCK = {
    "redcap_repeat_instrument": "inactivated_vaccine_history_and_specific_immune_re",
    "agent_field_1": "inactiv_vax",
    "agent_field_2": "inactiv_vax_other",
    "cumulative_dose": "inactiv_vax_dose",
    "adverse_event_field": "inactiv_vax_ae",
    "completion_of_inact_vax": "completion_inactiv_vax",
    "adverse_event_other_field": "inactiv_vax_ae_other",
    "adverse_event_severity": "inactiv_vax_ae_severity",
    "response_field_1": "vo_0000424_before_pneu",
    "response_field_2": "inactiv_vax_response",
    "previous_pneumococcal_vaccine": "vo_0000424_before_pneu",
    "enum_classes": {
        "vo_": "cieinr.v1_0_0.python_schemas.form_6_inactivated_vaccines.InactivatedVaccineTypeEnum"
    }
}
# Live vaccine mapping
LIVE_VACCINE_BLOCK = {
    "redcap_repeat_instrument": "live_vaccine_and_specific_immune_response",
    "agent_field_1": "live_vax",
    "agent_field_2": "live_vax_other",
    "cumulative_dose": "live_vax_dosages",
    "dose_interval_start_date": "completion_live_vax",
    "adverse_event_field": "live_vax_ae",
    "adverse_event_other_field": "live_vax_ae_other",
    "adverse_event_severity": "live_vax_ae_severity",
    "response_field_1": "live_vax_response",
    "response_field_2": "measles_response",
    "response_field_3": "mumps_response",
    "response_field_4": "rubella_response",
    "enum_classes": {
        "vo_": "cieinr.v1_0_0.python_schemas.form_7_live_vaccines.LiveVaccineTypeEnum"
    }
}