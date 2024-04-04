import MySQLdb
from urllib.parse import quote_plus
import sys


if len(sys.argv) != 5:
    print("Usage: python script_name.py <db_username> <db_password> <db_name> <state_name>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]
host = 'localhost'
port = 3306

encoded_password = quote_plus(password)

try:
    connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
    cursor = connection.cursor()
    
    # Execute the query to fetch cities of the given state
    query = """
            SELECT cities.id, cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))

    records = cursor.fetchall()

    for x in records:
        print(x)

except MySQLdb.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    if 'connection' in locals() or 'connection' in globals():
        connection.close()
