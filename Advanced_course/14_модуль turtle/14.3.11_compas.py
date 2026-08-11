from turtle import *
from random import *

def direction(angle, x, y, text, align):
    pendown()
    left(angle)
    forward(200)
    penup()
    goto(x, y)
    write(text, align)
    goto(0,0)

hideturtle()
direction(0, 220, -5, "Восток", align='left')
direction(90, -12, 220, "Север", align='center')
direction(180, -240, -5, "Запад", align='right')
direction(270, -6, -220, "Юг", align='center')
goto(0, 50)
pendown()
circle(50)
mainloop()