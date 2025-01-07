# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:14:46 2025

@author: Jarin
"""

main_list = [1, 5, 6, 5, 1, 2, 3]
duplicates_list = []

for i in main_list:
  if main_list.count(i) > 1:
    if i not in duplicates_list:
      duplicates_list.append(i)

print(duplicates_list)