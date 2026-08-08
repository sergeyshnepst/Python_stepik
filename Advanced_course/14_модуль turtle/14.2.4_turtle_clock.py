from turtle import *

def turtle_clock(angle):
    penup()
    stamp()
    for _ in range(10):
        forward(50)
        stamp()
        backward(50)
        left(angle)

shape('turtle')
turtle_clock(36)



   