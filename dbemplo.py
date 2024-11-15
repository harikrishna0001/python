import sqlite3

con=sqlite3.connect('employe1.db')

# n_admno=int(input("enter the admno of employe need change :"))
# n_name=input("enter the updated name :")
# con.execute('update employe1 set Name=? where admno=?',(n_name,n_admno))
# con.commit()

data=con.execute('select * from employe_details')