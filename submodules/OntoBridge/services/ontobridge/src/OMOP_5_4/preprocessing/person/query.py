def query_person():
    query = """
PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>

SELECT DISTINCT ?person_id ?gender_concept_id ?year_of_birth ?month_of_birth ?day_of_birth ?birth_datetime ?race_concept_id ?ethnicity_concept_id ?location_id ?provider_id ?care_site_id ?person_source_value ?gender_source_value ?gender_source_concept_id ?race_source_value ?race_source_concept_id ?ethnicity_source_value ?ethnicity_source_concept_id
WHERE {
    ?p1 rdf:type omop:person_id.
    ?instance_owl ?p1 ?person_id.
?p2 rdf:type omop:gender_concept_id.
    ?instance_owl ?p2 ?gender_concept_id_1.
    ?gender_concept_id_1 owl:sameAs ?omop_p2.
    ?omop_p2 std:domain_id ?omop_domain_p2.
     FILTER(?omop_domain_p2="Gender")
     ?omop_p2 std:standard_concept_id ?gender_concept_id_uri.
     ?gender_concept_id_uri std:concept_id ?gender_concept_id.
?p3 rdf:type omop:year_of_birth.
    ?instance_owl ?p3 ?year_of_birth.
OPTIONAL{?p4 rdf:type omop:month_of_birth.
    ?instance_owl ?p4 ?month_of_birth.}
OPTIONAL{?p5 rdf:type omop:day_of_birth.
    ?instance_owl ?p5 ?day_of_birth.}
OPTIONAL{?p6 rdf:type omop:birth_datetime.
    ?instance_owl ?p6 ?birth_datetime.}
OPTIONAL{?p8 rdf:type omop:race_concept_id.
    ?instance_owl ?p8 ?race_concept_id_1.
    ?race_concept_id_1 owl:sameAs ?omop_p8.
    ?omop_p8 std:domain_id ?omop_domain_p8.
    FILTER(?omop_domain_p8="Race" || ?omop_p8= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
    ?omop_p8 std:standard_concept_code ?race_concept_id_uri.
    ?race_concept_id_uri std:concept_id ?race_concept_id.}
OPTIONAL{?p9 rdf:type omop:ethnicity_concept_id.
    ?instance_owl ?p9 ?ethnicity_concept_id_1.
    ?ethnicity_concept_id_1 owl:sameAs ?omop_p9.
    ?omop_p9 std:domain_id ?omop_domain_p9.
    FILTER(?omop_domain_p9="Ethnicity" || ?omop_p9= <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_0> )
    ?omop_p9 std:standard_concept_code ?ethnicity_concept_id_uri.
    ?ethnicity_concept_id_uri std:concept_id ?ethnicity_concept_id.}
OPTIONAL{?p10 rdf:type omop:person_location_id.
    ?instance_owl ?p10 ?location_id.}
OPTIONAL{?p11 rdf:type omop:person_provider_id.
    ?instance_owl ?p11 ?provider_id.}
OPTIONAL{?p12 rdf:type omop:person_care_site_id.
    ?instance_owl ?p12 ?care_site_id.}
OPTIONAL{?p13 rdf:type omop:person_source_value.
    ?instance_owl ?p13 ?person_source_value.}
OPTIONAL{?p14 rdf:type omop:gender_source_value.
    ?instance_owl ?p14 ?gender_source_value_1.
    ?gender_source_value_1 owl:sameAs ?omop_p14.
    ?omop_p14 std:domain_id ?omop_domain_p14.
     FILTER(?omop_domain_p14="Gender")
     ?omop_p14 std:concept_code ?gender_source_value.}
?p15 rdf:type omop:gender_source_concept_id.
    ?instance_owl ?p15 ?gender_source_concept_id_1.
    ?gender_source_concept_id_1 owl:sameAs ?omop_p15.
    ?omop_p15 std:domain_id ?omop_domain_p15.
     FILTER(?omop_domain_p15="Gender")
     ?omop_p15 std:concept_id ?gender_source_concept_id.
OPTIONAL{?p16 rdf:type omop:race_source_value.
    ?instance_owl ?p16 ?race_source_value.}
OPTIONAL{?p17 rdf:type omop:race_source_concept_id.
    ?instance_owl ?p17 ?race_source_concept_id_1.
    ?race_source_concept_id_1 owl:sameAs ?omop_p17.
    ?omop_p17 std:domain_id ?omop_domain_p17.
    FILTER(?omop_domain_p17="Race")
     ?omop_p17 std:concept_id ?race_source_concept_id.}
OPTIONAL{?p18 rdf:type omop:ethnicity_source_value.
    ?instance_owl ?p18 ?ethnicity_source_value.}
OPTIONAL{?p19 rdf:type omop:ethnicity_source_concept_id.
    ?instance_owl ?p19 ?ethnicity_source_concept_id_1.
    ?ethnicity_source_concept_id_1 owl:sameAs ?omop_p19.
    ?omop_p19 std:domain_id ?omop_domain_p19.
    FILTER(?omop_domain_p17="Ethnicity")
     ?omop_p19 std:concept_id ?ethnicity_source_concept_id.}
}
"""
    return query
