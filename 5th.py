# for loop
# for i in range(5)
# print(i)

# for i in range(9,4,-2):
#     print(i)

# for i in range(9,4,-1):
#      print(i)


# write a prgm to print pattern
# for i in range(6):
#     print('*'*i)
    

# for i in range(6,0,-1):
#     print('*'*i)
    

# n=1    
# for i in range(6):
#     for j in range(i+1):
#         print(n,end=" ")
#         n=n+1
#     print()


n=6
for i in range(5):
    n=n-1
    print(end="  "*n)
    for j in range(i+1):
        print(j+1,end="   ")
        # n=n+1
    print()
