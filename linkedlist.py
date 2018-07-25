# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 05:52:37 2018

@author: avinash

Linked List Implementaion

"""
"""
Linked List Implementation

"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.nextnode = None
        
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.nextnode
        
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.nextnode = newnext
        
        
class UnorderedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False 
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())        
    
    def search(self, item):  
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:   
                current = current.getNext()
        return found
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
            
        return count
        
    def index(self, item):
        count = 0 # head is 0 
        current = self.head
        
        if current.getData() == item:
            index = 0
        else:
            while current != None:
                count += 1
                current = current.getNext()
                if current.getData() == item:
                    index = count
        return index
        

if __name__ == "__main__":

    ## Testing Node Class
    temp = Node(34)
    
    ## wont work
    #print(temp.__data)
    
    ## will work
#    print(temp._Node__data)
    
    ## Testing UnorderedList
    
    newList = UnorderedList()
    
    print(newList.isEmpty())
    newList.add(20)
    newList.add(34)
    newList.add(45)
    newList.add(54)
    newList.add(21)

    print(newList.size())

    newList.remove(20)
    print(newList.search(20))
    
    newList.index(45)