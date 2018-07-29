# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 03:03:33 2018

@author: Avinash
"""

class HashTable:
    def __init__(self, tablesize=None):
        if tablesize is None:
            self.tablesize = 11
        else:
            self.tablesize = tablesize
        self.keys = [None]*self.tablesize
        self.values = [None]*self.tablesize

    def hashfunction(self, key):
        tableslot = key % self.tablesize
        return tableslot 
            
    def rehash(self, oldhash, rtype = None):
        if rtype == 'lin_probing':
            newslot = (oldhash + 1) % self.tablesize
        elif rtype == 'lin_probing_wskip':
            skip = 3
            newslot = (oldhash + skip) % self.tablesize
        elif rtype == 'quad_probing':
            newslot = (oldhash)**2 % self.tablesize
        else:
            newslot = (oldhash + 1) % self.tablesize            
        return newslot
           
    def put(self, key, value):
        slot = self.hashfunction(key)
        if self.keys[slot] == None:
            self.keys[slot] = key
            self.values[slot] = value
        elif self.keys[slot] == key:
            self.values[slot] = value
        else:
            newslot = self.rehash(slot)
            while self.keys[newslot] != None and self.keys[newslot] != key:
                newslot = self.rehash(newslot)
                
            if self.keys[newslot] == None:
                self.keys[newslot] = key
                self.values[newslot] = value
            else:
                self.values[newslot] = value #replace                
            
    def get(self, key):
        slot = self.hashfunction(key)
        
        if self.keys[slot] == key:
            return self.values[slot]
        else:
            newslot = self.rehash(slot)
            count = 0
            while self.keys[newslot] != key:
                newslot = self.rehash(newslot)
                if count > self.tablesize:
                    return None
                count += 1     
            return self.values[newslot]
        
    
    def __getitem__(self,key):
         return self.get(key)
     
    def __setitem__(self,key,value):
         return self.put(key,value)
        
#        
        

if __name__ == "__main__":
    
    new = HashTable(11)
    
    new.put(11,'eleven')

    new.put(12,'twelve')

    new.put(13,'thirteen')
    
    ## to verify if put() and hashfunction() work as designed
    print(new.keys) 
    
    new.put(22,'twentytwo')
    
    new.put(34,'thirtyfour')
    
    new.put(44,'fortyfour')
    
    new.put(35,'thirtyfive')
    ## to verify if rehash() works as designed    
    print(new.keys) ## ver

    new.put(11,'neweleven')
    
    new.put(44, 'newfortyfour')
    
    ## verify is values are replaced correctly
    print(new.values)
    
    ## verify get() method
    print(new.get(11))

    print(new.get(16))       
    
    ## verify setitem and getitem methods
    new[69] = 'sixtynine'
    
    new[82] = 'eightytwo'
    
    print(new.keys)
    print(new.values)
    print(new[22])