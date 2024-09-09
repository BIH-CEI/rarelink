LOAD DATA INFILE '/Users/adam/Documents/GIT/RareLink/database/RareLink_v2.0_DataDictionary.csv'
INTO TABLE RD-CDM
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';


CREATE TABLE rarelink_data (
    record_id INT PRIMARY KEY,
    snomed_422549004 VARCHAR(255), -- Pseudonym
    snomed_399423000 DATE,         -- Date of Admission
    personal_information_descr TEXT, -- Descriptive field for personal information
    snomed_184099003 DATE          -- Date of Birth
);

