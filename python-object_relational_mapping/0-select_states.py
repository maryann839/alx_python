import MySQLdb
import sys

print(sys.argv)
host = 'localhost'
port = 3306
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]



connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states")

records = cursor.fetchall()

for x in records:
    print(x)








