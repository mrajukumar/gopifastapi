import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="test"
)

print(mydb.get_server_info())
mydb.close()

