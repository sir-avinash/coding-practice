"""
Created on Tue Apr 16 13:01:13 2019

@author: Avinash Siravuru
"""

import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print("parentdir=",parentdir)
os.sys.path.insert(0,parentdir)

from datastructuresuctures import stack, binarytree_nodesnrefs

class ParseTree:
  def __init__(self, pstack, ptree):
    self.pstack = Stack()
    self.ptree = BinaryTree('')
    
  def buildTree(self, stringexp):
    for key in stringexp:
      if key == '('
        newTree = BinaryTree('')
        self.pstack(newTree)
      elif key in {'0','1','2','3','4','5','6','7','8','9'}:
        parentTree = self.pstack.pop()
        if self.getLeftChild() is None:
          self.pTree 
    




if __name__ == "__main__":
  