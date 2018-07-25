# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 18:41:57 2018

@author: avinash

Script using "Divide by n" algorithm to convert any decimal number to base n

Deps: Custom Stack class

"""

from stack import Stack

def convert2baseN(num, base):

    if base > 36
        ValueError('Only bases upto 36 allowed :-/')    
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    base_stack = Stack()
        
    while num > 0:
        rem = num % base        
        base_stack.push(rem)
        num = num // base

    base_num = ""
    while not base_stack.isEmpty():
        base_num += str(base_stack.pop())
        
    return int(base_num)

if __name__ == "__main__":
    
    test_num = 88888888898676895327138598558735749026431764198264237584
    test_base = 3
    test_num_base2 = convert2baseN(test_num, test_base)
    print(test_num_base2)    