from turtle import *

pensize(2)
penup()
goto(150, 200)
pencolor('red')
dot()
x = 0
for _ in range(10):
    pendown()
    pencolor('lightgreen')
    goto(x, 0)
    pencolor('blue')
    dot()
    penup()
    goto(150, 200)
    pendown()
    x += 30



   