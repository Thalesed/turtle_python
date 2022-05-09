import turtle
import math

trt = turtle.Turtle()

trt.speed(100)
trt.hideturtle()

def fib(turtle, num):

    turtle.color("blue")
    
    a = 0
    b = 1

    turtle.left(180)
    
    for j in range(0, num):
        turtle.forward(-a)
        turtle.right(90)
        for i in range(0, 3):
            turtle.forward(b)
            turtle.left(90)
        turtle.right(90)
        tmp = b
        b +=a
        a = tmp

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    a = 0
    b = 1

    turtle.color("red")
  
    #turtle.left(90)
    for i in range(num):
        equ = math.pi * b /2
        equ /= 90
        for j in range(90):
            turtle.forward(equ)
            turtle.left(1)
        tmp = a
        a = b
        b += tmp


fib(trt, 15)

turtle.done()
