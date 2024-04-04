import MySQLdb
from urllib.parse import quote_plus
import sys

if len(sys.argv) != 5:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
host = 'localhost'
port = 3306

encoded_password = quote_plus(password)

try:
    connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
    cursor = connection.cursor()

    # Execute the query to fetch cities
    query = """
            SELECT name
            FROM cities
            WHERE state_id IN (
                SELECT id
                FROM states
                WHERE name = %s
            )
            ORDER BY id ASC
            """
    cursor.execute(query, ("Texas",))  # Replace "Texas" with the state_name variable

    records = cursor.fetchall()

    # Store city names in a list
    city_names = [record[0] for record in records]

    # Print the city names joined by comma and space
    print(", ".join(city_names))

except MySQLdb.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    if 'connection' in locals() or 'connection' in globals():
        connection.close()
