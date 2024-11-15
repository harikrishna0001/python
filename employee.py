import sqlite3

con=sqlite3.connect('employee.db')
try:
   con.execute('create table employe_details(empid int,empname text,salary int,bonus int,incentive int)')
except:
    pass
a=int(input("enter the limit :"))
for i in range (a):
 id=int(input("Enter the employe id :"))
 name=input("Enter the employe name :")
 salary=int(input("enter the empolye salary :"))
 bonus=int(input("enter the empolye bonus :"))
 incentive=int(input("enter the empolye inccentive :"))
 con.execute("insert into employe_details values(?,?,?,?,?)",(id,name,salary,bonus,incentive))
 con.commit()
 print("data added  successfully")