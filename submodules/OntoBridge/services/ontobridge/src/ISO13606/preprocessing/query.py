def query_iso13606():
    query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX iso13606_2: <http://ontoar.clinic.cat/ontologias/iso_13606_dt.owl#>
PREFIX iso13606_1: <http://ontoar.clinic.cat/ontologias/iso_13606_1.owl#>

SELECT ?ehr_extract_rc_id_root ?ehr_extract_rc_id_extension ?ehr_extract_rc_id_in ?ehr_id_root ?ehr_id_extension ?ehr_system_root ?ehr_system_extension ?composition_rc_id_root ?composition_rc_id_extension ?composition_rc_id_in ?archetypeId_root ?archetypeId_extension ?archetypeId_in ?entry_instance_root ?entry_instance_ext ?entry_instance_in ?property_root ?property_ext ?property_in ?property_value_datetime ?property_value_root ?property_value_ext ?property_value_cv ?property_value_code_system ?property_value_cs ?property_value_real ?property_value_pq ?property_value_pq_unit_code

WHERE {
  ?ehr_extract_instance rdf:type iso13606_1:EHR_EXTRACT .
  ?ehr_extract_instance iso13606_1:rc_id ?ehr_extract_rc_id .
  ?ehr_extract_rc_id iso13606_2:root ?ehr_extract_rc_id_root .
  ?ehr_extract_rc_id iso13606_2:extension ?ehr_extract_rc_id_extension .
  OPTIONAL{ ?ehr_extract_rc_id iso13606_2:identifier_name ?ehr_extract_rc_id_in . }

  ?ehr_extract_instance iso13606_1:ehr_id ?ehr_id .
  ?ehr_id iso13606_2:root ?ehr_id_root .
  ?ehr_id iso13606_2:extension ?ehr_id_extension .

  ?ehr_extract_instance iso13606_1:ehr_system ?ehr_system .
  ?ehr_system iso13606_2:root ?ehr_system_root .
  ?ehr_system iso13606_2:extension ?ehr_system_extension .

  ?ehr_extract_instance iso13606_1:compositions ?composition_instance .
  ?composition_instance iso13606_1:rc_id ?composition_rc_id .
  ?composition_rc_id iso13606_2:root ?composition_rc_id_root .
  ?composition_rc_id iso13606_2:extension ?composition_rc_id_extension .
  OPTIONAL{ ?composition_rc_id iso13606_2:identifier_name ?composition_rc_id_in . }

  ?composition_instance iso13606_1:content ?entry_instance .

  ?entry rdf:type iso13606_1:ENTRY_def .
  ?entry iso13606_1:archetype_id ?archetypeId .
  ?archetypeId iso13606_2:extension ?archetypeId_extension .
  ?archetypeId iso13606_2:root ?archetypeId_root . 
  ?archetypeId iso13606_2:identifier_name ?archetypeId_in .  

  ?entry_instance rdf:type ?entry .
  ?entry_instance iso13606_1:rc_id ?entry_rc_id .
  ?entry_rc_id iso13606_2:root ?entry_instance_root .
  ?entry_rc_id iso13606_2:extension ?entry_instance_ext .
  OPTIONAL{ ?entry_instance iso13606_2:identifier_name ?entry_instance_in . }
 
  ?entry_instance ?property ?property_value .
  
  ?property iso13606_1:element_archetype_id ?element_archetype_id .
  ?element_archetype_id iso13606_2:root ?property_root .
  ?element_archetype_id iso13606_2:extension ?property_ext .
  ?element_archetype_id iso13606_2:identifier_name ?property_in .  
  
  OPTIONAL{ ?property_value iso13606_2:datetime_value ?property_value_datetime }
  OPTIONAL{
 	?property_value iso13606_2:root ?property_value_root .
    ?property_value iso13606_2:extension ?property_value_ext .
  }

  OPTIONAL{
 	?property_value iso13606_2:code_cv ?property_value_cv .
    ?property_value iso13606_2:code_system ?property_value_code_system .
  }

  OPTIONAL{
 	?property_value iso13606_2:code_cs ?property_value_cs . 
  }

  OPTIONAL{
 	?property_value iso13606_2:real_value ?property_value_real .
  }

  OPTIONAL{
 	?property_value iso13606_2:physical_quantity_value ?property_value_pq .
    OPTIONAL{
 	  ?property_value iso13606_2:unit ?property_value_pq_unit .
    ?property_value_pq_unit iso13606_2:code_cs ?property_value_pq_unit_code .
  }
  }

}
"""
    return query
