from turtle import *

def turtle_clock(angle):
    penup()
    stamp()
    for _ in range(12):
        forward(50)
        pendown()
        forward(15)
        penup()
        forward(10)
        stamp()
        backward(75)
        left(angle)

shape('turtle')
turtle_clock(360/12)



   