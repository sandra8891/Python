import sqlite3
conn=sqlite3.connect('mydb.db')
cursor=conn.cursor()

# create table
# cursor.execute("CREATE TABLE STUDENT(ROLLNO text,Name text)")

# EXECUTE
#method1 to execute one name and rollno
# cursor.execute("INSERT INTO STUDENT(ROLLNO, NAME) VALUES(?, ?)",('101','Anu'))

# method2 to execute more than one name and rollno
# data = [('101', 'Anu'), ('22', 'John'),('55','baby')]
# cursor.executemany("INSERT INTO STUDENT(ROLLNO, NAME) VALUES(?, ?)", data)

# DELETE
#method1 to delete one item from list
# cursor.execute("DELETE FROM STUDENT WHERE ROLLNO = ?", ('101',))

#method2 to delete more than one item from .list
# cursor.execute("DELETE FROM STUDENT WHERE ROLLNO IN (?, ?)", ('101', '22'))

# method3 to delete
# cursor.execute("DELETE FROM STUDENT WHERE ROLLNO = 55")

#METHOD4 TO DELETE A TABLE
# cursor.execute("DROP TABLE STUDENT")

# conn.commit()
# conn.close()
# print("data inserted")

# To display a table
# p=cursor.execute("SELECT * FROM STUDENT" )
# for i in p:
#     print(i)

# To dispaly name only
# p=cursor.execute("SELECT NAME FROM STUDENT")
# for i in p:
#     print(i)

# To display rollno greater than a number
# p=cursor.execute("SELECT * FROM STUDENT WHERE ROLLNO>22")
# for i in p:
#     print(i)
    
# update
# p=cursor.execute("UPDATE STUDENT SET  NAME='Manu' WHERE ROLLNO=55 " )
# for i in p:
#     print(i) 
    
# to find LARGEST rollno
# p=cursor.execute("SELECT MAX(ROLLNO)FROM STUDENT" )
# for i in p:
#     print(i) 

# to find smallest rollno
# p=cursor.execute("SELECT MIN(ROLLNO)FROM STUDENT" )
# for i in p:
#     print(i) 

# to find the same values
# p=cursor.execute("SELECT NAME,COUNT(*)FROM STUDENT GROUP BY NAME" )
# for i in p:
#     print(i) 

conn.commit()
conn.close()




