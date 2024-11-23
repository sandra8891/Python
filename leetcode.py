#1Q. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order

# method1
# def twosum(num, target):
#     length=len(num)
#     for i in range(length):
#         for j in range(i+1,length):
#             if num[i]+num[j]==target:
#                 return[i,j]
# n=[2,3,4,5,6]
# t=9
# print(twosum(n,t))

# method2
#list1=[2,3,4,5,6,7]
# target=8
# res=[]
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         t=list1[i]+list1[j]
#         if t==target:
#             if i in res and j in res:
#                 pass
#             else:
#                 print(i,j)
#                 res.append(i)
#                 res.append(j)
        
    
    
# 2Q.Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".  
  

