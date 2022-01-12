# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:47:13 2022

@author: Yarden
"""
def product(*args, **kwargs):
    listargs = []
    for i in range(len(args)):
        listargs.append(tuple(args[i]))
    products = [[]]
    for i in range(len(listargs)):
            products = [x + [y] for x in products for y in listargs[i]]
    for prod in products:
        yield prod

p=list(product((1, 2), ['AB', 'CD', 'EF'], (4, 5)))