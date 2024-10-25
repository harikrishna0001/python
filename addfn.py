def add(**arg):
    return arg
def delete(a,b):
    return a-b
def show(a,b):
    return a*b

while True:
    print(""" 1.Add student
              2.delete student
              3.show all student
              4.exit""")
    choice=int(input("Enter your choice : "))
    if choice==1:
        name=(input("Enter the name of student:"))
        res=add(name)
        print(res)