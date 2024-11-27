# class Car:
#     def disp():
#         print("Hello World")
# obj1=Car
# obj1.disp()

# class Car:
#     def __init__(self,name1,color):
#         self.name=name1
#         self.color=color
#     def disp(self):
#         print("Name",self.name)
#         print("Color",self.color)
# obj1=Car("swift","red")
# obj1.disp()


class Bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        a=int(input("enter a amount:"))
        self.balance=self.balance+a
        print("cash deposited")
    def withdrawal(self):
        b=int(input("enter a the amount:"))
        if b<=self.balance:
            print("amount debeted")
            self.balance=self.balance-b
        else:
            print("insufficent balance")
    def check_balance(self):
        print(self.balance) 
obj1=Bank(0)
d="y"
while(d=="y"):
    print("1.deposit 2.withdrawal 3.checkbalance 4.exit")
    c=int(input("which one do you wish to run:"))
    if c==1:
        obj1.deposit()
    elif c==2:
        obj1.withdrawal()
    elif c==3:
        obj1.check_balance()
    else:
        print("exit")
    d=(input("do you want to continue y/n:"))
                   