# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:26:34 2018

@author: avinash

A Script to check if the given string has balanced paranthesis

Deps: Custom Stack class

"""

from stack import Stack

def paranChecker(test_string):
    
    par_stack = Stack()
    openers = "({[<"
    closers = ")}]>"

    isBalanced = True
    
    for ch in test_string:
        if ch in openers:
            par_stack.push(ch)
        else:            
            if not par_stack.isEmpty():
                top = par_stack.pop()
                if not openers.index(top) == closers.index(ch):
                    isBalanced = False         
            else: 
                isBalanced = False
                        
    if par_stack.isEmpty() and isBalanced:
        return True
    else:
         return False   
        

if __name__ == "__main__":
    
    test_string = "(([[]]))"
    
    print(paranChecker(test_string))