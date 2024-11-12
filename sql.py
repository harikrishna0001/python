import sqlite3

con=sqlite3.connect('students.db')

try:
    con.execute("create table std_details(admno int,name text,age int,eemail text)")
except:
    pass


# con.execute("insert into std_details values(101,'hari',22,'hari12@gmail.com')")
# con.commit()
a=int(input("enter your limit :"))
for i in range(a):
    admno=int(input("Enter the admission number of the students :"))
    name=input("Enter the name of the student :")
    age=int(input("Enter the age of  the student :"))
    email=input("Enter email of the student :")
    con.execute("insert into std_details values(?,?,?,?)",(admno,name,age,email))
    con.commit()
print("suceesfully addeed")