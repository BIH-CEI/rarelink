def query_modifier_dimension():
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

#Queries de MODIFIER_DIMENSION

SELECT DISTINCT ?modifier_path ?modifier_cd ?name_char ?modifier_blob ?update_date ?download_date ?import_date ?sourcesystem_cd ?upload_id
WHERE { 

?modifier rdf:type ?modifier_domain .
?modifier_domain rdfs:subClassOf i2b2_sc:i2b2_Modifiers .

?modifier i2b2_sc:modifier_cd ?modifier_cd .
?modifier i2b2_sc:modifier_path ?modifier_path .
?modifier i2b2_sc:name_char ?name_char .

OPTIONAL {?modifier_blob_MD rdf:type i2b2:modifier_blob_MD .
?modifier ?modifier_blob_MD ?modifier_blob .}

OPTIONAL {?update_date_MD rdf:type i2b2:update_date_MD .
?modifier ?update_date_MD ?update_date .}

OPTIONAL {?download_date_MD rdf:type i2b2:download_date_MD .
?modifier ?download_date_MD ?download_date .}

OPTIONAL {?import_date_MD rdf:type i2b2:import_date_MD .
?modifier ?import_date_MD ?import_date .}

OPTIONAL {?sourcesystem_cd_MD rdf:type i2b2:sourcesystem_cd_MD .
?modifier ?sourcesystem_cd_MD ?sourcesystem_cd .}

OPTIONAL {?upload_id_MD rdf:type i2b2:upload_id_MD .
?modifier ?upload_id_MD ?upload_id .}

}
    """
    return query
