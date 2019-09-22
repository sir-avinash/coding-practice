# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 18:12:58 2018

@author: Avinash
"""

class BinHeap:
    def __init__(self):
        self.heapList = [0] ## tree starts from index1
        self.currentSize = 0
        
    def isEmpty(self):
        return self.currentSize == 0
    
    def size(self):
        return self.currentSize
    
    ## Methods for inserting items and heapifying 
    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i] 
            i = i//2
                
    def insert(self, newItem):
        self.heapList.append(newItem)
        self.currentSize += 1
        self.percUp(self.currentSize)
    
    ## Methods for removing minItem and heapifying
    def minChild(self, i):
        if 2*i + 1 > self.currentSize:
            return 2*i
        elif self.heapList[2*i] <= self.heapList[2*i + 1]:
            return 2*i
        else:
            return 2*i + 1
    
    def percDown(self, i):
        while i*2 <= self.currentSize:
            i_mc = self.minChild(i) 
            if self.heapList[i] > self.heapList[i_mc]:
                self.heapList[i], self.heapList[i_mc] = self.heapList[i_mc], self.heapList[i]
            i = i_mc
            
    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        return val
    
    def buildHeap(self, alist):  
        self.heapList += alist[:]
        self.currentSize += len(alist) 
        i = len(alist)//2
        while i > 0:
            self.percDown(i)
            i -= 1

#    def heapSort(self, alist):
#        self.heapList += alist[:]
#        self.currentSize += len(alist)
#        for i in range(1,len(alist)):
#            self.buildHeap(alist[i:len(alist)])
#        return self.heapList[1:len(alist)]    
#            

if __name__ == "__main__":

    testList = [4,2,3,5,1,7]
    
    testHeap = BinHeap()
    for i in testList:
        print(i)
        testHeap.insert(i)
        print(testHeap.heapList)
        
    testHeap.delMin()
    print(testHeap.heapList)
    
    testHeap.delMin()
    print(testHeap.heapList)
    
    testHeap.insert(-2)
    print(testHeap.heapList[1:])
        
    testHeap2 = BinHeap()
    testHeap2.buildHeap(testList)
    
    print(testHeap2.heapList[1:])
    
#    print(BinHeap().heapSort(testList))