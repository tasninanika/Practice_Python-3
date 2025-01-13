# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:12:46 2025

@author: Jarin
"""

def calculator(*numbers, operation):
  if operation == "Add":
      total = 0
      for i in numbers:
          total += i
      return total

  elif operation == "Sub":
       sub = numbers[0]
       for i in numbers[1:]:
           sub = sub - i
           if(sub < 0):
               sub = 0
       return sub
  elif operation == "Mul":
       mul = 1
       for i in numbers:
           mul *= i
       return mul
  elif operation == "Div":
       div = 1
       for i in numbers:
           div /= i
       return div
        


number = calculator(10, 5, 10, operation = "Sub")
print(number)   
