from turtle import *

def circle_(color):
    fillcolor(color)
    begin_fill()
    circle(200)
    end_fill()

hideturtle()
speed(0)
penup()
bgcolor('darkblue')
circle_('yellow')
goto(50, 0)
circle_('darkblue')
    
mainloop()



   