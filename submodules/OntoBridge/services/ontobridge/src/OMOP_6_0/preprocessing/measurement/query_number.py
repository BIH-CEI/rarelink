def query_measurement_number():
    query = """
PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>

SELECT DISTINCT ?measurement_id ?person_id ?measurement_concept_id ?measurement_date ?measurement_datetime ?measurement_time ?measurement_type_concept_id ?operator_concept_id ?value_as_number ?value_as_concept_id ?unit_concept_id ?range_low ?range_high ?provider_id ?visit_occurrence_id ?visit_detail_id ?measurement_source_value ?measurement_source_concept_id ?unit_source_value ?value_source_value
 WHERE {
?p1 rdf:type omop:measurement_id.
    ?instance_owl ?p1 ?measurement_id.
?p2 rdf:type omop:measurement_person_id.
    ?instance_owl ?p2 ?person_id.
?p3 rdf:type omop:measurement_concept_id.
    ?instance_owl ?p3 ?measurement_concept_id_1.
    ?measurement_concept_id_1 owl:sameAs ?omop_p3.
    ?omop_p3 std:domain_id ?omop_domain_p3.
      FILTER(?omop_domain_p3="Measurement" || ?omop_p3 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p3 std:standard_concept_id ?measurement_concept_id_uri.
      ?measurement_concept_id_uri std:concept_id ?measurement_concept_id.
?p4 rdf:type omop:measurement_date.
    ?instance_owl ?p4 ?measurement_date.
OPTIONAL{?p5 rdf:type omop:measurement_datetime.
    ?instance_owl ?p5 ?measurement_datetime.}
OPTIONAL{?p6 rdf:type omop:measurement_time.
    ?instance_owl ?p6 ?measurement_time.}
OPTIONAL{?p7 rdf:type omop:measurement_type_concept_id.}
OPTIONAL{?instance_owl ?p7 ?measurement_type_concept_id_1.
    ?measurement_type_concept_id_1 owl:sameAs ?omop_p7.
    ?omop_p7 std:domain_id ?omop_domain_p7.
      FILTER(?omop_domain_p7="Type Concept")
      ?omop_p7 std:standard_concept_id ?measurement_type_concept_id_uri.
      ?measurement_type_concept_id_uri std:concept_id ?measurement_type_concept_id.}
OPTIONAL{?p8 rdf:type omop:operator_concept_id.
    ?instance_owl ?p8 ?operator_concept_id_1.
    ?operator_concept_id_1 owl:sameAs ?omop_p8.
    ?omop_p8 std:domain_id ?omop_domain_p8.
      FILTER(?omop_domain_p8="Meas Value Operator")
      ?omop_p8 std:standard_concept_id ?operator_concept_id_uri.
      ?operator_concept_id_uri std:concept_id ?operator_concept_id.} 
?p9 rdf:type omop:measurement_value_as_number.
    ?instance_owl ?p9 ?value_as_number.
OPTIONAL{?p11 rdf:type omop:unit_concept_id.
    ?instance_owl ?p11 ?unit_concept_id_1.
    ?unit_concept_id_1 owl:sameAs ?omop_p11.
    ?omop_p11 std:domain_id ?omop_domain_p11.
      FILTER(?omop_domain_p11="Unit")
      ?omop_p11 std:standard_concept_id ?unit_concept_id_uri.
      ?unit_concept_id_uri std:concept_id ?unit_concept_id.}
OPTIONAL{?p12 rdf:type omop:range_low.
    ?instance_owl ?p12 ?range_low.}
OPTIONAL{?p13 rdf:type omop:range_high.
    ?instance_owl ?p13 ?range_high.}
OPTIONAL{?p14 rdf:type omop:measurement_provider_id.
    ?instance_owl ?p14 ?provider_id.}
OPTIONAL{?p15 rdf:type omop:measurement_visit_occurrence_id.
    ?instance_owl ?p15 ?visit_occurrence_id.}
OPTIONAL{?p16 rdf:type omop:measurement_visit_detail_id.
    ?instance_owl ?p16 ?visit_detail_id.}
?p17 rdf:type omop:measurement_source_value.
    ?instance_owl ?p17 ?measurement_source_value_uri.
?p21 rdf:type omop:local_concept.
	?measurement_source_value_uri ?p21 ?measurement_source_value.
  OPTIONAL{?p18 rdf:type omop:measurement_source_concept_id.
    ?instance_owl ?p18 ?measurement_source_value_uri.
    ?measurement_source_value_uri owl:sameAs ?omop_p18.
    ?omop_p18 std:domain_id ?omop_domain_p18.
      FILTER(?omop_domain_p18="Measurement" || ?omop_p18 = <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0>)
      ?omop_p18 std:concept_id ?measurement_source_concept_id.}
OPTIONAL{?p19 rdf:type omop:unit_source_value.
    ?instance_owl ?p19 ?unit_source_value_1.
    ?unit_source_value_1 ?p21 ?unit_source_value.}
OPTIONAL{?p20 rdf:type omop:value_source_value.
    ?instance_owl ?p20 ?value_source_value_1.
    ?value_source_value_1 owl:sameAs ?omop_p20.
    ?omop_p20 std:domain_id ?omop_domain_p20.
      FILTER(?omop_domain_p20="Meas Value")
      ?omop_p20 std:concept_code ?value_source_value.} 
 }

"""
    return query
