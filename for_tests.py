from turtle import *

def romb(side):
    for i in range(2):
        forward(side)
        left(50)
        forward(side)
        left(130)
   
for j in range(10):
    romb(100)
    left(36)

   