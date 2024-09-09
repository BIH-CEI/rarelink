def query_death():
    query = """
PREFIX omop: <http://ontoks.clinic.cat/ontologias/omop.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_omop: <http://infmed.fcrb.es/ontologias/datanex_omop.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/datanex_reg.owl#>
    
SELECT DISTINCT ?person_id ?death_date ?death_datetime ?death_type_concept_id ?cause_concept_id ?cause_source_value ?cause_source_concept_id
    
WHERE{
    ?p1 rdf:type omop:death_person_id.
    ?instance_owl ?p1 ?person_id.
    
    ?p2 rdf:type omop:death_death_date.
    ?instance_owl ?p2 ?death_date.
    OPTIONAL{
    ?p3 rdf:type omop:death_death_datetime.
    ?instance_owl ?p3 ?death_datetime.     
    }

    OPTIONAL{
    ?p4 rdf:type omop:death_death_type_concept_id.
    ?instance_owl ?p4 ?death_type_concept_id.
    }
 
    OPTIONAL{
    ?p5 rdf:type omop:death_cause_concept_id.
    ?instance_owl ?p5 ?cause_concept_id.     
    }

    OPTIONAL{
    ?p6 rdf:type omop:death_cause_source_value.
    ?instance_owl ?p6 ?cause_source_value.    
    }

    OPTIONAL{
    ?p7 rdf:type omop:death_cause_source_concept_id.
    ?instance_owl ?p7 ?cause_source_concept_id.  
    }
}
    
    """
    return query