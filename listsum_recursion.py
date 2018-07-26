# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:03:09 2018

@author: Avinash

Using recursion to find a sum of the list
"""
import time

def listsum(givenList):
    firstnum = givenList[0]
    if len(givenList) == 1:
        sum = firstnum
    else:
        sum = firstnum + listsum(givenList[1:])  
    return sum

def listsum_iter(givenList):
    sum = 0
    for num in givenList:
        sum += num
    return sum 

test_list = list(range(500))

use_recur = 1
if use_recur:
    starttime_recur = time.time()        
    print(listsum(test_list))
    endtime_recur = time.time() - starttime_recur
else:
    endtime_recur = 0

starttime_iter = time.time()
print(listsum_iter(test_list))
endtime_iter = time.time() - starttime_iter

print("Recursion Time: {}, Iteration Time: {}".format(endtime_recur, endtime_iter))