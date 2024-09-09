-- create_tables.sql
CREATE DATABASE IF NOT EXISTS rarelink_db;

USE rarelink_db;

CREATE TABLE rarelink_data (
    record_id INT PRIMARY KEY,
    snomed_422549004 VARCHAR(255), -- Pseudonym
    snomed_399423000 DATE,         -- Date of Admission
    personal_information_descr TEXT, -- Descriptive field for personal information
    snomed_184099003 DATE          -- Date of Birth
);

