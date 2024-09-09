def query_observation_fact():
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
    
SELECT DISTINCT ?encounter_num ?patient_num ?concept_cd ?provider_id ?start_date ?modifier_cd ?instance_num ?valtype_cd ?tval_char ?nval_num ?valueflag_cd ?quantity_num ?units_cd ?end_date ?location_cd ?observation_blob ?confidence_num ?update_date ?download_date ?import_date ?sourcesystem_cd ?upload_id?text_search_index
WHERE { 
?encounter_num_OF rdf:type i2b2:encounter_num_OF .
?registro ?encounter_num_OF ?encounter_num .

?patient_num_OF rdf:type i2b2:patient_num_OF .
?registro ?patient_num_OF ?patient_num .

?concept_cd_OF rdf:type i2b2:concept_cd_OF .
?registro ?concept_cd_OF ?concept .
?concept owl:sameAs ?concept_i2b2 .
?concept_i2b2 i2b2_sc:concept_cd ?concept_cd .

OPTIONAL {?provider_id_OF rdf:type i2b2:provider_id_OF .
?registro ?provider_id_OF ?provider_id .}

?start_date_OF rdf:type i2b2:start_date_OF .
?registro ?start_date_OF ?start_date .

OPTIONAL {?modifier_cd_OF rdf:type i2b2:modifier_cd_OF .
?registro ?modifier_cd_OF ?modifier .
?modifier owl:sameAs ?modifier_i2b2 .
?modifier_i2b2 i2b2_sc:modifier_cd ?modifier_cd .}

OPTIONAL {?instance_num_OF rdf:type i2b2:instance_num_OF .
?registro ?instance_num_OF ?instance_num .}

OPTIONAL {?valtype_cd_OF rdf:type i2b2:valtype_cd_OF .
?registro ?tvaltype_cd_OF ?valtype_cd_name .
?valtype_cd_name owl:sameAs ?valtype_cd_i2b2 .
?valtype_cd_i2b2 i2b2_sc:name_char ?valtype_cd .}

OPTIONAL {?tval_char_OF rdf:type i2b2:tval_char_OF .
?registro ?tval_char_OF ?tval_char_source .
?tval_char_source owl:sameAs ?tval_char_i2b2 .
?tval_char_i2b2 i2b2_sc:name_char ?tval_char .}

OPTIONAL {?nval_num_OF rdf:type i2b2:nval_num_OF .
?registro ?nval_num_OF ?nval_num .}

OPTIONAL {?valueflag_cd_OF rdf:type i2b2:valueflag_cd_OF .
?registro ?valueflag_cd_OF ?valueflag_cd_name .
?valueflag_cd_name owl:sameAs ?valueflag_cd_i2b2 .
?valueflag_cd_i2b2 i2b2_sc:name_char ?valueflag_cd .}

OPTIONAL {?quantity_num_OF rdf:type i2b2:quantity_num_OF .
?registro ?quantity_num_OF ?quantity_num .}

OPTIONAL {?units_cd_OF rdf:type i2b2:units_cd_OF .
?registro ?units_cd_OF ?units_cd_name .
?units_cd_name owl:sameAs ?units_cd_i2b2 .
?units_cd_i2b2 i2b2_sc:name_char ?units_cd .}

OPTIONAL {?end_date_OF rdf:type i2b2:end_date_OF .
?registro ?end_date_OF ?end_date .}

OPTIONAL {?location_cd_OF rdf:type i2b2:location_cd_OF .
?registro ?location_cd_OF ?location_cd_name .
?location_cd_name owl:sameAs ?location_cd_i2b2 .
?location_cd_i2b2 i2b2_sc:name_char ?location_cd .}

OPTIONAL {?observation_blob_OF rdf:type i2b2:observation_blob_OF .
?registro ?observation_blob_OF ?observation_blob .}

OPTIONAL {?confidence_num_OF rdf:type i2b2:confidence_num_OF .
?registro ?confidence_num_OF ?confidence_num .}

OPTIONAL {?update_date_OF rdf:type i2b2:update_date_OF .
?registro ?update_date_OF ?update_date .}

OPTIONAL {?download_date_OF rdf:type i2b2:download_date_OF .
?registro ?download_date_OF ?download_date .}

OPTIONAL {?import_date_OF rdf:type i2b2:import_date_OF .
?registro ?import_date_OF ?import_date .}

OPTIONAL {?sourcesystem_cd_OF rdf:type i2b2:sourcesystem_cd_OF .
?registro ?sourcesystem_cd_OF ?sourcesystem_cd .}

OPTIONAL {?upload_id_OF rdf:type i2b2:upload_id_OF .
?registro ?upload_id_OF ?upload_id .}

OPTIONAL {?text_search_index_OF rdf:type i2b2:text_search_index_OF .
?registro ?text_search_index_OF ?text_search_index .}
}
    """
    return query
