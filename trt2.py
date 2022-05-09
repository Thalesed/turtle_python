import turtle
import math

truga = turtle.Turtle()

truga.color("red", "yellow")

truga.speed(90)

truga.begin_fill()
for c in range(0, 2000):
    truga.forward(math.sqrt(c))
    truga.left(1)
truga.end_fill()



turtle.done()
