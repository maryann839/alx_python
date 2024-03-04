
import MySQLdb
import sys


username, password, database, state_name_searched = sys.argv[1:5]

host = 'localhost'
port = 3306
username = 'root'
password = '@Nadiaann839'
db = "hbtn_0e_0_usa"




connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
cursor = connection.cursor()

query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
cursor.execute(query, (state_name_searched,))

states = cursor.fetchall()

for state in states:
    print(state)








