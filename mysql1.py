import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="sandraks",
    password="pass123",
    database="myql"
)

cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE tudo1(
        CREATED_DATE TEXT,
        TITLE TEXT,
        DUE_DATE TEXT
    )
    """)
connection.commit()
print("Table 'tudo1' created successfully")
connection.commit
connection.close()

