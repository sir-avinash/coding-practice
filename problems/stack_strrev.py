# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:50:41 2018

@author: avinash

Script to implement string reverse using a stack

Deps: Custom Stack class

"""

from stack import Stack

def reverse_str(string):
    
    s = Stack()
    reverse_string = ''    
    for letter in string:
        s.push(letter)
    while not s.isEmpty():
        reverse_string = reverse_string + s.pop()
        
    return reverse_string   
        

if __name__ == "__main__":
    
    test_string = "abcdefghijklmnopqrstuvwxyz"

    rev_test_string = reverse_str(test_string)

    print(rev_test_string)