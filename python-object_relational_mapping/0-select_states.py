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
cursor.execute("SELECT * FROM states")

records = cursor.fetchall()

for x in records:
    print(x)








