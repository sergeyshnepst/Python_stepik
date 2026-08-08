from turtle import *

def arrow(n):
    for i in range(n):
        forward(200)
        stamp()
        backward(200)
        left(360/n)

def net(n):
    for i in range(100):
        lt(360/n)
        fd(i)
        
n = 12
dot(15)
arrow(n)
lt(180/n)
net(n)




   