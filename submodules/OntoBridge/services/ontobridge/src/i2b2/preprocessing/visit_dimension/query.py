def query_visit_dimension():
    query = """

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX std: <http://ontoar.clinic.cat/ontologias/standard_concepts.owl#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX dtnex_i2b2: <http://ontoks.clinic.cat/ontologias/datanex_i2b2.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX reg: <http://infmed.fcrb.es/ontologias/reg_datanex.owl#>
PREFIX i2b2_sc: <http://ontoar.clinic.cat/ontologias/i2b2_standard_concepts.owl#>
PREFIX i2b2: <http://ontoks.clinic.cat/ontologias/i2b2.owl#>

#Queries de VISIT_DIMENSION

SELECT DISTINCT ?encounter_num ?patient_num ?active_status_cd ?start_date ?end_date ?inout_cd ?location_cd ?location_path ?length_of_stay ?visit_blob ?update_date ?download_date ?import_date ?sourcesystem_cd ?upload_id

WHERE { 
?encounter_num_VD rdf:type i2b2:encounter_num_VD .
?registro ?encounter_num_VD ?encounter_num .

?patient_num_VD rdf:type i2b2:patient_num_VD .
?registro ?patient_num_VD ?patient_num .

OPTIONAL {?active_status_cd_VD rdf:type i2b2:active_status_cd_VD .
?registro ?active_status_cd_VD ?active_status_cd_name .
?active_status_cd_name owl:sameAs ?active_status_cd_i2b2 .
?active_status_cd_i2b2 i2b2_sc:name_char ?active_status_cd .}

?start_date_VD rdf:type i2b2:start_date_VD .
?registro ?start_date_VD ?start_date .

OPTIONAL {?end_date_VD rdf:type i2b2:end_date_VD .
?registro ?end_date_VD ?end_date .}

OPTIONAL {?inout_cd_VD rdf:type i2b2:inout_cd_VD .
?registro ?inout_cd_VD ?inout_cd_name .
?inout_cd_name owl:sameAs ?inout_cd_i2b2 .
?inout_cd_i2b2 i2b2_sc:name_char ?inout_cd .}

OPTIONAL {?location_cd_VD rdf:type i2b2:location_cd_VD .
?registro ?location_cd_VD ?location_cd_name .
?location_cd_name owl:sameAs ?location_cd_i2b2 .
?location_cd_i2b2 i2b2_sc:name_char ?location_cd .}

OPTIONAL {?location_path_VD rdf:type i2b2:location_path_VD .
?registro ?location_path_VD ?location_path_name .
?location_path_name owl:sameAs ?location_path_i2b2 .
?location_path_i2b2 i2b2_sc:name_char ?location_path .}

OPTIONAL {?length_of_stay_VD rdf:type i2b2:length_of_stay_VD .
?registro ?length_of_stay_VD ?length_of_stay .}

OPTIONAL {?visit_blob_VD rdf:type i2b2:visit_blob_VD .
?registro ?visit_blob_VD ?visit_blob .}

OPTIONAL {?update_date_VD rdf:type i2b2:update_date_VD .
?registro ?update_date_VD ?update_date .}

OPTIONAL {?download_date_VD rdf:type i2b2:download_date_VD .
?registro ?download_date_VD ?download_date .}

OPTIONAL {?import_date_VD rdf:type i2b2:import_date_VD .
?registro ?import_date_VD ?import_date .}

OPTIONAL {?sourcesystem_cd_VD rdf:type i2b2:sourcesystem_cd_VD .
?registro ?sourcesystem_cd_VD ?sourcesystem_cd .}

OPTIONAL {?upload_id_VD rdf:type i2b2:upload_id_VD .
?registro ?upload_id_VD ?upload_id .}

}
    """
    return query
