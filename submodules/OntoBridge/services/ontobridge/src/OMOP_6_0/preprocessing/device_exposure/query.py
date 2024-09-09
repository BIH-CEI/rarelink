def query_device_exposure():
    query = """
PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>

SELECT DISTINCT ?device_exposure_id ?person_id ?device_concept_id ?device_exposure_start_date ?device_exposure_start_datetime ?device_exposure_end_date ?device_exposure_end_datetime ?device_type_concept_id ?unique_device_id ?quantity ?provider_id ?visit_occurrence_id ?visit_detail_id ?device_source_value ?device_source_concept_id

WHERE {
?p1 rdf:type omop:device_exposure_id.
    ?instance_owl ?p1 ?device_exposure_id.
?p2 rdf:type omop:device_exposure_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:device_concept_id.
    ?instance_owl ?p3 ?device_concept_id_1.
    ?device_concept_id_1 owl:sameAs ?omop_p3.
    ?omop_p3 std:domain_id ?omop_domain_p3.
      FILTER(?omop_domain_p3="Device" || ?omop_p3 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p3 std:standard_concept_id ?device_concept_id_uri.
      ?device_concept_id_uri std:concept_id ?device_concept_id.
?p4 rdf:type omop:device_exposure_start_date.
    ?instance_owl ?p4 ?device_exposure_start_date.
OPTIONAL{?p5 rdf:type omop:device_exposure_start_datetime.
    ?instance_owl ?p5 ?device_exposure_start_datetime.}
OPTIONAL{?p6 rdf:type omop:device_exposure_end_date.
    ?instance_owl ?p6 ?device_exposure_end_date.}
OPTIONAL{?p7 rdf:type omop:device_exposure_end_datetime.
    ?instance_owl ?p7 ?device_exposure_end_datetime.}
OPTIONAL{?p8 rdf:type omop:device_type_concept_id.}
OPTIONAL{?instance_owl ?p8 ?device_type_concept_id_1.
    ?device_type_concept_id_1 owl:sameAs ?omop_p8.
    ?omop_p8 std:domain_id ?omop_domain_p8.
      FILTER(?omop_domain_p8="Type Concept")
      ?omop_p8 std:standard_concept_id ?device_type_concept_id_uri.
      ?device_type_concept_id_uri std:concept_id ?device_type_concept_id.}
OPTIONAL{?p9 rdf:type omop:unique_device_id.
    ?instance_owl ?p9 ?unique_device_id.}
OPTIONAL{?p10 rdf:type omop:device_exposure_quantity.
    ?instance_owl ?p10 ?quantity.}
OPTIONAL{?p11 rdf:type omop:device_exposure_provider_id.
    ?instance_owl ?p11 ?provider_id.}
OPTIONAL{?p12 rdf:type omop:device_exposure_visit_occurrence_id.
    ?instance_owl ?p12 ?visit_occurrence_id.}
OPTIONAL{?p13 rdf:type omop:device_exposure_visit_detail_id.
    ?instance_owl ?p13 ?visit_detail_id.}
?p14 rdf:type omop:device_source_value.
    ?instance_owl ?p14 ?device_source_value_uri.
?p14bis rdf:type omop:local_concept.
  ?device_source_value_uri ?p14bis ?device_source_value.
OPTIONAL{?p15 rdf:type omop:device_source_concept_id.
    ?instance_owl ?p15 ?device_source_value_uri.
    ?device_source_value_uri owl:sameAs ?omop_p15. 
    ?omop_p15 std:domain_id ?omop_domain_p15.
      FILTER(?omop_domain_p15="Device" || ?omop_p15 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p15 std:concept_id ?device_source_concept_id.} 
}
"""
    return query
