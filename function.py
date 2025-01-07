# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:08:40 2025

@author: Jarin
"""

# static function
def gretting():
    print('Jarin Tasnin Anika')

gretting()




# dynamic function

def my_print(x):
    print(x)

my_print('Jarin')




# practice

def my_range(start_num, end_num, increment_num):
    while start_num <= end_num:
        print(start_num)
        start_num += 1

my_range(0, 20, 1)




# calculator

def calculator(num1, num2, operation):
  if operation == "Add":
    print(num1 + num2)
  elif operation == "Sub":
    print(num1 - num2)
calculator(10, 5, "Add")




# to return value

def calculator(num1, num2, operation):
  if operation == "Add":
    cal=(num1 + num2)
  elif operation == "Sub":
    cal=(num1 - num2)
  return cal
    
    
number = calculator(10, 5, "Add")




# globally variable declaration

def calculator(num1, num2, operation):
      global cal
      if operation == "Add":
        cal=(num1 + num2)
      elif operation == "Sub":
        cal=(num1 - num2)
      return cal

number = calculator(10, 5, "Add")
print(cal)    




# multiple numbers

def multi_number(*numbers):
    print(numbers)

multi_number(11, 13, 12)


# sum of multiple numbers
def multi_num_sum(*numbers):
    global total
    total = 0
    for i in numbers:
        total += i
    return total

multi_num_sum(10, 10, 10)
print(total)


def calculator(*numbers, operation):
  if operation == "Add":
      total = 0
      for i in numbers:
          total += i
      return total

  elif operation == "Sub":
       sub = 0
       for i in numbers:
           sub -= i
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
        


number = calculator(10, 5, 10, operation = "Mul")
print(number)        
   


