# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 00:55:18 2018

All my sorting scripts. They all work, sort of(f). ;)

@author: Avinash
"""

def bubbleSort(alist):
    asize = len(alist)    
    for passnum in range(asize-1,0,-1):
        for index2 in range(passnum):
            if alist[index2] > alist[index2 + 1]:
                alist[index2], alist[index2 + 1] = alist[index2 + 1], alist[index2]            
    return alist

def shortBubbleSort(alist):
    
    # stop early if the list is sorted
    asize = len(alist)
    isSorted = True
    passnum = asize - 1
    while passnum > 0 and isSorted:
        isSorted = False
        for index2 in range(passnum):
            if alist[index2] > alist[index2 + 1]:
                alist[index2], alist[index2 + 1] = alist[index2 + 1], alist[index2]                        
                isSorted = True
        passnum -= 1       
    return alist


def selectionSort(alist):
    asize = len(alist)
    for passnum in range(asize - 1, 0, -1):
        maxval = alist[passnum]
        maxindex = passnum
        for index2 in range(passnum):
            if alist[index2] > maxval:
                maxval = alist[index2]
                maxindex = index2
        if maxindex == passnum:
            pass
        else:
            alist[maxindex],alist[passnum] = alist[passnum],maxval        
    return alist


def insertionSort(alist):
    asize = len(alist)
    sortlist = [alist[0]]
    for passnum in range(1, asize):
        newitem = alist[passnum]
        if newitem > alist[passnum-1]:
            sortlist.insert(passnum, newitem)
        else:
            isSorted = False
            for index in range(passnum-2, 0, -1):
                if newitem > alist[index]:
                    sortlist.insert(index+1, newitem)
                    isSorted = True
            if not isSorted:
                sortlist.insert(0,newitem)
    return alist       
                                
        
def gapInsertionSort(alist, start, gap):
    for passnum in range(start+gap,len(alist),gap):
        position = passnum
        currentval = alist[passnum]
        while alist[position - gap] > currentval and position >= gap:
            alist[position] = alist[position-gap]
            position -= gap
        
        alist[position] = currentval
    return alist
            

def shellSort(alist):    
    gapcount = len(alist)//2
    while gapcount > 0:
        for start in range(gapcount):
            alist = gapInsertionSort(alist, start, gapcount)
        gapcount = gapcount//2    
    return alist        
    
    
def mergeSort(alist):
    if len(alist) == 1:
#        print('sorted: ' + str(alist))
        return alist
    else:
        mid = len(alist)//2
        aleft = mergeSort(alist[0:mid])
        aright = mergeSort(alist[mid:len(alist)])
        ####### 
#        print('merging:' + str(aleft) + str(aright))
        i = j = k = 0
        while i < len(aleft) and j < len(aright):
            if aleft[i] < aright[j]:
                alist[k] = aleft[i]
                i += 1
            else:
                alist[k] = aright[j]
                j += 1
            k += 1
#        print(alist)
        return alist


def partition(alist, start, end):
    pivotValue = alist[start]
    leftMark = start + 1
    rightMark = end
    done = False
    
    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivotValue:
            leftMark += 1
            
        while leftMark <= rightMark and alist[rightMark] >= pivotValue:
            rightMark -= 1
            
        if leftMark > rightMark:
            done = True
        else:
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]

    alist[start], alist[rightMark] = alist[rightMark], alist[start]    
    return rightMark

def quickSortBackend(alist, start, end):
    if start < end:
        splitvalue = partition(alist, start, end)
        quickSortBackend(alist[start:splitvalue-1], start, splitvalue-1)
        quickSortBackend(alist[splitvalue+1:end], splitvalue+1, end)        
    
def quickSort(alist):
    return quickSortBackend(alist,0,len(alist)-1)
    
    



if __name__ == "__main__":
    alist = [12,4,56,78,2,34,83,90,12]
    print(bubbleSort(alist))
    print(shortBubbleSort(alist))
    print(selectionSort(alist))
    print(insertionSort(alist))
    print(shellSort(alist))
    print(mergeSort(alist))
    print(quickSort(alist))