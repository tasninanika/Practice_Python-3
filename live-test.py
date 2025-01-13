# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:16:59 2025

@author: Jarin
"""

def hourToMin(hour):
  min = hour * 60
  return min

hour = int(input("Enter the hour you want to convert: "))
min = hourToMin(hour)

print(f"Your Given Hour is: {hour} hour")
print(f"Your Given Hour in Minute is: {min} min")