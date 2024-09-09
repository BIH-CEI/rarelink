def query_observation_concept():
    query = """
PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>

SELECT DISTINCT ?observation_id ?person_id ?observation_concept_id ?observation_date ?observation_datetime ?observation_type_concept_id ?value_as_number ?value_as_string ?value_as_concept_id ?qualifier_concept_id ?unit_concept_id ?provider_id ?visit_occurrence_id ?visit_detail_id ?observation_source_value ?observation_source_concept_id ?unit_source_value ?qualifier_source_value
WHERE {
    ?p1 rdf:type omop:observation_id.
    ?instance_owl ?p1 ?observation_id.
?p2 rdf:type omop:observation_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:observation_concept_id.
    ?instance_owl ?p3 ?observation_concept_id_1.
    ?observation_concept_id_1 owl:sameAs ?omop_p3.
      FILTER(?omop_domain_p3="Observation" || ?omop_p3 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
    ?omop_p3 std:standard_concept_id ?observation_concept_id_uri.
    ?observation_concept_id_uri std:concept_id ?observation_concept_id.
OPTIONAL{?p4 rdf:type omop:observation_date.
    ?instance_owl ?p4 ?observation_date.}
OPTIONAL{?p5 rdf:type omop:observation_datetime.
    ?instance_owl ?p5 ?observation_datetime.}
OPTIONAL{?p6 rdf:type omop:observation_type_concept_id.}
OPTIONAL{?instance_owl ?p6 ?observation_type_concept_id_1.
    ?observation_type_concept_id_1 owl:sameAs ?omop_p6.
    ?omop_p6 std:domain_id ?omop_domain_p6.
      FILTER(?omop_domain_p6="Type Concept")
      ?omop_p6 std:standard_concept_id ?observation_type_concept_id_uri.
      ?observation_type_concept_id_uri std:concept_id ?observation_type_concept_id.}
?p9 rdf:type omop:value_as_concept_id.
    ?instance_owl ?p9 ?value_as_concept_id_1.
    ?value_as_concept_id_1 owl:sameAs ?omop_p9.
    ?omop_p9 std:domain_id ?omop_domain_p9.
      FILTER(?omop_domain_p9="Condition" || ?omop_domain_p9="Observation" || ?omop_p9= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p9 std:standard_concept_id ?value_as_concept_id_uri.
      ?value_as_concept_id_uri std:concept_id ?value_as_concept_id.
OPTIONAL{?p10 rdf:type omop:qualifier_concept_id.
    ?instance_owl ?p10 ?qualifier_concept_id_1.
    ?qualifier_concept_id_1 owl:sameAs ?omop_p10.
    ?omop_p10 std:standard_concept_id ?qualifier_concept_id_uri.
    ?qualifier_concept_id_uri std:concept_id ?qualifier_concept_id.}
OPTIONAL{?p11 rdf:type omop:observation_unit_concept_id.
    ?instance_owl ?p11 ?unit_concept_id_1.
    ?unit_concept_id_1 owl:sameAs ?omop_p11.
    ?omop_p11 std:domain_id ?omop_domain_p11.
      FILTER(?omop_domain_p11="Unit")
      ?omop_p11 std:standard_concept_id ?unit_concept_id_uri.
      ?unit_concept_id_uri std:concept_id ?unit_concept_id.}
OPTIONAL{?p12 rdf:type omop:observation_provider_id.
    ?instance_owl ?p12 ?provider_id.}
OPTIONAL{?p13 rdf:type omop:observation_visit_occurrence_id.
    ?instance_owl ?p13 ?visit_occurrence_id.}
OPTIONAL{?p14 rdf:type omop:observation_visit_detail_id.
    ?instance_owl ?p14 ?visit_detail_id.}
?p15 rdf:type omop:observation_source_value.
    ?instance_owl ?p15 ?observation_source_value_uri.
?p22 rdf:type omop:local_concept.
    ?observation_source_value_uri ?p22 ?observation_source_value.
OPTIONAL{?p16 rdf:type omop:observation_source_concept_id.
    ?instance_owl ?p16 ?observation_source_value_uri.
    ?observation_source_value_uri owl:sameAs ?omop_p16.
    ?omop_p16 std:domain_id ?omop_domain_p16.
      FILTER(?omop_domain_p16="Observation" || ?omop_p16= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p16 std:concept_id ?observation_source_concept_id.}
OPTIONAL{?p17 rdf:type omop:observation_unit_source_value.
    ?instance_owl ?p17 ?unit_source_value_uri.
    ?unit_source_value_uri ?p22 ?unit_source_value.}
OPTIONAL{?p18 rdf:type omop:qualifier_source_value. 
    ?instance_owl ?p18 ?qualifier_source_value_uri.
    ?qualifier_source_value_uri ?p22 ?qualifier_source_value}
}
"""
    return query
