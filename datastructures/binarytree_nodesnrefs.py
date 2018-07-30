# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 01:33:28 2018
@author: Avinash

Implementing a Binary Tree using Nodes and References
"""

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.rightChild = None
        self.leftChild = None
        
    def insertRight(self, rightObj):
        if self.rightChild == None:
            self.rightChild = BinaryTree(rightObj)
        else:
            t = BinaryTree(rightObj)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def insertLeft(self, leftObj):
        if self.leftChild == None:
            self.leftChild = BinaryTree(leftObj)
        else:
            t = BinaryTree(leftObj)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def getRootVal(self):
        return self.key
        
    def setRootVal(self, newKey):
        self.key = newKey
        
    def getRightChild(self):
        return self.rightChild
        
    def getLeftChild(self):
        return self.leftChild
        
if __name__ == "__main__":
    
    myTree = BinaryTree('a')
    
    myTree.insertLeft('b')
    myTree.insertRight('c')
    lTree = myTree.getLeftChild()
    lTree.insertRight('d')
    
    print(lTree.getRootVal())
            


