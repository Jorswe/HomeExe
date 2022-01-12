# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:06:49 2022

@author: Yarden
"""
import statistics as stats

 
list_diff_average = lambda list1, list2: stats.mean( abs(list1[n] - list2[n]) for n in range(len(list1)))


no_spaces_in_begining = lambda list_of_string: [string.lstrip() for string in list_of_string]


no_spaces_begining_ending = lambda string: ' '.join(string.split())


find_duplicates = lambda list1: True if len(set(list1)) != len(list1) else False

