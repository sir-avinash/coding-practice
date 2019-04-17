# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 01:30:58 2018
@author: Avinash

## Implementing a Tree datastructure

# Method1: Using a List of lists

 Start with a simple binary tree

"""

def binTree(rootName):
    return [rootName, [],[]] ## Initialized left and right child nodes

def insertRight(aTree, newRightBranch):
    t = aTree.pop(2)
    
    if len(t) > 1:
        aTree.insert(2, [newRightBranch, [], t])
    else:
        aTree.insert(2, [newRightBranch, [], []])
    return aTree

def insertLeft(aTree, newLeftBranch):
    t = aTree.pop(1)
    
    if len(t) > 1:
        aTree.insert(1, [newLeftBranch, t, []])
    else:
        aTree.insert(1, [newLeftBranch, [], []])
    return aTree

def getRootVal(aTree):
    return aTree[0]
    
def setRootVal(aTree, newName):
    aTree[0] = newName
    return aTree
    
def getRightChild(aTree):
    return aTree[2]
    
def getLeftChild(aTree):
    return aTree[1]
    

if __name__ == "__main__":
    myTree = binTree('a')
    
    print(myTree)
    
    insertRight(myTree, 'c')
    
    insertLeft(myTree, 'b')
    
    insertRight(getLeftChild(myTree), 'd')
    
    insertLeft(getRightChild(myTree), 'e')
    
    insertRight(getRightChild(myTree), 'f')
    
    lor = getLeftChild(getRightChild(myTree))
    rol = getRightChild(getLeftChild(myTree))
    
    print(lor)
    print(rol)
    print(myTree)

