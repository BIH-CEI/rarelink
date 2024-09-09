import pandas as pd
import numpy as np 
import os
from datetime import datetime

now = datetime.now()
timestamp_str = now.strftime("%Y_%m_%d_%H_%M_%S")

def load_iso_data(file_path):
    """ Load ISO 13606 data from a CSV file. """
    return pd.read_csv(file_path, sep=';')

def generate_xml_files_per_ehr_extract(df, write_folder):
    for ehr_extract in np.unique(df.ehr_extract_rc_id_extension.values):
        df_ehr_extract = df[df.ehr_extract_rc_id_extension == ehr_extract]
        file_name = os.path.join(write_folder, f"ehr_extract_{ehr_extract}_{timestamp_str}.xml")
        
        xml_file = []
        indent = ""

        # Add EHR_EXTRACT
        xml_file.append(f'{indent}<EHR_EXTRACT rm_id="ISO 13606">')
        indent += "\t"
        xml_file.append(f'{indent}<ehr_system extension="{df_ehr_extract.ehr_system_extension.values[0]}" root="{df_ehr_extract.ehr_system_root.values[0]}" xsi:type="INSTANCE_IDENTIFIER"/>')
        xml_file.append(f'{indent}<ehr_id extension="{df_ehr_extract.ehr_id_extension.values[0]}" root="{df_ehr_extract.ehr_id_root.values[0]}" xsi:type="INSTANCE_IDENTIFIER"/>')
        xml_file.append(f'{indent}<rc_id extension="{df_ehr_extract.ehr_extract_rc_id_extension.values[0]}" root="{df_ehr_extract.ehr_extract_rc_id_root.values[0]}" xsi:type="INSTANCE_IDENTIFIER"/>')

        # Iterate over each COMPOSITION within the EHR_EXTRACT
        for composition in np.unique(df_ehr_extract.composition_rc_id_extension.values):
            df_composition = df_ehr_extract[df_ehr_extract.composition_rc_id_extension == composition]
            
            xml_file.append(f'{indent}<compositions xsi:type="COMPOSITION">')
            indent += "\t"
            xml_file.append(f'{indent}<rc_id extension="{df_composition.composition_rc_id_extension.values[0]}" root="{df_composition.composition_rc_id_root.values[0]}" xsi:type="INSTANCE_IDENTIFIER"/>')
            
            # Iterate over each ENTRY within the COMPOSITION
            for entry in np.unique(df_composition.entry_instance_ext.values):
                df_entry = df_composition[df_composition.entry_instance_ext == entry]
                
                xml_file.append(f'{indent}<members xsi:type="ENTRY">')
                indent += "\t"
                xml_file.append(f'{indent}<rc_id extension="{df_entry.entry_instance_ext.values[0]}" root="{df_entry.entry_instance_root.values[0]}" xsi:type="INSTANCE_IDENTIFIER"/>')
                xml_file.append(f'{indent}<archetype_id extension="{df_entry.archetypeId_extension.values[0]}" identifier_name="{df_entry.archetypeId_in.values[0]}" root="{df_entry.archetypeId_root.values[0]}" xsi:type="INSTANCE_IDENTIFIER"/>')

                # Iterate over each ELEMENT within the ENTRY
                for n in range(len(df_entry)):
                    row = df_entry.iloc[n]

                    xml_file.append(f'{indent}<items xsi:type="ELEMENT">')
                    indent += "\t"
                    xml_file.append(f'{indent}<rc_id extension="{df_entry.entry_instance_ext.values[0]}_{row.property_in}" root="clinic" xsi:type="INSTANCE_IDENTIFIER"/>')
                    xml_file.append(f'{indent}<archetype_id extension="{row.property_ext}" identifier_name="{row.property_in}" root="{row.property_root}" xsi:type="INSTANCE_IDENTIFIER"/>')

                    # Add VALUE
                    if not pd.isna(row.property_value_datetime):
                        xml_file.append(f'{indent}<value xsi:type="DATE_TIME" value="{row.property_value_datetime}"/>')
                    elif not pd.isna(row.property_value_cv):
                        display_name = f"{row.property_value_code_system} {row.property_value_cv}"
                        xml_file.append(f'{indent}<value code_cv="{row.property_value_cv}" code_system="{row.property_value_code_system}" display_name="{display_name}" xsi:type="CODED_VALUE"/>')
                    elif not pd.isna(row.property_value_cs):
                        xml_file.append(f'{indent}<value code_cs="{row.property_value_cs}" xsi:type="CODED_SIMPLE"/>')
                    elif not pd.isna(row.property_value_root):
                        xml_file.append(f'{indent}<value extension="{row.property_value_ext}" root="clinic" identifier_name="{row.property_value_root}" xsi:type="INSTANCE_IDENTIFIER"/>')
                    elif not pd.isna(row.property_value_real):
                        xml_file.append(f'{indent}<value value="{row.property_value_real}" xsi:type="REAL"/>')
                    elif not pd.isna(row.property_value_pq):
                        xml_file.append(f'{indent}<value value="{row.property_value_pq}" xsi:type="PHYSICAL_QUANTITY"/>')
                        if not pd.isna(row.property_value_pq_unit_code):
                            xml_file.append(f'{indent}\t<unit xsi:type="CODED_SIMPLE" code="{row.property_value_pq_unit_code}"/>')

                    indent = indent[:-1]
                    xml_file.append(f'{indent}</items>')

                indent = indent[:-1]
                xml_file.append(f'{indent}</members>')

            indent = indent[:-1]
            xml_file.append(f'{indent}</compositions>')

        indent = indent[:-1]
        xml_file.append(f'{indent}</EHR_EXTRACT>')

        with open(file_name, "w") as archivo:
            for row in xml_file:
                archivo.write(row + "\n")
