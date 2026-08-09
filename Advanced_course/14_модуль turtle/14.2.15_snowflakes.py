from turtle import *
from random import *

def snowflake(size):
    for _ in range(8):
        beam(10*size, size)
    forward(15*size)
    left(45)
    forward(15*size)
    for i in range(8):
        center_pattern(15*size)  

def beam(length, size):
    forward(35*size)
    lines_45(length*size)
    forward(length)
    lines_45(length*size)
    backward(45*size)
    right(45)

def lines_45(length):
    left(45)
    forward(length)
    backward(length)
    right(45)
    forward(length)
    backward(length)
    right(45)
    forward(length)
    backward(length)
    left(45)
    forward(length)
    backward(length)

def center_pattern(lenght):
    left(135)
    forward(lenght)
    right(90)
    forward(lenght)

colors = ['aliceblue', 'aquamarine', 'beige', 'blue', 'chocolate', 'orange', 'green','red', 'black', 'gold', 'white', 'pink', 'magenta1', 'purple']
Screen().bgcolor(choice(colors))  
Screen().setup(400, 400)

for snowlake in range(20):
    penup()
    goto(randint(0, 400), randint(0, 400))
    pendown()
    pencolor(choice(colors))
    snowflake(random())




