"""
Created on Wed Jul 25 20:53:49 2018

@author: Avinash

Factorial of n
"""

def factorial(n):
    if n<=1:
        result = 1
    else:
        result = n*factorial(n-1)
        
    return result

print(factorial(10))