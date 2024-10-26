from addm import *
add()
sub()

while True:
  print(""" 1.Addition
              2.Substraction
              3.Multiplication
              4.Division
              5.Exit  """)
  
  choice=int(input("Enter your choice : "))
  if choice==1:
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        res=add(a,b)
        print(res)

  elif choice==2:
        no1=int(input("Enter first number :"))
        no2=int(input("Enter second number :"))
        res=sub(no1,no2)
        print(res)
        

    # elif choice==3:
    #     no1=int(input("Enter first number :"))
    #     no2=int(input("Enter second number :"))
    #     res=mul(no1,no2)
    #     print(res)
        
    
    # elif choice==4:
    #     no1=int(input("Enter first number :"))
    #     no2=int(input("Enter second number :"))
    #     res=div(no1,no2)
    #     print(res)
        
    # elif choice==5:
    #     break
    
