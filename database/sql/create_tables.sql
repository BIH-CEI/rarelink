-- create_tables.sql
CREATE DATABASE IF NOT EXISTS rarelink_db;

USE rarelink_db;


CREATE TABLE rarelink_data (
    record_id INT PRIMARY KEY AUTO_INCREMENT,  -- Registry ID of the individual
    
    -- Formal Criteria Section
    snomed_422549004 VARCHAR(255),  -- 1.1 Pseudonym (SNOMED: 422549004)
    snomed_399423000 DATE,          -- 1.2 Date of Admission (SNOMED: 399423000)

    -- Personal Information Section
    personal_information_descr TEXT, -- Descriptive field for personal information
    snomed_184099003 DATE,           -- 2.1 Date of Birth (SNOMED: 184099003)

    -- Add more fields here if they exist in your data model (each corresponding to REDCap fields)
    -- Example fields based on REDCap structure:
    
    snomed_114000119 VARCHAR(255),  -- Example Field 1 (SNOMED code if available)
    snomed_117510000 VARCHAR(255),  -- Example Field 2 (another field from REDCap)
    
    -- Validation fields
    validation_type_1 VARCHAR(255),  -- Validation information if applicable (e.g., date validation)
    validation_type_2 VARCHAR(255),  -- Another validation field if needed

    -- Additional fields and notes
    notes_field_1 TEXT,             -- Notes or descriptions for any other field
    notes_field_2 TEXT              -- Another field for additional notes or descriptions
);