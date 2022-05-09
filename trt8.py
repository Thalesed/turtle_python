import turtle
import math
 
x = turtle.Turtle()

x.pencolor("red")

x.speed(100)

factor = 1
n = 11

a = 0
b =1

# Fibonacci Spiral Plot
x.left(90)
for i in range(n):
    fdwd = math.pi * b / 2
    fdwd /= 90
    for j in range(90):
        x.forward(fdwd)
        x.left(1)
    temp = a
    a = b
    b = temp + b 
 

turtle.done()
