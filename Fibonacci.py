# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:22:39 2022

@author: Yarden
"""
decoratorMemory=[]
def decorator(func):
    """
    Decorator for heavy duty function
    
    Parameters
    ----------
    func : Heavy duty function which returns the same value for the same argument .

    Returns
    -------
    TYPE
        function output.

    """
    def inner(*args,**kargs):
        for line in decoratorMemory:
            if(line[1] == args and func == line[0]):
                return (line[2])   
        decoratorMemory.append((func,args,func(args)))   
        return decoratorMemory[len(decoratorMemory)-1][2]
    return inner 
    
    

@decorator
def fibonachi(args):
  
    """
    Parameters
    ----------
    args : int 
        The location number in fibonacci series  
    Returns
    -------
    int
        The number in the location 
    """
    if (len(args) != 1):
        return -1
    location=args[0]
    if (location <= 2):
        return 1
    else :
        return fibonachi(location - 2)+fibonachi(location - 1)

   

