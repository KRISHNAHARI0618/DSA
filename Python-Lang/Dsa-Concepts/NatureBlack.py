import mysql.connector

database = mysql.connector.connect(
host="localhost",
user="springstudent",
passwd="Butta7595@Hn3"

)

print(database)

database.close()
