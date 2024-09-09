def query_procedure_occurrence():
    query = """
PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>

SELECT DISTINCT ?procedure_occurrence_id ?person_id ?procedure_concept_id ?procedure_date ?procedure_datetime ?procedure_type_concept_id ?modifier_concept_id ?quantity ?provider_id ?visit_occurrence_id ?visit_detail_id ?procedure_source_value ?procedure_source_concept_id ?modifier_source_value
WHERE {
    ?p1 rdf:type omop:procedure_occurrence_id.
    ?instance_owl ?p1 ?procedure_occurrence_id.
?p2 rdf:type omop:procedure_occurrence_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:procedure_concept_id.
    ?instance_owl ?p3 ?procedure_concept_id_1.
    ?procedure_concept_id_1 owl:sameAs ?omop_p3.
    ?omop_p3 std:domain_id ?omop_domain_p3.
      FILTER(?omop_domain_p3="Procedure" || ?omop_p3= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p3 std:standard_concept_id ?procedure_concept_id_uri.
      ?procedure_concept_id_uri std:concept_id ?procedure_concept_id.
OPTIONAL{?p4 rdf:type omop:procedure_date.
    ?instance_owl ?p4 ?procedure_date.}
OPTIONAL{?p5 rdf:type omop:procedure_datetime.
    ?instance_owl ?p5 ?procedure_datetime.}
OPTIONAL{?p6 rdf:type omop:procedure_type_concept_id.
    ?instance_owl ?p6 ?procedure_type_concept_id_1.
    ?procedure_type_concept_id_1 owl:sameAs ?omop_p6.
    ?omop_p6 std:domain_id ?omop_domain_p6.
      FILTER(?omop_domain_p6="Type Concept")
      ?omop_p6 std:standard_concept_id ?procedure_type_concept_id_uri.
      ?procedure_type_concept_id_uri std:concept_id ?procedure_type_concept_id.}
OPTIONAL{?p7 rdf:type omop:modifier_concept_id.
    ?instance_owl ?p7 ?modifier_concept_id.}
OPTIONAL{?p8 rdf:type omop:procedure_occurrence_quantity.
    ?instance_owl ?p8 ?quantity.}
OPTIONAL{?p9 rdf:type omop:procedure_occurrence_provider_id.
    ?instance_owl ?p9 ?provider_id.}
OPTIONAL{?p10 rdf:type omop:procedure_occurrence_visit_occurrence_id.
    ?instance_owl ?p10 ?visit_occurrence_id.}
OPTIONAL{?p11 rdf:type omop:procedure_occurrence_visit_detail_id.
    ?instance_owl ?p11 ?visit_detail_id.}
?p12 rdf:type omop:procedure_source_value.
    ?instance_owl ?p12 ?procedure_source_value_uri.
?p12bis rdf:type omop:local_concept.
    ?procedure_source_value_uri ?p12bis ?procedure_source_value
OPTIONAL{?p13 rdf:type omop:procedure_source_concept_id.
    ?instance_owl ?p13 ?procedure_source_value_uri.
    ?procedure_source_value_uri owl:sameAs ?omop_p13.
    ?omop_p13 std:domain_id ?omop_domain_p13.
      FILTER(?omop_domain_p13="Procedure" || ?omop_p13= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
      ?omop_p13 std:concept_id ?procedure_source_concept_id.}
OPTIONAL{?p14 rdf:type omop:modifier_source_value.
    ?instance_owl ?p14 ?modifier_source_value_uri.
    ?modifier_source_value_uri ?p12bis ?modifier_source_value}
}
"""
    return query
