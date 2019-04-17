# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:53:52 2018

@author: Avinash

Recursion to convert interger to string
"""

def int2str(num):
    base = 10
    baseChars = "0123456789"
    if str(num) in baseChars:
        num_str = str(num)
    else:
        num_str = int2str(num//base) + str(num%base)
        
    return num_str

def int2strBaseN(num, baseChars, base):
    
    if num < base:
        return baseChars[num] 
    else:
        return int2strBaseN(num//base, baseChars, base) + baseChars[num % base]
            

if __name__ == "__main__":

    test_num = 34567234
    
    test_result = int2str(test_num)
    
    print(test_result)
    
    print(test_result.__class__)
    
    base = 14
    baseChars = "0123456789ABCDEF"
    
    test_result16 = int2strBaseN(test_num, baseChars, base)
    
    print(test_result16)

        
        