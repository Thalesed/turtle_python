import turtle

truga = turtle.Turtle()

truga.color("red")

for c in range(0, 360):
    truga.forward(3)
    truga.left(1)
for c in range(0, 360):
    truga.forward(2.5)
    truga.left(1)
for c in range(0, 360):
    truga.forward(2)
    truga.left(1)
for c in range(0, 360):
    truga.forward(1.5)
    truga.left(1)
for c in range(0, 360):
    truga.forward(1)
    truga.left(1)
for c in range(0, 360):
    truga.forward(0.5)
    truga.left(1)

truga.penup()
truga.forward(100)
truga.pendown()

turtle.done()
