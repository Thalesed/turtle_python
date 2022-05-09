import turtle
import time

trt = turtle.Turtle()

a = 0
b = 1

trt.penup()
trt.goto(-250, -250)
trt.pendown()

def fib(turtle, a, b):
    for i in range(0, 4):
        turtle.forward(a)
        turtle.left(90)
    for i in range(0, 4):
        turtle.forward(b)
        turtle.left(90)
    a += b
    b += a
    fib(turtle, a, b)

fib(trt, a, b)

turtle.done()
