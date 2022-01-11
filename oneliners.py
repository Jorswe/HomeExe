# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:06:49 2022

@author: Yarden
"""
import statistics as stats

 
ListDiffAverage=lambda list1,list2 : stats.mean( abs(list1[n] - list2[n]) for n in range(len(list1)))

NoSpacesInBegining=lambda listofstring: [string.lstrip() for string in listofstring]

NoSpacesBeginingEnding=lambda string:' '.join(string.split())

FindDuplicates=lambda list1 :True if len(set(list1))!=len(list1) else False

