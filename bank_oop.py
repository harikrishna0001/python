class bank:
    def __init__(self):
        self.pin=1234
        self.balance=0
    def deposit(self):
        upin=int(input("enter your pin to continue :"))
        if upin==self.pin:
            udep=int(input("enter the deposit :"))
            self.balance=self.balance+udep
            print("amount credited")
        else:
            print("incorrect pin")
    def withdraw(self):
        upin=int(input("enter your pin to cntinue :"))
        if upin==self.pin:
            uwid=int(input("enter the amount :"))
            if uwid<=self.balance:
                self.balance=self.balance-uwid
            print("amount  withdrawed")
        else:
            print("incorrect pin")
    def blnc(self):
        upin=int(input("enter your pin to cntinue :"))
        if upin==self.pin:
            print(self.balance)
        else:
            print("incorrect pin")
            
user1=bank()
while True:
    print("""
            1.deposit
            2.withdraw
            3.balance
            4.exit""")
    choice=int(input("enter your choice :"))
    if choice==1:
        user1.deposit()
    elif choice==2:
        user1.withdraw()
    elif choice==3:
        user1.blnc()
    elif choice==4:
        break