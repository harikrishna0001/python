import sqlite3

con=sqlite3.connect('employe.db')

# data=con.execute("select * from employe_details")
# for i in data:
#     print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
# con.execute("update employe_details set age='22' where empname='hari'")
# con.commit()

# con.execute("delete from employe_details where email='hahaah'")
# con.commit()

# data=con.execute("select * from employe_details where empname='sonu'")
# data=con.execute("select empname,phone from employe_details where empname='sonu'")
# data=con.execute("select * from employe_details where empname like 'h%' ")
# data=con.execute("select * from employe_details where empname like '__n%' ")
# data=con.execute("select * from employe_details where empname like '%i' ")
data=con.execute("select * from employe_details ")
print("{:<20}{:<20}{:<20}{:<20}".format("empname","age","email","phone"))
print("_"*80)

for i in data:
    print("{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3]))
    
a=con.execute('select count(*) from employe_details')
for i in a:
    print(i)
a=con.execute('select sum(phone) from employe_details')
for i in a:
    print(i)
a=con.execute('select avg(age) from employe_details')
for i in a:
    print(i)
a=con.execute('select max(age) from employe_details')
for i in a:
    print(i)
    a=con.execute('select min(age) from employe_details')
for i in a:
    print(i)