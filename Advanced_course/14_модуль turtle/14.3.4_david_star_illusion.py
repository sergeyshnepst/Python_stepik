from turtle import *

def black_circle():
    fillcolor('black')
    begin_fill()
    circle(10)
    end_fill()

hideturtle()
for _ in range(3):
    forward(100)
    left(120)
penup()

goto(0, 40)
pendown()
black_circle()
penup()
goto(100, 40)
pendown()
black_circle()
penup()
goto(50, -45)
pendown()
black_circle()


goto(100, 50)
pendown()
pencolor('white')
fillcolor('white')
begin_fill()
for _ in range(3):
    right(120)
    forward(100)
end_fill()
    

mainloop()



   