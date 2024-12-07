import sqlite3
conn=sqlite3.connect('mydb.db')
cursor=conn.cursor()

# create table
# cursor.execute("CREATE TABLE STUDENT(ROLLNO text,Name text)")

#method1 to execute one name and rollno
# cursor.execute("INSERT INTO STUDENT(ROLLNO, NAME) VALUES(?, ?)",('101','Anu'))

# method2 to execute more than one name and rollno
# data = [('101', 'Anu'), ('22', 'John'),('55','baby')]
# cursor.executemany("INSERT INTO STUDENT(ROLLNO, NAME) VALUES(?, ?)", data)

#method1 to delete one item from list
# cursor.execute("DELETE FROM STUDENT WHERE ROLLNO = ?", ('101',))

#method2 to delete more than one item from .list
# cursor.execute("DELETE FROM STUDENT WHERE ROLLNO IN (?, ?)", ('101', '22'))

conn.commit()
conn.close()
print("data inserted")

