import sqlite3
conn=sqlite3.connect('mydb.db')
cursor=conn.cursor()

# cursor.execute("CREATE TABLE STUDENT(ID Text, NAME Text, AGE Text, GRADE Text, CITY Text)")


# data = [('1', 'Anu','14','B','Ernakulam'), ('2', 'John','15','A+','Thrissur'),('3','Manu','14','A','Kozhikode'),('4', 'Alex','15','A+','Malappuram'),('5','Chikku','14','B+','Kozhikode')]
# cursor.executemany("INSERT INTO STUDENT(ID, NAME,AGE,GRADE,CITY) VALUES(?, ?,?,?,?)", data)

# p=cursor.execute("UPDATE STUDENT SET  NAME='Aromal' WHERE ID=3 " )
# for i in p:
#     print(i)

cursor.execute("DELETE FROM STUDENT WHERE ID=1")
# cursor.execute("DROP TABLE STUDENT")
conn.commit()
conn.close()
print("data inserted")

