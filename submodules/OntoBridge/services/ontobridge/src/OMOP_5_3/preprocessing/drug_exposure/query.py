def query_drug_exposure():
    query = """
        PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
        PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
        PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>
        
        SELECT DISTINCT ?drug_exposure_id ?person_id ?drug_concept_id ?drug_exposure_start_date ?drug_exposure_start_datetime ?drug_exposure_end_date ?drug_exposure_end_datetime ?verbatim_end_date ?drug_type_concept_id ?stop_reason ?refills ?quantity ?days_supply ?sig ?route_concept_id ?lot_number ?provider_id ?visit_occurrence_id ?visit_detail_id ?drug_source_value ?drug_source_concept_id ?route_source_value ?dose_unit_source_value

WHERE {
?p1 rdf:type omop:drug_exposure_id.
    ?instance_owl ?p1 ?drug_exposure_id.
?p2 rdf:type omop:drug_exposure_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:drug_exposure_drug_concept_id.
    ?instance_owl ?p3 ?drug_concept_id_1.
    ?drug_concept_id_1 owl:sameAs ?omop_p3.
    ?omop_p3 std:domain_id ?omop_domain_p3.
      FILTER(?omop_domain_p3 = "Drug" || ?omop_p3 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p3 std:standard_concept_id ?drug_concept_id_uri.
      ?drug_concept_id_uri std:concept_id ?drug_concept_id.
?p4 rdf:type omop:drug_exposure_start_date.
    ?instance_owl ?p4 ?drug_exposure_start_date.
OPTIONAL{?p5 rdf:type omop:drug_exposure_start_datetime.
    ?instance_owl ?p5 ?drug_exposure_start_datetime.}
OPTIONAL{?p6 rdf:type omop:drug_exposure_end_date.
    ?instance_owl ?p6 ?drug_exposure_end_date.}
OPTIONAL{?p7 rdf:type omop:drug_exposure_end_datetime.
    ?instance_owl ?p7 ?drug_exposure_end_datetime.}
OPTIONAL{?p8 rdf:type omop:verbatim_end_date.
    ?instance_owl ?p8 ?verbatim_end_date.}
OPTIONAL{?p9 rdf:type omop:drug_type_concept_id.}
OPTIONAL{?instance_owl ?p9 ?drug_type_concept_id_1.
    ?drug_type_concept_id_1 owl:sameAs ?omop_p9.
    ?omop_p9 std:domain_id ?omop_domain_p9.
      FILTER(?omop_domain_p9="Type Concept")
      ?omop_p9 std:standard_concept_id ?drug_type_concept_id_uri.
      ?drug_type_concept_id_uri std:concept_id ?drug_type_concept_id.}
OPTIONAL{?p10 rdf:type omop:drug_exposure_stop_reason.
    ?instance_owl ?p10 ?stop_reason.}
OPTIONAL{?p11 rdf:type omop:refills.
    ?instance_owl ?p11 ?refills.}
OPTIONAL{?p12 rdf:type omop:drug_exposure_quantity.
    ?instance_owl ?p12 ?quantity.}
OPTIONAL{?p13 rdf:type omop:days_supply.
    ?instance_owl ?p13 ?days_supply.}
OPTIONAL{?p14 rdf:type omop:sig.
    ?instance_owl ?p14 ?sig.}
OPTIONAL{?p15 rdf:type omop:route_concept_id.}
OPTIONAL{?instance_owl ?p15 ?route_concept_id_1.}
OPTIONAL{?route_concept_id_1 owl:sameAs ?omop_p15.
    ?omop_p15 std:domain_id ?omop_domain_p15.
      FILTER(?omop_domain_p15="Route")
      ?omop_p15 std:standard_concept_id ?route_concept_id_uri.
      ?route_concept_id_uri std:concept_id ?route_concept_id.}
OPTIONAL{?p16 rdf:type omop:lot_number.
    ?instance_owl ?p16 ?lot_number.}
OPTIONAL{?p17 rdf:type omop:drug_exposure_provider_id.
    ?instance_owl ?p17 ?provider_id.}
OPTIONAL{?p18 rdf:type omop:drug_exposure_visit_occurrence_id.
    ?instance_owl ?p18 ?visit_occurrence_id.}
OPTIONAL{?p19 rdf:type omop:drug_exposure_visit_detail_id.
    ?instance_owl ?p19 ?visit_detail_id.}
?p20 rdf:type omop:drug_source_value.
    ?instance_owl ?p20 ?drug_source_value_uri.
?p20bis rdf:type omop:local_concept.
?drug_source_value_uri ?p20bis ?drug_source_value.
  OPTIONAL{?drug_source_value_uri owl:sameAs ?omop_p20.
    ?omop_p20 std:domain_id ?omop_domain_p20.
      FILTER(?omop_domain_p20 = "Drug" || ?omop_p20 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p20 std:concept_code ?drug_source_value_std.}
OPTIONAL{?p21 rdf:type omop:drug_source_concept_id.
    ?instance_owl ?p21 ?drug_source_value_uri.
    ?drug_source_value_uri owl:sameAs ?omop_p21.
    ?omop_p21 std:domain_id ?omop_domain_p21.
      FILTER(?omop_domain_p21 = "Drug" || ?omop_p21 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p21 std:concept_id ?drug_source_concept_id.}
OPTIONAL{?p22 rdf:type omop:route_source_value.
?instance_owl ?p22 ?route_source_value_uri.
?route_source_value_uri ?p20bis ?route_source_value.}
OPTIONAL{?p23 rdf:type omop:dose_unit_source_value.
    ?instance_owl ?p23 ?dose_unit_source_value_uri.
    ?dose_unit_source_value_uri ?p20bis ?dose_unit_source_value.}
}
        """
    return query
