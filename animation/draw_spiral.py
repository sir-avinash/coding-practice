# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 07:10:31 2018

@author: avinash

Using Turtle Module to draw a spiral
"""


import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)
        
        
drawSpiral(myTurtle,100)
myWin.exitonclick()
