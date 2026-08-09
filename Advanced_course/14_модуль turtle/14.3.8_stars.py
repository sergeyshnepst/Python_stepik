from turtle import *
from random import *

def star_(size):
    begin_fill()
    for _ in range(5): 
        forward(size * 100) 
        left(144)  
    end_fill()

colors = ['aliceblue', 'aquamarine', 'beige', 'blue', 'chocolate', 'orange', 'green','red', 'black', 'gold', 'white', 'pink', 'magenta1', 'purple']
bg_color = Screen().bgcolor(choice(colors))  
Screen().setup(400, 400)
for star in range(20):
    star_color = choice(colors)
    if star_color == bg_color:
        star_color = choice(colors)
    penup()
    goto(randint(-200, 200), randint(-200, 200))
    pendown()
    left(randrange(45))
    color(star_color,star_color)
    star_(random())
