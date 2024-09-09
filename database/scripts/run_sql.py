import os
import mysql.connector

def create_database_and_table():
    # Get credentials from environment variables
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database="rarelink_db"
    )
    cursor = connection.cursor()

    # Read SQL from file
    with open('../sql/create_tables.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute the SQL script
    for statement in sql_script.split(';'):
        if statement.strip():
            cursor.execute(statement)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    create_database_and_table()
    