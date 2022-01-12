# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:22:39 2022

@author: Yarden
"""


decorator_memory=[]
def save_repeted_returns(function):
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
    def inner(*args, **kargs):
        for line in decorator_memory:
            if(line[1] == args and function == line[0]):
                return (line[2])
        decorator_memory.append((function,args, function(args)))
        return decorator_memory[len(decorator_memory) - 1][2]
    return inner
    

@save_repeted_returns
def fibonachi(args, *kwargs):
  
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
    if len(args) != 1:
        return -1
    location=args[0]
    if location <= 2:
        return 1
    else:
        return fibonachi(location - 2) + fibonachi(location - 1)

   

