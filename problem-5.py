# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:31:49 2025

@author: Jarin
"""

#Problem 5: Combination - Nested For Loop with Break and Continue
#Write a program that prints all pairs (i, j) where i ranges from 1 to 5 and j ranges from 1 to 5. Use a continue statement to skip printing pairs where i + j is even, and use break to stop the loop entirely if i * j > 15.

#Expected Output:
#Example: (1, 2), (1, 4), (2, 3) ... (following the conditions)

for i in range(1, 6, 1):
    for j in range(1, 6, 1):
        if (i + j) % 2 == 0:
            continue
        elif (i * j) > 15:
            break
        else:
            print(i, j)