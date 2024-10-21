l=['name','age','place']
d=dict.fromkeys(l,"null")
d.update({'name':'hari'})
d.update({'age':21})
d.update({'place':"kozhikode"})
print(d.get("name"))
print(d)