from turtle import *
color_list = ['cyan', 'black', 'red', 'yellow', 'limegreen']
pensize(4)
penup()
dic = {'green1': (50, -50), 'red': (100, 0), 'black': (0, 0), 'cyan': (-100, 0), 'yellow': (-50, -50)}
for i in dic:
    pencolor(i)
    goto(dic[i])
    pendown()
    circle(50)
    penup()




   