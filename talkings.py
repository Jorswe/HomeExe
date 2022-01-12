# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:08:18 2022

@author: Yarden
"""


class Person:
    
    def __init__(self, first_name, family_name, age):
        if age < 0 and age > 150:
            raise ValueError("Age must be between 0 and 150 ")
            
        if type(first_name) != str:
            raise TypeError("First name must be a string")
        else:
            if first_name.isalpha() != True:
                raise ValueError("First name must be alphabetical")
                
        if type(family_name) != str:
            raise TypeError("First name must be a string")
        else:
            if family_name.isalpha() != True:
                raise ValueError("Family name must be alphabetical")
                
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


class Talker(Person):
    
    def talk(self, text):
        raise NotImplementedError("Please implement a talk function")


class HappyTalker(Talker):
    
    def talk(self, text):
        return text + "!!!"
    
    
class SlowTalker(Talker):
    
    def talk(self, text):
        return text.replace("", " ")


class StutterTalker(Talker):
    
    def talk(self, text):
        text_as_string=text.split()
        
        for string_num in range(len(text_as_string)):
            text_as_string[string_num] = (2 * text_as_string[string_num][0]
                                          + text_as_string[string_num])
        return " ".join(text_as_string)


def make_them_talk(talkers, say_what):
    for talker in talkers:
        if talker.age >= 10:
            print(talker.first_name, talker.family_name,
                  talker.talk(say_what))
    
   
happy=HappyTalker("h", "T", 3)
slow=SlowTalker("sl", "T", 30)
stutter=StutterTalker ("st", "T", 20)     
make_them_talk([happy, slow, stutter], "say wha")           
    
        
            
        
        
