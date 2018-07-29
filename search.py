# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:47:16 2018

@author: Avinash

All my search scripts
"""

def sequentialSearch(glist, item):
    isExist = False
    count = 0
    
    while count < len(glist):
        if glist[count] == item:
            isExist = True
            break
        else:
            count += 1
    
#    print(count)        
    return isExist

def orderedSequentialSearch(glist, item):
#    glist.sort()
    isExist = False
    count = 0
    
    while count < len(glist):
        if glist[count] == item:
            isExist = True
            break
        else:
            if glist[count] > item:
                break
            else:
                count += 1
#    print(count)            
    return isExist

def binarySearch(glist, item):
     
    if len(glist) == 0:
        return False
    else: 
       index = len(glist) // 2
#       print(index)
       if glist[index] == item:
            return True
       elif item < glist[index]:
            return binarySearch(glist[:index], item)
       else:
            return binarySearch(glist[index+1:], item)
            
  










if __name__ == "__main__":
    
    ## Testing algos
    glist = [23,30,23,73,1,0,34,58,182,173,27]
    print(sequentialSearch(glist,35))
    glist.sort()
    print(orderedSequentialSearch(glist,35))
    print(binarySearch(glist,3))