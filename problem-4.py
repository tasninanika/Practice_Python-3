# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:19:12 2025

@author: Jarin
"""
#Problem 4: Continue - Skip Multiples of 3
#Write a Python program that prints numbers from 1 to 30, skipping all numbers that are multiples of 3. Use the continue statement to achieve this.

#Expected Output:
#1 2 4 5 7 8 10 ... (skipping multiples of 3)

for i in range(1, 31, 1):
    if i % 3 == 0:
        continue
    else:
        print(i)

i = 1        
while(i < 31):
    if i % 3 == 0:
        i = i + 1
        continue
    else:
        print(i) 
        i = i + 1
    
    