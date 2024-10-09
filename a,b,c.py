a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>b):
    if(c>a):
        print(a,"is larger")
    else:
        print(c,"is larger")
else:
    if(b>c):
        print(b,"is larger")
    else:
        print(c,"is larger")
    