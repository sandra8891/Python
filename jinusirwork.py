# for i in range(5):
#     print('*'*i)
    
# n=5
# for i in range(n+1,0,-1):
#     for j in range(0,i-1):
#         print('*',end="")
#     print("")

# a=[4,2,5,3,1,3,4]   
# for i in range(len(a)):
#     print(a[i]*'*')


# a=[]
# i=1
# while i<=100:
#     if i%5==0 and i%3==0:
#         a.append('fizzbuzz')
#     elif i%5==0:
#         a.append('buzz')
#     elif i%3==0:
#         a.append('fizz')
#     else:
#         a.append(i)
#     i=i+1
# print(a)


# a=[]
# s=1
# while True:
#     print(
#         '1.add todo'
#           '2.display '
#           '3.edit '
#           '4.delete'
#           '5.quit'
#           )
#     choice=int(input('enter your choice'))
#     if choice==1:
#         task=input('enter the task')
#         a.append(task)
#     elif choice==2:
#         for i in range(len(a)):
#             print(s,a[i],) 
#             s=s+1   
#     elif choice==3:
#         for i in range(len(a)):
#             print(s,a[i])
#             s=s+1
#         index=int(input('enter the number'))
#         index=index-1
#         task=input('enter the task')
#         a[index]=task
#     elif choice==4:
#         index=int(input('enter the index'))
#         a.pop(index)
#     elif choice==5:
#         break
#     else:
#         print('invalid choice')    


# swapping
# a=5
# b=10
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# # swapping
# a=10
# b=5
# b,a=a,b
# print(a)
# print(b)


# recurssion
# def fact(n):
#     if n==0:
#         return(1)
#     else:
#       return n * fact(n - 1)
# n=int(input("enter a number"))
# x=fact(n)    
# print(x)

# factorial
# i=1
# fact=1
# n=int(input("enter a number"))
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)    
    
