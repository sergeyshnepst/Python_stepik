from turtle import *
import math

def planet(radius, color):
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def paint_planet(radius, color, x, text):
    speed(0)
    penup()
    goto(x, -radius)
    pendown()
    planet(radius, color)
    penup()
    goto(x, -radius-30)
    write(text, align='center', font=('Arial', 12, 'bold'))
    pendown()

def ellipse(a, b):
    dx = xcor()
    dy = ycor()
    penup()
    goto(dx, dy+100)
    pendown()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        goto(x, y+100)
 

hideturtle()
speed(0)

paint_planet(200, 'lightyellow', -1000, 'Солнце')
paint_planet(50, 'yellow3', -700, 'Меркурий')
paint_planet(75, 'yellow2', -520, 'Венера')
paint_planet(50, 'lightgreen', -350, 'Земля')
paint_planet(30, 'red', -240, 'Марс')
paint_planet(130, 'yellow3', -50, 'Юпитер')
paint_planet(140, 'yellow2', 270, 'Сатурн')
ellipse(170, 70)
paint_planet(100, 'lightblue', 570, 'Уран')
paint_planet(100, 'blue', 800, 'Нептун')
paint_planet(10, 'blue', 950, 'Плутон')

mainloop()