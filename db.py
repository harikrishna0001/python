import sqlite3

con=sqlite3.connect('employe.db')
try:
   con.execute('create table employe_details(empname text,age int,email text,phone int,username text,password text)')
except:
    pass
a=int(input("enter the limit :"))
for i in range (a):
 name=input("Enter the employe name :")
 age=int(input("Enter the employe age :"))
 email=input("Enter the employe email :")
 phone=int(input("enter the empolye phone number :"))
 username=input("enter the username :")
 password=input("enter the password :")
 con.execute("insert into employe_details values(?,?,?,?,?,?)",(name,age,email,phone,username,password))
 con.commit()
 print("data added  successfully")