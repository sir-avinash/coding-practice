# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 00:04:56 2018

@author: Avinash

Reverse a string using Recursion
"""

def strRev(givenStr):
    if len(givenStr) == 1:
        revStr = givenStr[-1]
    else:
        revStr = givenStr[-1] + strRev(givenStr[:-1]) 
     
    return revStr    
        
test1 = 'apple'
test2 = 'googol'

print(strRev(test1))

print(strRev(test2))
        