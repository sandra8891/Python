import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="sandra",
    password="pass123",
    database='Mydb'
)
print("connected successfully!")
connection.close()