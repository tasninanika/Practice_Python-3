# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:58:55 2025

@author: Jarin
"""

#Problem 3: Break - Prime Number Checker
#Write a program that takes an integer input n and checks if it's a prime number using a loop. Use break to exit the loop early if the number is not prime.
#Example:
#Input: n = 11
#Output: 11 is a prime number
#Input: n = 10
#Output: 10 is not a prime number


n = int(input("Enter a number: "))

if n % 2 != 0:
    print("It's a prime number")
else:
    break