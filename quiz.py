# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:15:17 2025

@author: Jarin
"""

# What is the output of the following code

salary = 8000

def printSalary():

    salary = 12000

    print("Salary:", salary)

printSalary()

print("Salary:", salary)



#What is the output of the following function call

def fun1(name, age=20):

         print(name, age)

fun1('Emma')


#What is the output of the following list assignment?

aList = [4, 8, 12, 16]

aList[1:4] = [20, 24, 28]

print(aList)



#What is the output of the following for loop and range() function

for num in range(-2,-5,-1):

    print(num, end=", ")



#Given the following code:

my_list = [10, 20, 30, 40, 50] 
 

sliced_list = my_list[-4:-1]  

print(sliced_list)  



#What is the output of the following code?

my_dict = {"x": 100, "y": 200, "z": 300}
  

value = my_dict.get("a", "Key not found")  

print(value)  



#Given the following code:

set1 = {1, 2, 3, 4}  

set2 = {3, 4, 5, 6}  

result = set1 ^ set2  

print(result)  
