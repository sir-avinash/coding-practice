# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:37:52 2018

@author: Avinash

Palindrome Checker using Recursion

"""

def isPalindrome(givenStr):
   givenStr = givenStr.lower() ## case insensitive
   if len(givenStr) <= 1:
       return True
   elif givenStr[0] == givenStr[-1]:
       return isPalindrome(givenStr[1:-1])
   else:
       return False
   
    
if __name__ == "__main__":
    
    test1 = "kayak"
    test2 = "python"
    test3 = "malayalam"
    
    print(isPalindrome(test1))
    print(isPalindrome(test2))
    print(isPalindrome(test3))