# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:33:43 2025

@author: Jarin
"""

def sort_ascending(unsorted_list):
  for i in range(len(unsorted_list)):
    for j in range(i + 1, len(unsorted_list)):  
      if unsorted_list[i] > unsorted_list[j]:
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[j]
        unsorted_list[j] = temp
  return unsorted_list

unsorted_list = [1, 5, 2, 9, 3, 22, 13]
sorted_list = sort_ascending(unsorted_list)
print(sorted_list)
