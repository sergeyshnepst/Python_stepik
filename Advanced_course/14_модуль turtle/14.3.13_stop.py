from turtle import *

speed(0)
hideturtle()
def octogon(length):
    pensize(5)
    for _ in range(8):
        forward(length)
        left(45)

octogon(100)
penup()
goto(5,10)
pendown()
begin_fill()
color('firebrick', 'firebrick')
octogon(91)
end_fill()

penup()
goto(-50, 70)
pendown()
pencolor('white')
write('STOP', font=('Arial', 58))

mainloop()
