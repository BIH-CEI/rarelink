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

INACTIVATE_VACCINE_BLOCK = {
    "agent_field_1": "inactivated_vaccine_history_and_specific_immune_re.inactiv_vax",
    "agent_field_2": "inactivated_vaccine_history_and_specific_immune_re.inactiv_vax_other",
    "cumulative_dose": "inactiv_vax_dose",
    # add further CIEINR keys to mapping blocks for export to Phenopackets
    #   - inactiv_vax_ae
    #   - inactiv_vax_ae_other
    #   - inactiv_vax_ae_severity
    #   - vo_0000424_before_pneu
    #   - inactiv_vax_response
    #   - inactiv_vax_response_date
}

LIVE_VACCINE_BLOCK = {
    "agent_field_1": "live_vaccine_and_specific_immune_response.live_vax",
    "agent_field_2": "live_vaccine_and_specific_immune_response.live_vax_other",
    "cumulative_dose": "live_vax_dosages",
    # add further CIEINR keys to mapping blocks for export to Phenopackets
    #   - live_vax_ae
    #   - ae_live_vax
    #   - live_vax_ae_other
    #   - live_vax_ae_severity
    #   - live_vax_response
    #   - life_vax_response_date
    #   - measles_response
    #   - mumps_response
    #   - rubella_response
}


