def query_visit_occurrence():
    query = """
    PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
    PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
    PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>
    
    SELECT DISTINCT ?visit_occurrence_id ?person_id ?visit_concept_id ?visit_start_date ?visit_start_datetime ?visit_end_date ?visit_end_datetime ?visit_type_concept_id ?provider_id ?care_site_id ?visit_source_value ?visit_source_concept_id ?admitting_source_concept_id ?admitting_source_value ?discharge_to_concept_id ?discharge_to_source_value ?preceding_visit_occurrence_id
WHERE {
    ?p1 rdf:type omop:visit_occurrence_id.
    ?instance_owl ?p1 ?visit_occurrence_id.
?p2 rdf:type omop:visit_occurrence_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:visit_concept_id.
    ?instance_owl ?p3 ?visit_concept_id_1.
    ?visit_concept_id_1 owl:sameAs ?omop_p3.
    ?omop_p3 std:domain_id ?omop_domain_p3.
      FILTER(?omop_domain_p3="Visit" || ?omop_p3= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p3 std:standard_concept_id ?visit_concept_id_uri.
      ?visit_concept_id_uri std:concept_id ?visit_concept_id.
?p4 rdf:type omop:visit_start_date.
    ?instance_owl ?p4 ?visit_start_date.
OPTIONAL{?p5 rdf:type omop:visit_start_datetime.
    ?instance_owl ?p5 ?visit_start_datetime.}
?p6 rdf:type omop:visit_end_date.
    ?instance_owl ?p6 ?visit_end_date.
OPTIONAL{?p7 rdf:type omop:visit_end_datetime.
    ?instance_owl ?p7 ?visit_end_datetime.}
OPTIONAL{?p8 rdf:type omop:visit_type_concept_id.
    ?instance_owl ?p8 ?visit_type_concept_id_1.
    ?visit_type_concept_id_1 owl:sameAs ?omop_p8.
    ?omop_p8 std:domain_id ?omop_domain_p8.
      FILTER(?omop_domain_p8="Type Concept")
      ?omop_p8 std:standard_concept_id ?visit_type_concept_id_uri.
      ?visit_type_concept_id_uri std:concept_id ?visit_type_concept_id.}
OPTIONAL{?p9 rdf:type omop:visit_occurrence_provider_id.
    ?instance_owl ?p9 ?provider_id.}
OPTIONAL{?p10 rdf:type omop:visit_occurrence_care_site_id.
    ?instance_owl ?p10 ?care_site_id.}
?p11 rdf:type omop:visit_source_value.
    ?instance_owl ?p11 ?visit_source_value_uri.
?p11bis rdf:type omop:local_concept.
  ?visit_source_value_uri ?p11bis ?visit_source_value.
?p12 rdf:type omop:visit_source_concept_id.
    ?instance_owl ?p12 ?visit_source_value_uri.
OPTIONAL{?visit_source_value_uri owl:sameAs ?omop_p12.
    ?omop_p12 std:domain_id ?omop_domain_p12.
      FILTER(?omop_domain_p12="Visit" || ?omop_p12= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p12 std:concept_id ?visit_source_concept_id.}
OPTIONAL{?p13 rdf:type omop:visit_admitting_source_concept_id.
    ?instance_owl ?p13 ?admitting_source_concept_id_1.
    ?admitting_source_concept_id_1 owl:sameAs ?omop_p13.
    ?omop_p13 std:domain_id ?omop_domain_p13.
      FILTER(?omop_domain_p13="Visit" || ?omop_p13= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p13 std:standard_concept_id ?admitting_source_concept_id_uri.
      ?admitting_source_concept_id_uri std:concept_id ?admitting_source_concept_id.}
OPTIONAL{?p14 rdf:type omop:visit_admitting_source_value.
    ?instance_owl ?p14 ?admitting_source_value_1.
    ?admitting_source_value_1 owl:sameAs ?omop_p14.
    ?omop_p14 std:domain_id ?omop_domain_p14.
      FILTER(?omop_domain_p14="Visit" || ?omop_p14= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p14 std:concept_code ?admitting_source_value.}
OPTIONAL{?p15 rdf:type omop:visit_occurrence_discharge_to_concept_id.
    ?instance_owl ?p15 ?discharge_to_concept_id_1.
    ?discharge_to_concept_id_1 owl:sameAs ?omop_p15.
    ?omop_p15 std:domain_id ?omop_domain_p15.
      FILTER(?omop_domain_p15="Visit" || ?omop_p15= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p15 std:standard_concept_id ?discharge_to_concept_id_uri.
      ?discharge_to_concept_id_uri std:concept_id ?discharge_to_concept_id.}
OPTIONAL{?p16 rdf:type omop:visit_occurrence_discharge_to_source_value.
    ?instance_owl ?p16 ?discharge_to_source_value_1.
    ?discharge_to_source_value_1 owl:sameAs ?omop_p16.
    ?omop_p16 std:domain_id ?omop_domain_p16.
      FILTER(?omop_domain_p16="Visit" || ?omop_p16= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p16 std:concept_code ?discharge_to_source_value.}
OPTIONAL{?p17 rdf:type omop:preceding_visit_occurrence_id.
    ?instance_owl ?p17 ?preceding_visit_occurrence_id.}
}
    """
    return query
