# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:09:56 2025

@author: Jarin
"""

#Problem 1: For Loop - Sum of Even Numbers
#Write a Python program that asks the user for a positive integer n and calculates the sum of all even numbers from 1 to n using a for loop.
#Example:
#Input: n = 10
#Output: Sum of even numbers: 30

n = int(input("Enter a positive number: "))
sum = 0

for i in range(2, n, 2):
   sum += i
print(sum)

# another way
n = int(input("Enter a positive number: "))
sum = 0

for i in range(1, n, 1):
    if(i % 2 == 0):
        sum += i
print(sum)