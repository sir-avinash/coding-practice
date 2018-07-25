# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 05:51:38 2018

@author: avinash

Palindrome checker script using a Deque

"""

from deque import Deque

def isPalindrome(string):
    
    palDQ = Deque()
    
    result = False
    
    for ch in string:
        palDQ.addRear(ch)
        
    while palDQ.size() > 1:
        if palDQ.removeFront() == palDQ.removeRear():
            result = True
            print(palDQ.items)
        else:
            break
        
    return result
    

if __name__ == "__main__":
    
    string = "malayala"
    
    print(isPalindrome(string))
