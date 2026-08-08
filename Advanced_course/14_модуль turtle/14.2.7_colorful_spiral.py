from turtle import *

pensize(5)
n = 5
color_list = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', ]

for _ in range(10):
    for color in color_list:
        pencolor(color)
        forward(n)
        left(45)
        n += 2



   