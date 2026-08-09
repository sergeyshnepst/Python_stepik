from turtle import *

def case(color):
    fillcolor(color)
    begin_fill()
    for _ in range(2):
        forward(200)
        left(90)
        forward(600)
        left(90)
    end_fill()
    
def light(color):
    fillcolor(color)
    begin_fill()
    circle(80)
    end_fill()

hideturtle()
case('black')
goto(100, 410)
light('red')
goto(100, 220)
light('yellow')
goto(100, 30)
light('green')

mainloop()