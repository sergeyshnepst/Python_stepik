from turtle import *

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'lightgreen', 'cyan', 'lightblue', 'blue', 'purple', 'pink']
def circle_(size, color):
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()

hideturtle()
speed(0)
size = 250
y = 0
for color in rainbow_colors:
    penup()
    goto(0, y)
    pendown()
    circle_(size, color)
    size -= 25
    y += 25
    
mainloop()



   