# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 05:49:53 2018

@author: avinash
"""


class Deque:
    def __init__(self):
        # initialize and empty list
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def addRear(self, item):
        # add an item at the rear
        self.items.insert(0, item)
    
    def addFront(self, item):
        # add an item at the front
        self.items.append(item)   
    
    def removeRear(self):
        # remove from the rear
        return self.items.pop(0)
        
    def removeFront(self):
        # remove from the front
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
        
### Test it

if __name__ == "__main__":
    
    q = Deque()
    
    print(q.isEmpty())
    
    q.addRear('q is')
    q.addFront('legen')
    q.addFront('wait-for-it')
    q.addFront('dary')
    
    print(q.items)
    
    print(q.size())
    
    ch = q.removeRear()
    
    print(q.items)
    
