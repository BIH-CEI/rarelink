def query_condition_occurrence():
    query = """
    PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
    PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
    PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>
    
    SELECT DISTINCT ?condition_occurrence_id ?person_id ?condition_concept_id ?condition_start_date ?condition_start_datetime ?condition_end_date ?condition_end_datetime ?condition_type_concept_id ?condition_status_concept_id ?stop_reason ?provider_id ?visit_occurrence_id ?visit_detail_id ?condition_source_value ?condition_source_concept_id ?condition_status_source_value
WHERE {
?p1 rdf:type omop:condition_occurrence_id.
    ?instance_owl ?p1 ?condition_occurrence_id.
?p2 rdf:type omop:condition_occurrence_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:condition_occurrence_concept_id.
    ?instance_owl ?p3 ?condition_concept_id_1.
    ?condition_concept_id_1 owl:sameAs ?omop_p3.
    ?omop_p3 std:domain_id ?omop_domain_p3.
      FILTER(?omop_domain_p3="Condition"|| ?omop_p3 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p3 std:standard_concept_id ?condition_concept_id_uri.
      ?condition_concept_id_uri std:concept_id ?condition_concept_id.
?p4 rdf:type omop:condition_start_date.
    ?instance_owl ?p4 ?condition_start_date.
OPTIONAL{?p5 rdf:type omop:condition_start_datetime.
    ?instance_owl ?p5 ?condition_start_datetime.}
OPTIONAL{?p6 rdf:type omop:condition_end_date.
    ?instance_owl ?p6 ?condition_end_date.}
OPTIONAL{?p7 rdf:type omop:condition_end_datetime.
    ?instance_owl ?p7 ?condition_end_datetime.}
OPTIONAL{?p8 rdf:type omop:condition_type_concept_id.}
OPTIONAL{?instance_owl ?p8 ?condition_type_concept_id_1.
    ?condition_type_concept_id_1 owl:sameAs ?omop_p8.
    ?omop_p8 std:domain_id ?omop_domain_p8.
      FILTER(?omop_domain_p8="Type Concept")
      ?omop_p8 std:standard_concept_id ?condition_type_concept_id_uri.
      ?condition_type_concept_id_uri std:concept_id ?condition_type_concept_id.}
OPTIONAL{?p9 rdf:type omop:condition_status_concept_id.}
OPTIONAL{?instance_owl ?p9 ?condition_status_concept_id_1.
    ?condition_status_concept_id_1 owl:sameAs ?omop_p9.
    ?omop_p9 std:domain_id ?omop_domain_p9.
      FILTER(?omop_domain_p9="Condition Status" || ?omop_p9 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p9 std:standard_concept_id ?condition_status_concept_id_uri.
      ?condition_status_concept_id_uri std:concept_id ?condition_status_concept_id.}
OPTIONAL{?p10 rdf:type omop:condition_occurrence_stop_reason.
    ?instance_owl ?p10 ?stop_reason.}
OPTIONAL{?p11 rdf:type omop:condition_occurrence_provider_id.
    ?instance_owl ?p11 ?provider_id.}
OPTIONAL{?p12 rdf:type omop:condition_occurrence_visit_occurrence_id.
    ?instance_owl ?p12 ?visit_occurrence_id.}
OPTIONAL{?p13 rdf:type omop:condition_occurrence_visit_detail_id.
    ?instance_owl ?p13 ?visit_detail_id.}
?p14 rdf:type omop:condition_source_value.
    ?instance_owl ?p14 ?condition_source_value_uri.
?p14bis rdf:type omop:local_concept.
  ?condition_source_value_uri ?p14bis ?condition_source_value.
OPTIONAL{?p15 rdf:type omop:condition_source_concept_id.
    ?instance_owl ?p15 ?condition_source_value_uri.
    ?condition_source_value_uri owl:sameAs ?omop_p15.
    ?omop_p15 std:domain_id ?omop_domain_p15.
      FILTER(?omop_domain_p15="Condition" || ?omop_p15 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p15 std:concept_id ?condition_source_concept_id.}
OPTIONAL{?p16 rdf:type omop:condition_status_source_value.}
OPTIONAL{?instance_owl ?p16 ?condition_status_source_value_1.
    ?condition_status_source_value_1 owl:sameAs ?omop_p16.
    ?omop_p16 std:domain_id ?omop_domain_p16.
      FILTER(?omop_domain_p16="Condition Status")
      ?omop_p16 std:concept_code ?condition_status_source_value.}
}
    """
    return query
