from turtle import *

def square(side):
    for i in range(4):
        left(90)
        forward(side)

side = 8       
for i in range(20):         
    square(side)
    side += 4


   