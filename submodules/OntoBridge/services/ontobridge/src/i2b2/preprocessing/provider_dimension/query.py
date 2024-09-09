def query_provider_dimension():
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

#Queries de PROVIDER_DIMENSION

SELECT DISTINCT ?provider_id ?provider_path ?name_char ?provider_blob ?update_date ?download_date ?import_date ?sourcesystem_cd ?upload_id
WHERE { 
?provider_id_PD rdf:type i2b2:provider_id_PD .
?registro ?provider_id_PD ?provider_id .

OPTIONAL {?provider_path_PD rdf:type i2b2:provider_path_PD .
?registro ?provider_path_PD ?provider_path .}

OPTIONAL {?name_char_PD rdf:type i2b2:name_char_PD .
?registro ?name_char_PD ?name_char .}

OPTIONAL {?provider_blob_PD rdf:type i2b2:provider_blob_PD .
?registro ?provider_blob_PD ?provider_blob .}

OPTIONAL {?update_date_PD rdf:type i2b2:update_date_PD .
?registro ?update_date_PD ?update_date .}

OPTIONAL {?download_date_PD rdf:type i2b2:download_date_PD .
?registro ?download_date_PD ?download_date .}

OPTIONAL {?import_date_PD rdf:type i2b2:import_date_PD .
?registro ?import_date_PD ?import_date .}

OPTIONAL {?sourcesystem_cd_PD rdf:type i2b2:sourcesystem_cd_PD .
?registro ?sourcesystem_cd_PD ?sourcesystem_cd .}

OPTIONAL {?upload_id_PD rdf:type i2b2:upload_id_PD .
?registro ?upload_id_PD ?upload_id .}

}
        
    """
    return query
