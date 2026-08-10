from turtle import *
from random import *

def black_square(length):
    fillcolor('black')
    begin_fill()
    for _ in range(4):
        forward(length)
        left(90)
    end_fill()
    forward(length)
    left(90)
    forward(length)
    right(90)
 

for blk in range(5):
    black_square(20)
penup()
goto(0,40)
pendown()
for blk in range(3):
    black_square(20)
penup()
goto(40,0)
pendown()
for blk in range(3):
    black_square(20)
penup()
goto(0,80)
pendown()
black_square(20)
penup()
goto(80,0)
pendown()
black_square(20)
penup()
goto(0,0)
pendown()
for _ in range(4):
        forward(100)
        left(90)


mainloop()