import MySQLdb


host = 'localhost'
port = 3306
username = 'root'
password = '@Nadiaann839'
database = "hbtn_0e_0_usa"


connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
cursor = connection.cursor()
import MySQLdb


host = 'localhost'
port = 3306
username = 'root'
password = '@Nadiaann839'
database = "hbtn_0e_0_usa"


connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
cursor = connection.cursor()

query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cursor.execute(query)

records = cursor.fetchall()

for x in records:
    print(x)








