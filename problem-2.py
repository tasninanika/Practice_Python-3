# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:25:03 2025

@author: Jarin
"""

#Problem 2: While Loop - Guess the Number
#Create a guessing game where the program generates a random number between 1 and 50. The user has to guess the number. After each guess, the program provides a hint:
#"Too high" if the guess is greater than the number.
#"Too low" if the guess is less than the number.
#The loop ends when the user guesses the correct number.


import random

num = int(random.randrange(1, 50))
guessNum = 0
while(num != guessNum):
    guessNum = int(input("Enter a number: "))

    if(num < guessNum):
        print("Too high")
    elif(num > guessNum):
        print("Too low")
    else:
        print("Correct")
        
    
    