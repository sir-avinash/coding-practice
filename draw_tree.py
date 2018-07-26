# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 07:23:56 2018

@author: avinash

"""
import turtle

def tree(turtle_obj, branchLen):
    if branchLen > 5:
        turtle_obj.forward(branchLen)
        turtle_obj..right(20)
        tree(turtle_obj, branchLen - 5)        
        




if __name__ = "__main__":
    
    t = turtle.Turtle()
    myWin = turtle.Screen()
    
    
    
    
    
    
    myWin.exitonclick()
    