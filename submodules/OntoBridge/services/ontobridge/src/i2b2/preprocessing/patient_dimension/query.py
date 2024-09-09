def query_patient_dimension():
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

SELECT DISTINCT ?patient_num ?vital_status_cd ?birth_date ?death_date ?sex_cd ?age_in_years_num ?language_cd ?race_cd ?marital_status_cd ?religion_cd ?zip_cd ?statecityzip_path ?income_cd ?patient_blob ?update_date ?download_date ?import_date ?sourcesystem_cd ?upload_id

WHERE { 
?patient_num_PAD rdf:type i2b2:patient_num_PAD .
?registro ?patient_num_PAD ?patient_num .

OPTIONAL {?vital_status_cd_PAD rdf:type i2b2:vital_status_cd_PAD .
?registro ?vital_status_cd_PAD ?vital_status_cd_name .
?vital_status_name owl:sameAs ?vital_status_cd_i2b2 .
?vital_status_i2b2 i2b2_sc:name_char ?vital_status_cd .}

?birth_date_PAD rdf:type i2b2:birth_date_PAD .
?registro ?birth_date_PAD ?birth_date .

?death_date_PAD rdf:type i2b2:death_date_PAD .
OPTIONAL {?registro ?death_date_PAD ?death_date .}

?sex_cd_PAD rdf:type i2b2:sex_cd_PAD .
?registro ?sex_cd_PAD ?sex_cd_uri .
?local_sex_cd rdf:type i2b2:local_sex_CD .
?sex_cd_uri ?local_sex_cd ?sex_cd .

OPTIONAL {?age_in_years_num_PAD rdf:type i2b2:age_in_years_num_PAD .
?registro ?age_in_years_num_PAD ?age_in_years_num .}

OPTIONAL {?language_cd_PAD rdf:type i2b2:language_cd_PAD .
?registro ?language_cd_PAD ?language_cd_name .
?language_cd_name owl:sameAs ?language_cd_i2b2 .
?language_cd_i2b2 i2b2_sc:name_char ?language_cd .}

OPTIONAL {?race_PAD rdf:type i2b2:race_PAD .
?registro ?race_PAD ?race_cd_name .
?race_cd_name owl:sameAs ?race_cd_i2b2 .
?race_cd_i2b2 i2b2_sc:name_char ?race_cd .}

OPTIONAL {?marital_status_cd_PAD rdf:type i2b2:marital_status_cd_PAD .
?registro ?marital_status_cd_PAD ?marital_status_cd_name .
?marital_status_cd_name owl:sameAs ?marital_status_cd_i2b2 .
?marital_status_cd_i2b2 i2b2_sc:name_char ?marital_status_cd .}

OPTIONAL {?religion_cd_PAD rdf:type i2b2:religion_cd_PAD .
?registro ?religion_cd_PAD ?religion_cd_name .
?religion_cd_name owl:sameAs ?religion_cd_i2b2 .
?religion_cd_i2b2 i2b2_sc:name_char ?religion_cd .}

OPTIONAL {?zip_cd_PAD rdf:type i2b2:zip_cd_PAD .
?registro ?zip_cd_PAD ?zip_cd .}

OPTIONAL {?statecityzip_path_PAD rdf:type i2b2:statecityzip_path_PAD .
?registro ?statecityzip_path_PAD ?statecityzip_path .}

OPTIONAL {?income_cd_PAD rdf:type i2b2:income_cd_PAD .
?registro ?income_cd_PAD ?income_cd_name .
?income_cd_name owl:sameAs ?income_cd_i2b2 .
?income_cd_i2b2 i2b2_sc:name_char ?income_cd .}

OPTIONAL {?patient_blob_PAD rdf:type i2b2:patient_blob_PAD .
?registro ?patient_blob_PAD ?patient_blob .}

OPTIONAL {?update_date_PAD rdf:type i2b2:update_date_PAD .
?registro ?update_date_PAD ?update_date .}

OPTIONAL {?download_date_PAD rdf:type i2b2:download_date_PAD .
?registro ?download_date_PAD ?download_date .}

OPTIONAL {?import_date_PAD rdf:type i2b2:import_date_PAD .
?registro ?import_date_PAD ?import_date .}

OPTIONAL {?sourcesystem_cd_PAD rdf:type i2b2:sourcesystem_cd_PAD .
?registro ?sourcesystem_cd_PAD ?sourcesystem_cd .}

OPTIONAL {?upload_id_PAD rdf:type i2b2:upload_id_PAD .
?registro ?upload_id_PAD ?upload_id .}

}
    """
    return query
