def query_concept_dimension():
    query = """
    
#PREFIXES
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_i2b2: <http://ontoks.clinic.cat/ontologias/datanex_i2b2.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/reg_datanex.owl#>
PREFIX i2b2_sc: <http://ontoar.clinic.cat/ontologias/i2b2_standard_concepts.owl#>
PREFIX i2b2: <http://ontoks.clinic.cat/ontologias/i2b2.owl#>


#Queries de CONCEPT_DIMENSION

SELECT DISTINCT ?concept_path ?concept_cd ?name_char ?concept_blob ?update_date ?download_date ?import_date ?sourcesystem_cd ?upload_id
WHERE { 

?concept rdf:type ?concept_domain .
?concept_domain rdfs:subClassOf i2b2_sc:i2b2_Concepts .

?concept i2b2_sc:concept_cd ?concept_cd .
?concept i2b2_sc:concept_path ?concept_path .
?concept i2b2_sc:name_char ?name_char .

OPTIONAL {?concept_CD rdf:type i2b2:concept_blob_CD .
?concept ?concept_blob_CD ?concept_blob .}

OPTIONAL {?update_date_CD rdf:type i2b2:update_date_CD .
?concept ?update_date_CD ?update_date .}

OPTIONAL {?download_date_CD rdf:type i2b2:download_date_CD .
?concept ?download_date_CD ?download_date .}

OPTIONAL {?import_date_CD rdf:type i2b2:import_date_CD .
?concept ?import_date_CD ?import_date .}

OPTIONAL {?sourcesystem_cd_CD rdf:type i2b2:sourcesystem_cd_CD .
?concept ?sourcesystem_cd_CD ?sourcesystem_cd .}

OPTIONAL {?upload_id_CD rdf:type i2b2:upload_id_CD .
?concept ?upload_id_CD ?upload_id .}

}
    """
    return query
