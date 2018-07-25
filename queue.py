# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 05:47:20 2018

@author: avinash
"""
class Queue:
    def __init__(self):
        # initialize and empty list
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        # add an item at the rear
        self.items.insert(0, item)
        
    def dequeue(self):
        # remove from the front
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
        
### Test it

if __name__ == "__main__":
    
    q = Queue()
    
    print(q.isEmpty())
    
    q.enqueue('q is')
    q.enqueue('legen')
    q.enqueue('wait-for-it')
    q.enqueue('dary')
    
    print(q.items)
    
    print(q.size())
    
    ch = q.dequeue()
    
    print(q.items)
    
    if ch == 'q is':
        print('First In First Out Yo! ')
        