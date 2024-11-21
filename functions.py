#   function defining
def addition():
    # function definition
    print("enter a number")
    a=int(input())
    b=int(input())
    print(a+b)
def subtraction():
    print("enter a number")
    a=int(input())
    b=int(input())
    print(a-b)
def multiplication():
    print("enter a number")
    a=int(input())
    b=int(input())
    print(a*b)
def division():
    print("enter a number")
    a=int(input())
    b=int(input())
    print(a/b)
print('''1.addition
2.subtraction
3.multiplication
4.division''')
c=int(input("enter your choice"))
if c==1:
    # function calling
    addition()
elif c==2:
     subtraction()
elif c==3:
    multiplication()
elif c==4:
    division()
else:
    print("failed")


