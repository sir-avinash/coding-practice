# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:43:04 2018

@author: Avinash

Find elements that add up an arbitrary sum
"""

## Brute Force Algorithm
def elementsOfSum(alist, gsum):
    found = False
    i = j = 0
    while i < len(alist) - 1:
        while j < len(alist):
            if alist[i] + alist[j] == gsum:
                found = True
                print(i, j)
                break
            else:
                j +=1
        i+=1
     
    return found, alist[i], alist[j]             









if __name__ == "__main__":

    alist = [2,3,4,78.54,32,90]
    
    gsum = 82
    
    found, num1, num2 = elementsOfSum(alist, gsum)
    
    print(found, num1, num2)