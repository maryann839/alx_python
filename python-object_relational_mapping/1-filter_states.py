import MySQLdb
from urllib.parse import quote_plus
import sys


if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
host = 'localhost'
port = 3306

encoded_password = quote_plus(password)

connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
cursor = connection.cursor()

query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cursor.execute(query)

states = cursor.fetchall()

for state in states:
    print(state)








