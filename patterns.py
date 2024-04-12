# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:01:31 2024

@author: Admin
"""
"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
         print("*",end=" ")
    print("")
    
#or
rows = 5
for j in range(1, rows+1):
    print("* " * j)    
#***************************************************************  
"""
* * * * *  
* * * *  
* * *  
* *  
*  
"""
rows = 5
for i in range(rows ,0, -1):
    # nested reverse loop
    for j in range(i):
        # display star
        print("*", end=' ')
    print(" ")
  
#***************************************************************  



"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
         print(j,end=" ")
    print("")
#***************************************************************    
"""
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
"""    
rows=5
for i in range(1,rows+1):
    for j in range(i):
         print(i,end=" ")
    print("")
    
#**************************************************************   
"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

"""    
rows=5
for i in range(rows,0,-1):
    for j in range(i):
         print(rows-i+1,end=" ")
    print("")
           
         #or
         
rows=5
x=1
for i in range(rows,0,-1):
    for j in range(i):
         print(x,end=" ")
    x+=1     
    print("")
                  
#**************************************************************    
"""
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
"""

rows=5
for i in range(rows,0,-1):
    for j in range(i):
         print(rows-j,end=" ")
    print("")
#**************************************************************         

"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5 

"""

rows=5
for i in range(rows,0,-1):
    for j in range(i):
         print(rows,end=" ")
        
    print("")

"""Multiplication table
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
"""
rows=8
for i in range(1,rows+1):
    for j in range(1,i+1):
         print(i*j,end=" ")
        
    print("")
         
#**************************************************************         
         
#***************    
# #Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number    
# n= int(input("Enter a number\n"))
# s=0
# for i in range (n+1):
#     s+=i
# print("The sum of all numbers till {0}  = {1}".format(n,s) )   

# #or with built in function
# n= int(input("Enter a number\n"))
# x = sum(range(1, n + 1))
# print("The sum of all numbers till {0}  = {1}".format(n,x) )  

# #Write a program to print multiplication table of a given number 
# n= int(input("Enter a number\n"))
# for i in range(1,11):
#     print("{0} * {1} = {2}".format(n,i,n*i))
 
    
#  # count no of digits
#  n= int(input("Enter a number\n"))
# count=0

# while (n!=0):
#  count+=1
#  n=n//10
# print(count)
 

