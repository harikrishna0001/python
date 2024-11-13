import sqlite3

con=sqlite3.connect('employe.db')

data=con.execute("select * from employe_details")
for i in data:
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
con.execute("update employe_details set age='22' where empname='hari'")
con.commit()

con.execute("delete from employe_details where email='hahaah'")
con.commit()