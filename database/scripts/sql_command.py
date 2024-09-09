import mysql.connector

# Set up the connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="rarelink_db"
)
cursor = connection.cursor()

# SQL query to create table
create_table_query = """
CREATE TABLE rarelink_data (
    record_id INT PRIMARY KEY,
    snomed_422549004 VARCHAR(255),
    snomed_399423000 DATE,
    personal_information_descr TEXT,
    snomed_184099003 DATE
);
"""
cursor.execute(create_table_query)
connection.commit()
cursor.close()
connection.close()
